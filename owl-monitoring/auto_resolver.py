from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import subprocess
import threading

PORT = 9001
DIR_TO_CLEAN = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/overflow_test_dir"
DB_DIR = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/databaseError_test_dir"
CLEAN_CPU = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/cleanCPU.py"
CLEAN_MEMORY = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/cleanMemory.py"
def handle_alert_background(alertname):
    try:
        print(f"⚠️ Alert received: {alertname}")
        if "CPU" in alertname:
            print("🛠 Running CPU cleanup...")
            subprocess.run(["python3", CLEAN_CPU])
        elif "Memory" in alertname:
            print("🧠 Running Memory cleanup...")
            subprocess.run(["python3", CLEAN_MEMORY])
        elif "Database" in alertname:
            print("🧾 Cleaning up database errors...")
            for f in os.listdir(DB_DIR):
                file_path = os.path.join(DB_DIR, f)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted DB error file: {file_path}")
        elif "Directory" in alertname:
            print("📁 Cleaning up directory overflow...")
            for f in os.listdir(DIR_TO_CLEAN):
                file_path = os.path.join(DIR_TO_CLEAN, f)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted overflow file: {file_path}")
        else:
            print("ℹ️ Unknown alert type. No action taken.")
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            alerts = data.get("alerts", [])
            for alert in alerts:
                alertname = alert["labels"].get("alertname", "Unknown")
                threading.Thread(target=handle_alert_background, args=(alertname,)).start()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Auto-resolution complete.")
        except Exception as e:
            print("❌ Error in alert handling:", e)
            self.send_response(500)
            self.end_headers()

if __name__ == "__main__":
    httpd = HTTPServer(('0.0.0.0', PORT), RequestHandler)
    print(f"🚀 Listening on port {PORT} for Grafana alert webhooks...")
    httpd.serve_forever()

