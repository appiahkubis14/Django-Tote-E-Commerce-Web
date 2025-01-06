from .models import Customer

class CustomerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add customer to request if logged in
        
        customer_id = request.session.get('customer_id')
        if customer_id:
            try:
                request.customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                request.customer = None
        else:
            request.customer = None

        response = self.get_response(request)
        return response
