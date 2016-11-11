#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


# http://localhost:8000/lizhitao
def application(environ, start_response):
    # method = environ['REQUEST_METHOD']
    # path = environ['PATH_INFO']
    # if method=='GET' and path=='/':
    #     return handle_home(environ, start_response)
    # if method=='POST' and path='/signin':
    #     return handle_signin(environ, start_response)

    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


httpd = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
