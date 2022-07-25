from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 response
        self.send_response(200)
        # send response headers
        self.end_headers()
        # send the body of the response
        parsed = urlparse(self.path)
        query_string = parsed.query
        path = parsed.path
        self.wfile.write(b'It works!')

httpd = HTTPServer(('localhost', 10000), MyHandler)
httpd.serve_forever()