# main program

import sys
import os
import io
import time
import re
import urllib

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
    content_type = environ['CONTENT_TYPE']

    if method == 'GET':        
        if environ["QUERY_STRING"] != '':
            qs = environ["QUERY_STRING"]
            qs = urllib.parse.unquote_plus(qs) if nbt_global.python_version == '3' else urllib.unquote_plus(qs)
            query = path+"?"+qs
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
                cache_policy = 'max-age='+str(3600 * 24 * 30)
				
                if content_type == 'none':
                    status = '404 Not Found'
                elif content_type.startswith('image'):
                    image_encoding = True
                elif content_type == 'text/html':
					cache_policy = 'no-store, no-cache'
					
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

        elif response == None:
            headers = [('Content-type', 'text/plain')]
            status = '200 OK'
            start_response(status, headers)
            return [b"error"]

    elif method == 'POST':
        if content_type == 'application/x-www-form-urlencoded':
            parse_fn = parse_form_urlencoded_request
        elif content_type == 'application/x-www-form-urlencoded; charset=UTF-8':
            parse_fn = parse_form_urlencoded_request
        elif content_type == 'multipart/form-data':
            parse_fn = parse_multipart_formdata_request

        response = ""
        try:
            expires_by = time.strftime("%a, %d %b %Y %H:%M:%S %Z")
            cache_policy = 'no-store, no-cache'
            content_enc = 'gzip'
            response_is_list = False
            request_len = int(environ['CONTENT_LENGTH'])
            request = environ['wsgi.input'].read(request_len)
            param_table = parse_fn(request)
            # XXX: I should put another dispatch table for post requests in router
            if path.startswith('/update_project'):
                response = view.showView(project.update_project(param_table['name'], param_table['desc']))
            elif path.startswith('/new_project'):
                print(param_table['name'] + " "+ param_table['desc'])
                response = view.showView(project.new_project(param_table['name'], param_table['desc']))
            elif path.startswith('/rename_project'):
                response = view.showView(project.rename_project(param_table['oldname'], param_table['newname']))
            elif path.startswith('/rename_wiki'):
                response = view.showView(project.rename_wiki(param_table['wiki_id'], param_table['newname']))
            elif path.startswith('/new_wiki'):
                response = view.showView(project.new_wiki(param_table['project_name'],param_table['name'], param_table['content']))
            elif path.startswith('/new_bug'):
                response = view.showView(project.new_bug(param_table['project_name'],param_table['shortname']))
            elif path.startswith('/update_bug'):
                response = view.showView(project.update_bug(param_table['id'], param_table['params']))
            elif path.startswith('/update_wiki'):
                response = view.showView(project.update_wiki(param_table['id'], param_table['content']))
            elif path.startswith('/send_wtext'):
                response = view.showView(project.send_wtext(param_table['id']))
                response_is_list = True
                content_enc = 'text'
            else:
                response = "No Content"
        except Exception as e:
            print(str(e))
            response = "error" 

        if response_is_list: # for the jquery response
            response =  str(response[0])
       
        status = '200 OK'
        headers = [('Content-type', 'text/html'), 
                   ('Content-length', str(len(response))),
                   ('Content-encoding', content_enc),
                   ('Cache-Control', cache_policy),
                   ('Expires', expires_by)]

        start_response(status, headers)
        
        if response_is_list:            
            return [response]
        
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

# parse a xxx-url-form-encoded request
def parse_form_urlencoded_request(request_body):
    var_alist = {}
    request_body = str(request_body, 'utf-8') if nbt_global.python_version == '3' else str(request_body)
    for i in request_body.split('&'):
        if i != "":
            nv = i.split('=')
            var_alist[nv[0]] = urllib.parse.unquote_plus(nv[1]) if nbt_global.python_version == '3' else urllib.unquote_plus(nv[1])
    print(var_alist)
    return var_alist

# parse a multipart/form-data post request
def parse_multipart_formdata_request(request_body):
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
            request_tokens[index]  = ' '.join(i for i in list(tmpname.groups()))
        index = index + 1

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
        print("Open http://localhost:"+str(port_to_run)+" in your browser...")
        httpd = make_server('', port_to_run, nbugtrack)
        httpd.serve_forever()
    except KeyboardInterrupt:
        exit()
