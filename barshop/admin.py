from django.contrib import admin
from . import models

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
        'unit',
    ]
    
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
    ]
    
@admin.register(models.OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = [
        'product',
        'unit',
        'order'
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
    
    
    
    