# main program

import sys
import os
import router
import project
import urllib
import re
import view

from wsgiref.simple_server import make_server
from wsgiref.util import *

def nbugtrack(environ, start_response):
    path = environ['PATH_INFO'];
    method = environ['REQUEST_METHOD']

    if method == 'GET':
        
        if environ["QUERY_STRING"] != '':
            query = path+"?"+urllib.unquote(environ["QUERY_STRING"])
        else:
            query = path
            
        # does a type dispatch and prints the content
        response = view.showView(router.match(query))
        
        status = '200 OK'
        headers = [('Content-type', 'text/html'), 
                   ('Content-length', str(len(response)))]
    
        start_response(status, headers)
        return [response]
    
    elif method == 'POST':
        if path.startswith('/update_wiki'):
            try:
                request_len = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_len)
                param_table = parse_post_request(request_body)
                response_body = view.showView(project.update_wiki(param_table['id'], param_table['content']))
                print(response_body)

                status = '200 OK'
                headers = [('Content-type', 'text/html'), 
                           ('Content-length', str(len(response_body)))]

                start_response(status, headers)
                return [response_body]
            except:
                response_body = "error"

# regexes are great when you want
def parse_post_request(request_body):
    request_tokens = request_body.split('\r\n') # sends CR LF
    var_alist = {}

    # remove unwanted chars
    for i in request_tokens:
        if re.compile('^([-]+)([\w]*)([-]*)').search(i):
            request_tokens.remove(i)
        if i == "":
            request_tokens.remove(i)
        
    index = 0

    for i in request_tokens:
        tmpname =  re.compile('Content-Disposition: form-data; name="([\w]+)"$').search(i)

        if tmpname != None:
            name = ' '.join(i for i in list(tmpname.groups()))
            request_tokens[index] = name

        index = index + 1

    # but regexes need not be used everywhere
    while(len(request_tokens) != 0):
        try:
            name = request_tokens.pop(0)
            value = request_tokens.pop(0)
            var_alist[name] = value            
        except IndexError:
            break

    return var_alist
            
if __name__ == '__main__':
    port_to_run = 8765 # default port

    try:
        if len(sys.argv) == 2:
            port_to_run = argv[1]
        httpd = make_server('', port_to_run, nbugtrack)
        httpd.serve_forever()
    except KeyboardInterrupt:
        exit()
