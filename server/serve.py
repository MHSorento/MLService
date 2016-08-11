import SimpleHTTPServer
import SocketServer
from handler import Handler

PORT = 8000

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
