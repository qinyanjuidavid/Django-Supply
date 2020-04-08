from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.decorators import supplier_required,customer_required
from django.contrib.auth.decorators import login_required
from business.models import Products
from business.forms import UpdateForm
from accounts.models import Supplier,Counties
from django.core.serializers import serialize

def WelcomeView(request):
    context={

    }
    return render(request,'business/welcome.html',context)
@login_required
def HomeView(request):
    product=Products.objects.filter(user=request.user)
    supplier=Supplier.objects.all()
    context={
    'product':product,
    'supplier':supplier
    }
    return render(request,'business/home.html',context)
@login_required
@supplier_required
def ProductView(request,id):
    productdetails=Products.objects.get(user=request.user,id=id)
    context={
    'productdetails':productdetails
    }
    return render(request,'business/details.html',context)
@login_required
@supplier_required
def UpdateView(request,id):
    productUpdate=Products.objects.get(user=request.user,id=id)
    form=UpdateForm(instance=productUpdate)
    if request.method=="POST":
        form=UpdateForm(request.POST or None,request.FILES or None, instance=productUpdate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/product/{id}/details/')
    context={
    'form':form
    }
    return render(request,'business/update.html',context)
@login_required
@supplier_required
def ProductDelete(request,id):
    deleteProduct=Products.objects.get(user=request.user,id=id)
    deleteProduct.delete()
    return HttpResponseRedirect('/home/')
@login_required
@supplier_required
def AddProductView(request):
    if request.method=="POST":
        form=UpdateForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            product=form.save(commit=False)
            product.user=request.user
            product.save()
            return HttpResponseRedirect('/home/')
    else:
        form=UpdateForm()
    context={
    'form':form
    }
    return render(request,'business/addProduct.html',context)
def SupplierDetailsView(request,id):
    supObj=Supplier.objects.get(id=id)
    context={
    'supObj':supObj
    }

    return render(request,'business/supplierdetails.html',context)


#========================================================================
def CountyView(request):
    counties=serialize('geojson',Counties.objects.all())
    return HttpResponse(counties,content_type='json')
def SupplierData(request):
    supply=serialize('geojson',Supplier.objects.all())
    return HttpResponse(supply,content_type='json')
def SpecificSupplier(request,id):
    print(id)
    sup=serialize('geojson',Supplier.objects.filter(id=id))
    return HttpResponse(sup,content_type="json")
