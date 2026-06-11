import itertools
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

servers = [ 
    "http://localhost:8001", 
    "http://localhost:8002", 
    "http://localhost:8003", 
    "http://localhost:8004" 
] 

cycle = itertools.cycle(servers)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        for _ in range(len(servers)):
            target = next(cycle)
            try:
                response = requests.get(target, timeout=1)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(response.content)
                return
            except:
                continue

        # If all servers fail
        self.send_response(500)
        self.end_headers()
        self.wfile.write(b"All servers are down")

server = HTTPServer(("localhost", 9000), Handler)
print("Load balancer running on port 9000")
server.serve_forever()