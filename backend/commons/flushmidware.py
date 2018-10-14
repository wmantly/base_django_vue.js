import sys


def flushWare(get_response):
    sys.stdout.flush()
    sys.stderr.flush()
    
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        sys.stdout.flush()
        sys.stderr.flush()

        return response

    return middleware
