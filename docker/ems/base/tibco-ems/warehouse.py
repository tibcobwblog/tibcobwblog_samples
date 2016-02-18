#!/usr/bin/env python3

import http.server
import os
import socketserver
import sys

PORT = 18000


def run():
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)

    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    # First argument is the directory to serve files from
    os.chdir(sys.argv[1])
    run()
