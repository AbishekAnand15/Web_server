from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
</head>
<body>
<h1>Welcome</h1>
<h2>AbishekXavier</h2>
<h3>22008833</h3>
<h4>list of frameworks</h4>
<h5>django</h5>
<h5>ruby on rails</h5>
<h5>flask</h5>
</html>
"""


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())


server_address = ('',80)
httpd = HTTPServer(server_address,HelloHandler)
httpd.serve_forever()