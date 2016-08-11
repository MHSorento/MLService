from SimpleHTTPServer import SimpleHTTPRequestHandler
import json
import re
from mlengine import closest_skus

class Handler(SimpleHTTPRequestHandler):
	def do_GET(self):
		if None != re.search('/recommendations/*', self.path):
			sku = self.path.split('/')[-1]
			finder = closest_skus.SKUFeatureValues()
			recs = finder.get_closest_sku(sku, 5)
			if sku is not None and recs is not None:
				self.send_response(200)
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
				self.wfile.write(json.dumps(recs))
			else:
				self.send_response(400, 'Bad Request: record does not exist')
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
		else:
			self.send_response(403)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()

		return