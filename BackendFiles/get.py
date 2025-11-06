from http.server import BaseHTTPRequestHandler,HTTPServer
import json

data = [{
    'name':'Sam larry',
    'track':'Ai Engineer'
}]


class BaseAPI(BaseHTTPRequestHandler):
    def send_data(self,data,status=200): #function to send data
        self.send_response(status) #setting the response
        self.send_header('content-type','application/json') #sendthe header
        self.end_headers() # saying that thats all for header ,move to body
        self.wfile.write(json.dumps(data).encode()) #this takes what is in the body and saves(dump) in json format and encodes it i.e in bytes

    def do_GET(self):
        self.send_data(data)

def run():
    HTTPServer(('localhost',8000),BaseAPI).serve_forever() #start a web server that listens on port 8000


print('Application is running')
run()