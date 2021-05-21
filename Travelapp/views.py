from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import OrderForm,CustomerForm,PackageForm, CreateUserForm
from .filters import OrderFilter
from django.core.paginator import Paginator


# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect ('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Account was created for ' + user)

				return redirect('login')
		context = {'form' : form}
		return render(request,'pages/register.html',context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username=username,password=password)

			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'Username or Password is incorrect')

		context = {}

		return render(request,'pages/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect ('login')




@login_required(login_url = 'login')
def home(request):

	customers = Customer.objects.all()
	orders = Order.objects.all()
	total_orders = orders.count()
	orders_completed = orders.filter(status='Completed').count()
	orders_pending = orders.filter(status='Pending').count()
	orders_tripping = orders.filter(status='Tripping').count()

	paginator = Paginator(orders,4)
	page=request.GET.get('page')
	orders = paginator.get_page(page)


	context = {'customers' : customers,'orders' : orders,'total_orders' : total_orders , 'orders_completed' : orders_completed,'orders_pending' : orders_pending , 'orders_tripping' : orders_tripping }


	return render(request,'pages/dashboard.html',context)

@login_required(login_url = 'login')
def packeges(request):
	packeges= Packages.objects.all()
	return render(request,'pages/packeges.html',{'packeges' : packeges})

@login_required(login_url = 'login')
def customer(request,pk):

	customer= Customer.objects.get(id=pk)
	orders=customer.order_set.all()
	total_orders=orders.count()

	myFilter = OrderFilter(request.GET,queryset=orders)
	orders = myFilter.qs


	context = {'customer' : customer , 'orders' : orders , 'total_orders' : total_orders, 'myFilter' : myFilter }

	

	return render(request,'pages/customer.html',context)

@login_required(login_url = 'login')
def createcustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form' :form}
	return render(request,'pages/order_form2.html',context)	

@login_required(login_url = 'login')
def updatecustomer(request, pk):

	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'pages/order_form2.html', context)

@login_required(login_url = 'login')
def createpackage(request):
	form = PackageForm()
	if request.method == 'POST':
		form = PackageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form' :form}
	return render(request,'pages/order_form2.html',context)	


@login_required(login_url = 'login')
def createOrder(request,pk):
	OrderFormSet= inlineformset_factory(Customer, Order,fields=('packages' , 'status'),extra = 10)
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance= customer)
	#form  = OrderForm()
	if request.method == 'POST':
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST,instance = customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')
	context = {'form':formset}
	return render(request,'pages/order_form.html',context)


@login_required(login_url = 'login')
def updateOrder(request,pk):
	order=Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form' : form}
	return render(request,'pages/order_form.html',context)


@login_required(login_url = 'login')
def deleteOrder(request,pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')

	context = {'item' : order}
	return render(request,'pages/delete.html',context)
	
@login_required(login_url = 'login')
def gallery(request):
	return render(request,'pages/gallery.html')