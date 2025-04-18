# auto_resolver.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = 9001
DIR_TO_CLEAN = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/overflow_test_dir"

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Received alert from Grafana. Cleaning up...")
        try:
            for f in os.listdir(DIR_TO_CLEAN):
                file_path = os.path.join(DIR_TO_CLEAN, f)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("✅ Cleanup completed.")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Cleanup done.")
        except Exception as e:
            print("❌ Error during cleanup:", e)
            self.send_response(500)
            self.end_headers()

httpd = HTTPServer(('', PORT), RequestHandler)
print(f"Listening on port {PORT} for Grafana alert webhooks...")
httpd.serve_forever()
