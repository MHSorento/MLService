from SimpleHTTPServer import SimpleHTTPRequestHandler
import json
import re

class Handler(SimpleHTTPRequestHandler):
	def do_GET(self):
		if None != re.search('/recommendations/*', self.path):
			sku = self.path.split('/')[-1]
			if sku is not None:
				self.send_response(200)
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
				self.wfile.write(json.dumps(
					{ 'recommendations' : [
						'MIN-001-GNA',
						'MIN-002-GNA',
						'MIN-003-GNA',
						'MIN-004-GNA',
						'MIN-005-GNA']
				}))
			else:
				self.send_response(400, 'Bad Request: record does not exist')
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
		else:
			self.send_response(403)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()

		return