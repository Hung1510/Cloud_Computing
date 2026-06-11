from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time 

PORT = int(sys.argv[1])
INSTANCE = sys.argv[2]
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(3)
        self.send_response(200)
        self.end_headers()
        message = f"Hello from instance {INSTANCE}"
        self.wfile.write(message.encode())
server = HTTPServer(("localhost", PORT), Handler)
print(f"Running instance {INSTANCE} on port {PORT}")
server.serve_forever()