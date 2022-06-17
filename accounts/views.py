from django.shortcuts import redirect, render
from .models import Order, Customer
from . forms import OrderForm, UserRegisterForm
from django.forms import inlineformset_factory
from . filters import OrderFilter
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders= myFilter.qs
    context ={'orders':orders, 'customers':customers,'myFilter':myFilter}
   
    
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login')
def customer(request):
    return render(request,'accounts/customer.html')
@login_required(login_url='login')
def products(request):
    return render(request,'accounts/products.html')
@login_required(login_url='login')
def order(request,pk):
    order=Order.objects.get(pk=pk)
    context={'order':order}
    return render(request,'accounts/order.html',context)
@login_required(login_url='login')
def create_order(request):
    
    if request.method=='POST':
        form =OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=OrderForm()
    context ={'form':form}

    return render (request, 'accounts/createorder.html',context)
@login_required(login_url='login')
def update_order(request,pk):
    order=Order.objects.get(pk=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form =OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=OrderForm(instance=order)
    context ={'form':form}

    return render (request, 'accounts/update_order.html',context)
@login_required(login_url='login')
def delete_order(request,pk):
    order=Order.objects.get(pk=pk)
    context={'order':order}

    if request.method=='POST':
        order.delete()
        return redirect('home')
        

    return render(request,'accounts/delete_order.html',context)

@login_required(login_url='login')
def customer_create_order(request,pk):
    customer=Customer.objects.get(pk=pk)
    #form=OrderForm(initial={'customer':customer})
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'),extra=10)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method=='POST':
        formset =OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
   
   
    context={'customer':customer,'formset':formset}
    return render(request,'accounts/customer_create_order.html',context)
@login_required(login_url='login')
def register(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully')  
        return redirect('home')
  
    else:  
        form = UserCreationForm()  
    context = {  
            'form':form  
        }  
    return render(request, 'accounts/register.html', context)  
@login_required(login_url='login')
def loginpage(request):
    return render(request,'accounts/login.html')

