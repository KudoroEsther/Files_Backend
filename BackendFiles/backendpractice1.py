from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler
import json


data = [{
    "name":"Sam Larry",
    "track": "Developers"
}]

class BasciApi(BaseHTTPRequestHandler):
    #get endpoint: data is being sent from the server to the client
    def send_data(self, data, status=200): #status=200 means things are working perfectly
        
        #calling functions from BaseHTTPRequestHandler
        self.send_response(status)
        #this indicates the type of data being sent
        self.send_header('content-type', 'application/json') #header is the data that accompanies the data being sent through an endpoint. It gives the endpoint an idea of the type of data being sent. The types include texts, media, files
        self.end_headers()#ends the header
        #the main file
        self.wfile.write(json.dumps(data).encode())