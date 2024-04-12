from django.contrib import admin
from .models import Supplier, Buyer, Product, Order, Delivery
from octorest import OctoRest

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_date']
    search_fields = ['name', 'address']

class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_date']
    search_fields = ['name', 'address']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sortno', 'created_date']
    search_fields = ['name']
    list_filter = ['created_date']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'product', 'design', 'color', 'buyer', 'status', 'created_date']
    search_fields = ['product__name', 'design', 'color']
    list_filter = ['status', 'created_date']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change and obj.status == 'approved':
            self.print_order(obj)

    def print_order(self, order):
        octo_url = "http://octopi.local/"
        octo_apikey = "3342ACFDFCF0460AA0BF4E148A125F3B"
        client = OctoRest(url=octo_url, apikey=octo_apikey)
        file_path = "red.gcode" # print the red, add logic as design improves
        print("Initiating print job...")

        printer_status = client.job_info()
        print(printer_status)
        try:
            client.select(file_path, print=True)
            client.start()
            print("Print job started successfully!")
        except Exception as e:
            print("Error starting print job:", e)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'courier_name', 'created_date']
    search_fields = ['order__id', 'courier_name']
    list_filter = ['created_date']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery, DeliveryAdmin)
