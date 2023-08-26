from customers.models import Customer
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View


class CopyCustomer(View):
    '''Duplicate existed customer'''

    def get(self, request, pk, *args, **kwargs):
        copy = get_object_or_404(Customer, pk=pk)
        copy.pk = None
        copy.customer_name = f"Copy of {copy.customer_name}"
        context = {
            "customer_name": copy.customer_name,
            "customer_email": copy.customer_email,
            "mobile_no": copy.mobile_no,
            "customer_address": copy.customer_address
        }
        return render(request,  'customers/add_customer.html', context=context)

    def post(self, request, *args, **kwargs):
        ''' Respond to POST request '''
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        mobile_no = request.POST.get('mobile_no')
        customer_address = request.POST.get('customer_address')
        balance = request.POST.get('balance')
        customer = Customer(
            user=request.user,
            customer_name=customer_name,
            customer_email=customer_email,
            mobile_no=mobile_no,
            customer_address=customer_address,
            balance=balance
        )
        customer.save()
        '''Provide a redirect on GET request.'''
        return redirect('customer_list')
