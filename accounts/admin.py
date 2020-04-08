from django.contrib import admin
from accounts.models import User,Supplier,Customer,Categories,Counties
from leaflet.admin import LeafletGeoAdmin

admin.site.register(User)
class SupplierAdmin(LeafletGeoAdmin):
    list_display=('user','location')
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Customer)
admin.site.register(Categories)
class CountiesAdmin(LeafletGeoAdmin):
    list_display=("name",)
admin.site.register(Counties,CountiesAdmin)
