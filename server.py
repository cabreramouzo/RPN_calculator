import http.server
import socketserver
import logging

log = logging.getLogger(__file__)

PORT = 8000
class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print("Requested path: {}".format(self.path))
        super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
