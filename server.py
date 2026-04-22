#!/usr/bin/env python3
"""
Simple HTTP server for the workflow dashboard.
Run with: python3 server.py
"""

import http.server
import socketserver
import os
import webbrowser
from datetime import datetime

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Custom log format with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.address_string()} - {format % args}")
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    
    print("=" * 60)
    print("🤖 Team BB Workflow Dashboard")
    print("=" * 60)
    print(f"Server starting on port {PORT}")
    print(f"Dashboard URL: http://localhost:{PORT}/")
    print(f"Directory: {DIRECTORY}")
    print("\nAvailable files:")
    for file in os.listdir('.'):
        if file.endswith('.html'):
            print(f"  • {file}")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)
    
    # Try to open browser automatically
    try:
        webbrowser.open(f'http://localhost:{PORT}/')
        print("✓ Browser opened automatically")
    except:
        print("⚠ Could not open browser automatically")
        print("  Please open: http://localhost:{PORT}/")
    
    # Start server
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped by user")
            httpd.shutdown()

if __name__ == "__main__":
    main()