#!/usr/bin/env python3
"""Tiny static server for local play: python3 serve.py [port]"""
import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8471
print(f"Serving Forgotten Northern Towns at http://localhost:{port}")
HTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler).serve_forever()
