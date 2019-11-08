from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order
from .forms import OrderForm
from django.contrib import messages


def order_view(request):
    menu = Order.objects.all()
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Order Successfully')
            return redirect('home')
        else:
            form = OrderForm()

    context = {
        'form':form, 
        'menu': menu
        }
    return render(request, 'index.html', context)


