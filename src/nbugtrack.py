# main program

import sys
import os

from wsgiref.simple_server import make_server

def nbugtrack(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    
    start_response(status, headers)

    return "Hello, world"

if __name__ == '__main__':
    port_to_run = 8765

    try:
        if len(sys.argv) == 2:
            port_to_run = argv[1]
        httpd = make_server('', port_to_run, nbugtrack)
        httpd.serve_forever()
    except KeyboardInterrupt:
        exit()
