from django.contrib import admin
from . import models
from django.db.models import Sum
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'desc',
    #     # 'unit',
    ]
    # list_editable = ['unit']

    
@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
    ]
    
@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'cart',        
        'product',
        'unit',
        
    ]
    
@admin.register(models.Order)
class orderAdmin(admin.ModelAdmin):
    list_display = [
        'user',        
        'order_code',
        'status',
        'total__price',
        'order_list',
        'date'
    ]
    
    list_filter =[
        'date',
        'user',
        'status'
        
        
    ]
    list_editable = ['status']
    
    def order_list(self, obj):
        order_item = models.OrderItem.objects.filter(order=int(obj.id))
        total = ""
        for i in order_item:
            product = models.Product.objects.get(id=int(i.product.id))
            total += product.name +" : "+ str(i.unit)+","
        print(total)
        
        return total
    
    def total__price(self, obj):
        print(obj.id)
        order_item = models.OrderItem.objects.filter(order=int(obj.id))
        total = 0
        for i in order_item:
            product = models.Product.objects.get(id=int(i.product.id))
            total += (product.price * i.unit)
            
        
        return total
        

    
    
@admin.register(models.OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = [
        'product',
        'unit',
        'order',        
        
    ]

@admin.register(models.Table)
class TableAdmin(admin.ModelAdmin):
    list_display = [        
        'table_id',
        'status',
    ]

@admin.register(models.Reserve)
class CReserveAdmin(admin.ModelAdmin):
    list_display = [
        'user',        
        'table_id',
        
    ]
    
    
    
    