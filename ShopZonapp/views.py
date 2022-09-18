
from django.shortcuts import render ,HttpResponseRedirect
from django.views import View
from .models import Product,Customer
from .models import Cart
from .forms import CustomerRegistrationForm ,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login
from django.db.models import Q

# Create your views here.



class ProductView(View):
	def get(self, request):
		totalitem = 0
		topwears = Product.objects.filter(category='TW')
		bottomwears = Product.objects.filter(category='BW')
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'totalitem':totalitem})



class ProductDetailView(View):
	def get(self, request, pk):
		totalitem = 0
		product = Product.objects.get(pk=pk)
		print(product.id)
		item_already_in_cart=False
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
			item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
		return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})





class CustomerRegistrationView(View):
 def get(self, request):
  forms = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form':forms})
  
 def post(self, request):
  forms = CustomerRegistrationForm(request.POST)
  if forms.is_valid():
   messages.success(request, 'Congratulations!! Registered Successfully.')
   forms.save()
  return render(request, 'app/customerregistration.html', {'form':forms})



def user_login(request):
 if request.method =='POST':
   fn = AuthenticationForm(request=request, data=request.POST)
   if fn.is_valid():
    uname = fn.cleaned_data['username']
    upass = fn.cleaned_data['password']
       
    user= authenticate(username=uname, password=upass)  
    if user is not None:
      login(request,user)
      return HttpResponseRedirect('/profile/')

 else: 
    fn=AuthenticationForm()
 
    return render( request,'app/login.html',{'form':fn})



class profileView(View):
	def get(self, request):
		totalitem = 0
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		form = CustomerProfileForm()
		return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})
		
	def post(self, request):
		totalitem = 0
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		form = CustomerProfileForm(request.POST)
		if form.is_valid():
			usr = request.user
			name  = form.cleaned_data['name']
			locality = form.cleaned_data['locality']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
			reg.save()
			messages.success(request, 'Congratulations!! Profile Updated Successfully.')
		return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})

  
def address(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	add = Customer.objects.filter(user=request.user)
	return render(request, 'app/address.html', {'add':add, 'active':'btn-primary', 'totalitem':totalitem})












