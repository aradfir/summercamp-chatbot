from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from os import listdir, getcwd
from os.path import isfile, join, isdir

ADDRESS = 'localhost'
PORT = 10000
current_directory = getcwd()


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 response
        self.send_response(200)
        # send response headers
        self.end_headers()
        # send the body of the response
        parsed = urlparse(self.path)
        relative_path = parsed.path[1:]
        absolute_path = join(current_directory, relative_path)
        print(relative_path)
        all_items = listdir(absolute_path)
        onlyfiles = [f for f in all_items if isfile(join(absolute_path, f))]
        onlydirs = [f for f in all_items if isdir(join(absolute_path, f))]
        result = b"RESULT FOR : " + absolute_path.encode()
        result += b"\nFILES:\n" + "\n".join(onlyfiles).encode() + b"\nDIRS:\n" + "\n".join(onlydirs).encode()
        self.wfile.write(result)


httpd = HTTPServer((ADDRESS, PORT), MyHandler)
httpd.serve_forever()
