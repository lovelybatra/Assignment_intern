from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator

def index(request,request_args=None):
        requests_args = (requests_args or {}).copy()
        headers = get_headers(request.META)
        params = request.GET.copy()
        if 'headers' not in requests_args:
                requests_args['headers'] = {}
        if 'data' not in requests_args:
                requests_args['data'] = request.body
        if 'params' not in requests_args:
                requests_args['params'] = QueryDict('', mutable=True)
        headers.update(requests_args['headers'])
        params.update(requests_args['params'])
        for key in list(headers.keys()):
                if key.lower() == 'content-length':
                        del headers[key]
        requests_args['headers'] = headers
        requests_args['params'] = params
        response = requests.request(request.method, url, **requests_args)
        proxy_response = HttpResponse(
                response.content,
                status=response.status_code)

        excluded_headers = set([
                'connection', 'keep-alive', 'proxy-authenticate', 
        'proxy-authorization', 'te', 'trailers', 'transfer-encoding', 
        'upgrade', 'content-encoding','content-length',])
        for key, value in response.headers.items():
                if key.lower() in excluded_headers:
                        continue
                proxy_response[key] = value
        return proxy_response

def get_headers(environ):
        headers = {}
        for key, value in environ.items():
                if key.startswith('HTTP_') and key != 'HTTP_HOST':
                         headers[key[5:].replace('_', '-')] = value
                elif key in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                        headers[key.replace('_', '-')] = value
                return headers
                

        
	
    
	
    
    
    
	
    


