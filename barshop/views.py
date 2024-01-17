from django.shortcuts import render ,redirect
from django. contrib. auth.models import User
from . import models
from django.db.models import F

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import random
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
    data['cart'] = cart
    
    if models.Reserve.objects.filter(user=user).count()!=0:
        data['table']= models.Reserve.objects.get(user=user)
    
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

def loginPage (request):
    return render (request,"login.html")


def regis (request):
    return render (request,"regis.html")

#สมัครสมาชิก#

def  registerMember(request):
    first_name = request.POST.get('f_name')
    last_name = request.POST.get('i_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try :

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        if (user):
            models.Cart.objects.create(user=user)
            
            return redirect("login")
    
    except IOError as err:
        return redirect("regis")
    
    #login
    
def loginMember(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try :

        user = User.objects.create_user(
            username = username,
            password = password,
        )

        if (user):
            customer = models.Customer.objects.create(
                user=user,
            )
            if customer:
                return redirect("home_page")
    
    except :
        pass
    return render("regis")


def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)

    user = authenticate(
        username=username,
        password=password
    )

    if user:
        login(request, user)
        return redirect("home")
    else:
        
        return redirect("login")


def HomePage (request): 
    user_username = request.user.username
    user = User.objects.get(username=user_username)
    customer = models.Customer.objects.get(user=user)

    transaction = models.Transaction.objects.filter(customer=customer).order_by('-id')

   
    return render (request, 'index.html',
                   {
                       "balance":customer.balance,
                        "number_phone":customer.phone_number,
                       "trans":transaction,
                       "trans_count":transaction.count()
                   })
    
    
    
def logoutP (request):
    logout(request)
    return redirect('login')    

def reserve (request):
    table = models.Table.objects.filter(status="Wait")
    return render (request,"reserve.html" ,{
        "table":table,
    })

def Reserve (request, id):
    user = User.objects.get(username=request.user.username)
    table = models.Table.objects.get(id=id)
    models.Reserve.objects.create(user=user,table_id=table)
    data={}
    models.Table.objects.filter(id=table.id).update(status="Process")
     
    return redirect('home')    

def order_code():
    code = "{0:09}".format(random.randint(100000000,999999999))
    if models.Order.objects.filter(order_code=code).count() != 0 :
        order_code()
    return code
     

def Order (request, id):
    user = User.objects.get(username=request.user.username)
    cart = models.Cart.objects.get(id=int(id))
    cartitem = models.CartItem.objects.filter(cart=cart)
    
    order = models.Order.objects.create(
        user=user,
        order_code=order_code(),
        status="Wait",
    )
    for item in cartitem:
        print(item)
        product = models.Product.objects.get(id=int(item.product.id))
        unit = item.unit 
        
        models.OrderItem.objects.create(
            order=order,
            product=product,
            unit=unit
            
        )
        models.CartItem.objects.filter(cart=cart,product=product).delete()
    
    
    
    
    
    return redirect('cart')
    
    
    



