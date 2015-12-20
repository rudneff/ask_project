def is_post_request(environ):
    if environ['REQUEST_METHOD'].upper() in 'POST':
        return True
    else:
        return False


def app(environ, start_response):
    request_body = ''
    if is_post_request(environ):
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size)
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [
        'method: ', environ.get('REQUEST_METHOD', ''), '\n',
        'path info:  ', environ.get('PATH_INFO', ''), '\n',
        'query string: ', environ.get('QUERY_STRING', ''), '\n',
        'body: ', request_body, '\n\n'
        'Hello here!\n'
    ]
