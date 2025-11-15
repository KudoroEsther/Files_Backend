from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [{
    'Name': "Esther",
    'Track': "AI_Engineer"
},

    {
    'Name': "Bolu",
    'Track': "AI_Developer"
}
]

class BaseAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status = 200):
        self.send_response(status)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_DELETE(self):
        content_size = int(self.headers.get('content-Length', 0))
        raw_data = self.rfile.read(content_size)
        new_data = json.loads(raw_data.decode())
        for i in data:
            if i['Name'] == new_data['Name']:
                data.remove(i)
            self.send_data({
                'Message': "Data removed",
                'data': data
            }, status=200)

def run():
    HTTPServer(('localhost', 8000), BaseAPI).serve_forever()

print("Application is running")
run()