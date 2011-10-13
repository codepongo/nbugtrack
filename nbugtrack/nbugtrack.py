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
        response = router.match(query)

        if response != None:
            content_type = "text/html"
            status = "200 OK"
            response = view.showView(response)

            if type(response) == list: # resource
                content_type = response[1]
                response = response[0]

                if content_type == 'none':
                    status = '404 Not Found'

            headers = [('Content-type', content_type), 
                       ('Content-length', str(len(response)))]
    
            start_response(status, headers)
            return [response]
        else:
            return ["error"]
    elif method == 'POST':
        response_body = ""
        try:
            request_len = int(environ['CONTENT_LENGTH'])
            request_body = environ['wsgi.input'].read(request_len)
            param_table = parse_post_request(request_body)
                
            if path.startswith('/update_project'):
                response_body = view.showView(project.update_project(param_table['id'], param_table['desc']))
            elif path.startswith('/update_bug'):
                response_body = view.showView(project.update_bug(param_table['id'], param_table['params']))
            elif path.startswith('/update_wiki'):
                response_body = view.showView(project.update_wiki(param_table['id'], param_table['content']))
            else:
                response_body = "No Content"
        except:
            response_body = "error"
        
        status = '200 OK'
        headers = [('Content-type', 'text/html'), 
                  ('Content-length', str(len(response_body)))]

        start_response(status, headers)
        return [response_body]
            
# parse a post request
def parse_post_request(request_body):
    request_tokens = request_body.split('\r\n') # sends CR LF
    var_alist = {}

    # remove unwanted chars
    for i in request_tokens: # regexes are great when you want
        if re.compile('^([-]+)([\w]*)([-]*)').search(i):
            request_tokens.remove(i)
        if i == "":
            request_tokens.remove(i)
        
    index = 0

    for i in request_tokens:
        tmpname =  re.compile('Content-Disposition: form-data; name="([\w]+)"$').search(i)

        if tmpname != None:
            request_tokens[index]  = ' '.join(i for i in list(tmpname.groups()))
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
