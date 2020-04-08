from django.urls import path
from business import views
app_name="business"

urlpatterns=[
path('',views.WelcomeView,name="welcome"),
path('home/',views.HomeView,name='home'),
path('product/<id>/details/',views.ProductView,name="details"),
path('update/product/<id>/',views.UpdateView,name='update'),
path('delete/product/<id>/',views.ProductDelete,name='delete'),
path('addProduct/',views.AddProductView,name="addProduct"),
path('supplier/<id>/details/',views.SupplierDetailsView,name="supplierdetails"),
path('counties/',views.CountyView,name='county'),
path('supply/',views.SupplierData,name="supply"),
path('supplier/details/<id>/',views.SpecificSupplier,name="supplierlocation")
]
