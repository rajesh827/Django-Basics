#Q7
import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization when the server starts.

    def __call__(self, request):
        # 1. Code executed BEFORE the view is called (Incoming Request)
        start_time = time.time()
        
        # Print the request method (GET/POST) and the URL path
        print(f"➡️ Incoming Request: {request.method} {request.path}")

        # This passes the request to the next middleware or the actual View
        response = self.get_response(request)

        # 2. Code executed AFTER the view is called (Outgoing Response)
        duration = time.time() - start_time
        
        # Print the time it took to complete
        print(f"✅ Request completed in: {duration:.4f} seconds\n")

        return response