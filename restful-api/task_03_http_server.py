import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            error = json.dumps({"error": "404 Not Found", "message": "The requested endpoint does not exist."}).encode("utf-8")

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"Not Found")


if __name__ == "__main__":
    PORT = 8000
    server = http.server.HTTPServer(("", PORT), SimpleAPIHandler)
    print(f"Server running on http://localhost:{PORT}")
    print("Endpoints: /  |  /data  |  /status")
    server.serve_forever()
