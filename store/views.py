from .models import Store , Cart
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Payment, Order
from .utils import Paystack
from django.http import Http404
import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect, HttpResponseRedirect 
from django.contrib.auth.hashers import check_password ,make_password
from .models import Customer 
from django.views import View 
from django.contrib.auth import authenticate, login

class Signup(View):
    def get(self, request):
        return render(request, 'portal/register.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone_number')
        email = postData.get('email')
        password1 = postData.get('password1')
        password2 = postData.get('password2')

        # Form validation
        error_message = self.validateCustomer(first_name, last_name, phone, email, password1, password2)

        if not error_message:
            # Save customer if no errors
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=make_password(password1)
            )
            customer.save()
            return redirect('login')  # Redirect to login after successful registration
        else:
            data = {
                'error': error_message,
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email
            }
            return render(request, 'portal/register.html', data)

    def validateCustomer(self, first_name, last_name, phone, email, password1, password2):
        error_message = None
        if not first_name:
            error_message = "Please enter your First Name!"
        elif len(first_name) < 3:
            error_message = 'First Name must be at least 3 characters long.'
        elif not last_name:
            error_message = 'Please enter your Last Name!'
        elif len(last_name) < 3:
            error_message = 'Last Name must be at least 3 characters long.'
        elif not phone:
            error_message = 'Please enter your Phone Number!'
        elif len(phone) < 10:
            error_message = 'Phone Number must be at least 10 digits long.'
        elif not email:
            error_message = 'Please enter your Email Address!'
        elif len(email) < 5:
            error_message = 'Email must be at least 5 characters long.'
        elif password1 != password2:
            error_message = 'Passwords do not match!'
        elif len(password1) < 5:
            error_message = 'Password must be at least 5 characters long.'
        elif Customer.objects.filter(email=email).exists():
            error_message = 'Email Address already registered.'
        return error_message


class Login(View):
    return_url = None

    def get(self, request):
        # Get the return URL if it exists
        Login.return_url = request.GET.get('return_url')
        return render(request, 'portal/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None

        # Authenticate user
        customer = authenticate(request, username=email, password=password)

        if customer:
            # Log the user in and set session variables
            login(request, customer)
            request.session['customer'] = customer.id
            request.session['customer_first_name'] = customer.first_name

            if Login.return_url:
                return HttpResponseRedirect(Login.return_url)
            else:
                Login.return_url = None
                return redirect('homepage')
        else:
            error_message = 'Invalid email or password!'

        return render(request, 'portal/login.html', {'error': error_message})


def logout(request): 
	request.session.clear() 
	return redirect('login') 



def index(request):
    products = Store.objects.filter(is_available=True)
    return render(request, 'portal/index.html', locals())


def shop(request):
    products = Store.objects.filter(is_available=True)
    return render(request, 'portal/shop.html',locals())

#=============================================================================================
@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    
    # Add a calculated field for each item's total price
    cart_with_totals = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'line_total': item.product.new_price * item.quantity
        }
        for item in cart_items
    ]
    
    # Calculate the grand total
    total_price = sum(item['line_total'] for item in cart_with_totals)
    
    return render(request, 'portal/cart.html', {
        'cart_items': cart_with_totals, 
        'total_price': total_price
    })

#===================================================================================================
@login_required
def base(request):
    # Get all cart items for the logged-in user
    base_items = Cart.objects.filter(user=request.user).select_related('product')
    
    # Prepare a list of items with their line totals
    base_with_totals = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'line_total': item.product.new_price * item.quantity
        }
        for item in base_items
    ]
    
    # Calculate the total price of all items in the cart
    total_price = sum(item['line_total'] for item in base_with_totals)
    
    # Calculate the total number of items in the cart
    total_items = sum(item['quantity'] for item in base_items)

    # Pass the data to the template
    return render(request, 'portal/base.html', {
        'base_items': base_with_totals,
        'total_price': total_price,
        'total_items': total_items
    })

#============================================================================================================
@login_required
def checkout_view(request):
    checkout_items = Cart.objects.filter(user=request.user).select_related('product')
    checkout_with_totals = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'line_total': item.product.new_price * item.quantity
        }
        for item in checkout_items
    ]
    total_price = sum(item['line_total'] for item in checkout_with_totals)
    
    # total_price = sum(item.product.new_price * item.quantity for item in checkout_items)
    return render(request, 'portal/checkout.html', {
        'checkout_items': checkout_with_totals, 
        'total_price': total_price
    })

#=====================================================================================================
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        print(f"Cart Item ID: {item.id}, Product: {item.product.name}, Quantity: {item.quantity}")
    total_price = sum(item.product.new_price * item.quantity for item in cart_items)
    return render(request, 'portal/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


#=====================================================================================================
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Store, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, "Product quantity updated in your cart.")
    else:
        pass
        messages.success(request, "Product added to your cart.")
    return redirect('cart')  # Replace 'cart' with the name of your cart page URL


