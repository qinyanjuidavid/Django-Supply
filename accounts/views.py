from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomerSignupForm,SupplierSignupForm,SupplierUserUpdateForm,SupplierProfileUpdateForm,CustomerUserUpdateForm,CustomerProfileUpdateForm
from accounts.models import User,Supplier,Customer
from accounts.decorators import supplier_required,customer_required


class SupplierSignupView(CreateView):
    model=User
    form_class=SupplierSignupForm
    template_name='accounts/supplierSignup.html'
    def get_context_data(self,**kwargs):
        kwargs['user_type']='supplier'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        if form.is_valid:
            user=form.save()
            login(self.request,user)
            return HttpResponseRedirect('/accounts/login/')
class CustomerSignupView(CreateView):
    model=User
    form_class=CustomerSignupForm
    template_name='accounts/customerSignup.html'
    def get_context_data(self,**kwargs):
        kwargs['user_type']='customer'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        if form.is_valid():
            user=form.save()
            login(self.request,user)
            return HttpResponseRedirect('/accounts/login/')
#==========================Profile======================================================
@login_required
@supplier_required
def SupplierProfileView(request):
    supProfile=Supplier.objects.get(user=request.user)
    user_form=SupplierUserUpdateForm(instance=request.user)
    form=SupplierProfileUpdateForm(instance=supProfile)
    if request.method=="POST":
        form=SupplierProfileUpdateForm(request.POST or None,request.FILES or None,instance=supProfile)
        user_form=SupplierUserUpdateForm(request.POST or None,request.FILES or None,instance=request.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
    context={
    'supProfile':supProfile,
    'form':form,
    'user_form':user_form
    }
    return render(request,'accounts/SupplierProfile.html',context)
@login_required
@customer_required
def CustomerProfileView(request):
    custProfile=Customer.objects.get(user=request.user)
    form=CustomerProfileUpdateForm(instance=custProfile)
    user_form=CustomerUserUpdateForm(instance=request.user)
    if request.method=="POST":
        form=CustomerProfileUpdateForm(request.POST or None,request.FILES or None,instance=custProfile)
        user_form=CustomerUserUpdateForm(request.POST or None,request.FILES or None,instance=request.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
    context={
    'custProfile':custProfile,
    'form':form,
    'user_form':user_form
    }
    return render(request,'accounts/CustomerProfile.html',context)
