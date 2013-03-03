class MyMiddleware(object):
    def process_response(self, request, response):
        response['caner'] = 'candan'
        return response
