import http.server
import socketserver
import logging

log = logging.getLogger(__file__)

PORT = 8000
class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print("Requested path: {}".format(self.path))
        if self.path == '/life':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            response = bytearray('The meaning of life is 42', 'utf-8')
            self.wfile.write(response)
            return
        super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
