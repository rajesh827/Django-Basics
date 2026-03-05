import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        print(f"➡️ Incoming Request: {request.method} {request.path}")

        response = self.get_response(request)

        duration = time.time() - start_time
        
        print(f"✅ Request completed in: {duration:.4f} seconds\n")

        return response