# Developing a Simple Webserver

# AIM:
To Develop A Web server

# DESIGN STEPS:

## Step 1:

HTML content creation is done

## Step 2:

Design of webserver workflow

## Step 3:

Implementation using Python code

## Step 4:

Serving the HTML pages.

## Step 5:

Testing the webserver

# PROGRAM:
```python
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
</head>
<body>
<h1>Welcome</h1>
<p>AbishekXavier</p>
<p>22008833</p>
<p>list of frameworks</p>
<p>django</p>
<p>ruby on rails</p>
<p>flask</p>
</body>
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
```

# OUTPUT:
![output](output1.png)
![output](output.png)

# RESULT:

The program is executed succesfully
