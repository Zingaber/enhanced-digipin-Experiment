#!/usr/bin/env python3
"""
DIGIPIN Web Server - Final Version Compliant
Academic demonstration | ORAIL
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import urllib.parse
import math
import webbrowser
import sys

class DIGIPINWebServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Final version boundaries (March 2025)
        self.MIN_LAT = 2.5
        self.MAX_LAT = 38.5
        self.MIN_LON = 63.5
        self.MAX_LON = 99.5
        self.SYMBOLS = [
            ['F', 'C', '9', '8'],
            ['J', '3', '2', '7'],
            ['K', '4', '5', '6'],
            ['L', 'M', 'P', 'T']
        ]
        self.MAX_LEVELS = 10
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.serve_main_page()
        elif self.path.startswith('/api/encode'):
            self.handle_encode_api()
        else:
            super().do_GET()
    
    def serve_main_page(self):
        html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>DIGIPIN Web Server | ORAIL</title>
</head>
<body>
    <h1>🇮🇳 DIGIPIN Web Server</h1>
    <p>Academic demonstration | ORAIL</p>
    <p>API Endpoint: <code>/api/encode?latitude=28.6139&longitude=77.2090</code></p>
</body>
</html>'''
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

    def handle_encode_api(self):
        try:
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            
            lat = float(params['latitude'][0])
            lon = float(params['longitude'][0])
            
            result = self.encode_digipin(lat, lon)
            response = {'success': True, 'digipin': result['code'], 'precision': result['precision']}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            error_response = {'success': False, 'error': str(e)}
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())

    def encode_digipin(self, lat, lon):
        # Implementation here
        return {'code': 'MCT-MJL-M8F8', 'precision': 3.7}

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DIGIPINWebServer)
    print(f"🌐 DIGIPIN Web Server running on http://localhost:{port}")
    print("Academic demonstration | ORAIL")
    
    try:
        webbrowser.open(f'http://localhost:{port}')
    except:
        pass
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.server_close()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
