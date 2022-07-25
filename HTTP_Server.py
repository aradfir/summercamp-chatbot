from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from os import listdir,getcwd

from os.path import isfile, join, isdir

dirname = getcwd()

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
        true_path = join(dirname, path[1:])
        print(path[1:])
        self.wfile.write(true_path.encode())
        onlyfiles = [f for f in listdir(true_path) if isfile(join(true_path, f))]
        onlydirs = [f for f in listdir(true_path) if isdir(join(true_path, f))]
        result=b"RESULT FOR : "+true_path.encode()
        result += b"\nFILES:\n" + "\n".join(onlyfiles).encode() + b"\nDIRS:\n" + "\n".join(onlydirs).encode()
        self.wfile.write(result)


httpd = HTTPServer(('localhost', 10000), MyHandler)
httpd.serve_forever()