#===================================================================================================
@login_required
def update_cart(request, item_id):
    try:
        # Fetch the cart item belonging to the logged-in user
        cart_item = Cart.objects.get(id=item_id, user=request.user)
    except Cart.DoesNotExist:
        # Handle the case where the cart item does not exist
        raise Http404("Cart item not found for this user.")
    
    if request.method == "POST":
        # Debugging log
        print(f"Updating cart item: {cart_item.id} for user: {request.user.email}")
        
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            print(f"Updated quantity to: {quantity}")
        else:
            cart_item.delete()  # Remove the item if quantity is set to 0
            print(f"Deleted cart item with id: {cart_item.id}")
    
    return redirect('cart')  # Redirect back to the cart page


#==============================================================================================
@login_required
def remove_from_cart(request, item_id):
    try:
        # Fetch the cart item belonging to the logged-in user
        cart_item = Cart.objects.get(id=item_id, user=request.user)
    except Cart.DoesNotExist:
        # Handle the case where the cart item does not exist
        raise Http404("Cart item not found for this user.")
    
    # Debugging log
    print(f"Removing cart item: {cart_item.id} for user: {request.user.email}")
    
    cart_item.delete()
    print(f"Cart item with id: {cart_item.id} has been removed.")
    
    return redirect('cart')



#====================================================================================================
@login_required
def initialize_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    paystack = Paystack()
    email = request.user.email
    amount = int(order.total_price * 100)  # Convert to kobo if using Paystack (e.g., NGN)
    
    response = paystack.initialize_payment(email, amount)

    if response['status']:
        payment = Payment.objects.create(
            order=order,
            user=request.user,
            amount=order.total_price,
            payment_method='Paystack',
            reference=response['data']['reference'],
            payment_status='Pending',
        )
        return redirect(response['data']['authorization_url'])
    else:
        return JsonResponse({'error': 'Payment initialization failed'}, status=400)


#==============================================================================================
@csrf_exempt
def verify_payment(request):
    reference = request.GET.get('reference')
    if not reference:
        return JsonResponse({'error': 'Missing payment reference'}, status=400)

    paystack = Paystack()
    response = paystack.verify_payment(reference)

    if response['status']:
        try:
            payment = Payment.objects.get(reference=reference)
        except Payment.DoesNotExist:
            return JsonResponse({'error': 'Payment record not found'}, status=404)

        payment.payment_status = 'Completed'
        payment.save()

        # Update order status
        payment.order.status = 'Completed'  # Update this based on your workflow
        payment.order.save()

        return JsonResponse({'message': 'Payment successful'}, status=200)
    else:
        return JsonResponse({'error': 'Payment verification failed'}, status=400)


#========================================================================================================
def process_payment(request):
    if request.method == "POST":
        # Get payment method from the form
        payment_method = request.POST.get("payment_method")
        
        # Simulate payment processing (replace with actual logic)
        if payment_method in ["bank_transfer", "check_payment", "cash_on_delivery"]:
            # Update payment status in session or database
            request.session['payment_completed'] = True
            return redirect('checkout')  # Redirect to the checkout or order confirmation page
        else:
            # Handle invalid payment method
            return render(request, 'checkout.html', {"error": "Invalid payment method"})
    
    # If not a POST request, redirect to the checkout page
    return redirect('checkout')


#================================================================================================================
@csrf_exempt
def process_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        reference = data.get('reference')
        # Verify payment
        url = f'https://api.paystack.co/transaction/verify/{reference}'
        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result['status'] and result['data']['status'] == 'success':
                # Save customer information
                customer, created = Customer.objects.get_or_create(
                    email=data.get('email'),
                    defaults={
                        'name': data.get('name'),
                        'phone': data.get('phone'),
                        'address': data.get('address'),
                    }
                )
                # Save order
                order = Order.objects.create(
                    customer=customer,
                    total_price=data.get('total_price'),
                    reference=reference
                )
                # Save order items
                for item in data.get('items', []):
                    OrderItem.objects.create(
                        order=order,
                        product_name=item['product']['name'],
                        quantity=item['quantity'],
                        price=item['line_total']
                    )
                
                return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'failed', 'message': 'Payment verification failed'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)



#==============================================================================================
def about(request):
    return render(request, 'portal/about.html', locals())


def shop_single(request):
    return render(request, 'portal/shop-single.html', locals())


# def register(request):
    
#     return render(request, 'portal/register.html', locals())


# def login(request):
#     return render(request, 'portal/login.html', locals())


def blog(request):
    return render(request, 'portal/blog.html', locals())


def contact(request):
    return render(request, 'portal/contact.html', locals())

