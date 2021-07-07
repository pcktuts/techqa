from django.http import JsonResponse

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("got a request")

        response = self.get_response(request)
        #return JsonResponse({'foo': 'bar'})
        # Code to be executed for each request/response after
        # the view is called.

        return response