# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# # Create your views here.
# def coffee_list(request):
#     return render(request,'coffee_site/coffee_list.html', {})


from django.shortcuts import render
from django.http import HttpResponse
from coffee_site.models import Customer,Menu,Order,Records

from .forms import FormName

# Create your views here.
def coffee_list(request):
    customer_list = Customer.objects.order_by('mail')
    mail_dict = {'customers':customer_list}
    return render(request,'coffee_site/coffee_list.html', context = mail_dict)


def form(request):

        context = {}

        form = FormName(request.POST or None, request.FILES or None)

        if form.is_valid() :
            form.save()

        context['form'] = form

        return render(request, 'coffee_site/form.html', context)

def new_page(request):
    return render(request,'coffee_site/new_page.html')
