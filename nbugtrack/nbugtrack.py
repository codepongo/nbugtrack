# main program

import sys
import os
import io
import time
import re

import nbt_global
import router
import project
import gzip
import view

from wsgiref.simple_server import make_server
from wsgiref.util import *

def nbugtrack(environ, start_response):
    path = environ['PATH_INFO'];
    method = environ['REQUEST_METHOD']

    if method == 'GET':        
        if environ["QUERY_STRING"] != '':
            query = path+"?"+environ["QUERY_STRING"]
        else:
            query = path
            
        # does a type dispatch and prints the content
        response = router.match(query)

        if response != None:
            content_type = "text/html"
            status = "200 OK"
            response = view.showView(response)
            expires_by = time.strftime("%a, %d %b %Y %H:%M:%S %Z")
            cache_policy = 'no-store, no-cache'
            image_encoding = False

            if type(response) == list: # resource
                content_type = response[1]
                response = response[0]
                expires_by = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(time.time() + 3600 * 24 * 30)) # expire a month from now
                cache_policy = 'only-if-cached, max-age='+str(3600 * 24 * 30)

                if content_type == 'none':
                    status = '404 Not Found'
                elif content_type.startswith('image'):
                    image_encoding = True

            # see: http://developer.yahoo.com/performance/rules.html
            #      www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
            headers = [('Content-type', content_type),
                       ('Content-encoding', 'gzip'),
                       ('Content-length', str(len(response))),
                       ('Cache-Control', cache_policy),
                       ('Expires', expires_by)]
    
            start_response(status, headers)

            if nbt_global.python_version == '3':
                if image_encoding == True:
                    return [gzip.compress(bytes(response))]
            
            return [gzip.compress(bytes(response,"utf-8"))] if nbt_global.python_version == '3' else [compress(response)]  # gzip compression
        else:
            return ["error"]
    elif method == 'POST':
        response = ""
        try:
            request_len = int(environ['CONTENT_LENGTH'])
            request = environ['wsgi.input'].read(request_len)
            param_table = parse_post_request(request_body)
                
            if path.startswith('/update_project'):
                response = view.showView(project.update_project(param_table['id'], param_table['desc']))
            elif path.startswith('/update_bug'):
                response = view.showView(project.update_bug(param_table['id'], param_table['params']))
            elif path.startswith('/update_wiki'):
                response = view.showView(project.update_wiki(param_table['id'], param_table['content']))
            else:
                response = "No Content"
        except:
            response = "error"
        
        status = '200 OK'
        headers = [('Content-type', 'text/html'), 
                  ('Content-length', str(len(response)))]

        start_response(status, headers)
        return [gzip.compress(bytes(response, "utf-8"))] if sys.version[:1] == '3' else [compress(response)]  # gzip compression

# gzip compression for strings was added from 3.0, the following
# functions make it work with 2.x:
#      http://bugs.python.org/file15282/gzip.py.svndiff
def compress(data, compresslevel=9):
    """ Compress data in one shot. Returns the compressed string.
    Optional argument is the compression level, in range of 1-9. """
    
    bf = io.BytesIO(b'')
    f = gzip.GzipFile(fileobj = bf, mode = 'wb', compresslevel = compresslevel)
    f.write(data)
    f.close()

    return bf.getvalue()

def decompress(data):
    """ Decompress a gzip compressed string in one shot.
    Returns the decompressed string. """

    f = gzip.GzipFile(fileobj = io.BytesIO(data))
    return f.read()    

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
