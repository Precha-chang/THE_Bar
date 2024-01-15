from django.shortcuts import render ,redirect
from django. contrib. auth.models import User
from . import models

from django.db.models import F


# Create your views here.
def homepage (request):
    product = models.Product.objects.all()
    beer = models.Category.objects.get(name ='เบียร์')
    product_beer = models.Product.objects.filter(category=beer)
    spirits = models.Category.objects.get(name ='เหล้า')
    product_spirits = models.Product.objects.filter(category=spirits)
    snacks = models.Category.objects.get(name ='อาหาร')
    product_snacks = models.Product.objects.filter(category=snacks)
    mixer = models.Category.objects.get(name ='มิกซ์')
    product_mixer = models.Product.objects.filter(category=mixer)
    return render (request,"index.html", {
        "products":product,
        "beer":product_beer,
        "spirits":product_spirits,
        "snacks":product_snacks,
        "snacks":product_mixer,
    })


def about (request):
    return render (request,"about.html")

def shop (request):
    product = models.Product.objects.all()
    return render (request,"shop.html", {
        "products":product,
    })


def cart (request):
    user = User.objects.get(username=request.user.username)
    cart = models.Cart.objects.get(user=user)
    data = {}
    cartiten = models.CartItem.objects.filter(cart=cart)
    data['cartitem'] = cartiten
    
    return render (request,"cart.html", data)



def addCart(request, id):
    user = User.objects.get(username=request.user.username)
    
    
    product = models.Product.objects.get(id=id)
    cart = models.Cart.objects.get(user=user)
    
    if (models.CartItem.objects.filter(cart=cart, product=product)).count() != 0:
        
        models.CartItem.objects.filter(cart=cart, product=product).update(unit=F("unit")+1)
        
    else :
        models.CartItem.objects.create(
            cart=cart,
            product=product,
            unit=1   
        )
    

    return redirect('shop')

def login (request):
    return render (request,"login.html")


def regis (request):
    return render (request,"regis.html")