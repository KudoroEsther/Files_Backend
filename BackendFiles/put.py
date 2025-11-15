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

# Defining a class that inherits the characteristics of BaseHTTPRequestHandler
class BaseAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())
    
    #Defining the put function
    def do_PUT(self):
        content_size = int(self.headers.get('Content-Length', 0))
        raw_data = self.rfile.read(content_size)
        new_data = json.loads(raw_data)
        for i in data: 
            if i['Name'] == new_data['Name']:
                i.update(new_data)
                self.send_data({
                    'Message': "Data received",
                    'Data': data
                })
    

#Running the class
def run():
    HTTPServer(('localhost', 3000), BaseAPI).serve_forever()

print("Application is running")
run()



# class BasicAPI(BaseHTTPRequestHandler):
#     def send_data(self, payload, status = 200):
#         self.send_response(status)
#         self.send_header("Content-Type", "application/json")
#         self.end_headers()
#         self.wfile.write(json.dumps(payload).encode())

#     def do_GET(self):
#         self.send_data({"Message": "Data received successfully", "Data": data})

#     def do_PUT(self):
#         cotent_size =int(self.headers.get("Content-Length",0))
#         parsed_data = self.rfile.read(cotent_size)
#         pUT_data = json.loads(parsed_data)
#         if data:
#             data[0] = pUT_data
#             self.send_data({
#             "Message":"Data Replaced",
#             "data":data[0]
#         })
#         else:
#           data.append(pUT_data)
#           self.send_data({
#             "Message":"Data Addeded",
#             "data":pUT_data
#         })
# def run():
#     HTTPServer(("localhost", 5000), BasicAPI).serve_forever()
# print("Application is running")
# run()