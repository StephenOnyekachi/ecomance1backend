import random
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from .models import *

# Create your views here.

@login_required
def DeleteItem(request, pk):
    item = Items.objects.get(id=pk)
    item.delete()
    messages.success(request, f'This Item "{item.out_number}" Is Deleted')
    return redirect('dashboard')

def DeleteCart(request, pk):
    cart = Carts.objects.get(id=pk)
    cart.delete()
    return redirect('cart')

def Outofstock(request, pk):
    item = Items.objects.get(id=pk)
    if item.available:
        item.available = False
        item.save()
        return redirect('dashboard')
    item.available = True
    item.save()
    return redirect('dashboard')

def Remove(request, pk):
    item = Items.objects.get(id=pk)
    if item.add_to_store:
        item.add_to_store = False
        item.save()
        return redirect('dashboard')
    item.add_to_store = True
    item.save()
    return redirect('dashboard')

def PriceList(request):
    priceList = Items.objects.all().order_by('-id')
    context = {
        'priceList' : priceList
    }
    return render(request, 'pricelist.html', context)

def EditImage(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == 'POST':
        picture = request.FILES.get('picture')
        item.picture = picture
        item.save()
        return redirect('dashboard')
    context = {
        'item': item,
    }
    return render(request, 'changeimage.html', context)

def ViewItem(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        out_number = request.POST['outnumber']
        catigory = request.POST['catigory']
        new_price = request.POST['new_price']
        old_price = request.POST['old_price']
        color = request.POST['color']
        total_quantity = request.POST['total']

        item.item_name = name
        item.out_number = out_number
        item.catigory = catigory
        item.price = new_price
        item.old_price = old_price
        item.color = color
        item.total_quantity = total_quantity
        item.save()
        messages.success(request, f'This Item "{out_number}" Was Edited')
        return redirect('dashboard')
    context = {
        'item': item,
    }
    return render(request, 'edititem.html', context)

def Message(request):
    message = Messages.objects.all().order_by('-id')
    context = {
        'message' : message,
    }
    return render(request, 'messages.html', context)

def UserLogout(request):
    logout(request)
    return redirect('index')

def UserSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        number = request.POST['number']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']  
        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                Users.objects.create_user(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    number = number,
                    password = password1,
                    gender = gender,
                    position = 'Customer',
                )
                messages.success(request, 'User was successfully')
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('login') 
    context = {
        # 'plans': plans,
    }
    return render(request, 'signup.html', context)

def NewStaff(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        number = request.POST['number']
        position = request.POST['position']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                Users.objects.create_user(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    number = number,
                    password = password1,
                    gender = gender,
                    position = position,
                    is_staff = True,
                    is_superuser = False
                )
                messages.success(request, 'User was successfully')
                return redirect('dashboard')
        else:
            messages.info(request, 'password not matching...')
            return redirect('newstatff') 
    context = {
        
    }
    return render(request, 'addStaff.html', context)

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('dashboard')
            elif user.position == 'Customer':
                login(request, user)
                return redirect('store')
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('login')
    context = {
        'message': messages,
    }
    return render(request, 'login.html', context)

def Dashboard(request):
    report = SellReports.objects.all().order_by('-id')
    users = Users.objects.all().filter(is_superuser=False)
    item = Items.objects.all().order_by('-id')
    context = {
        'item':item,
        'users':users,
        'report':report,
    }
    return render(request, 'dashboard.html', context)

def Userss(request):
    users = Users.objects.all().filter(is_superuser=False)
    context = {
        'users':users
    }
    return render(request, 'users.html', context)

def Index(request):
    cart = Carts.objects.all().order_by('-id')
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        message = request.POST['message']
        Messages.objects.create(
            sender_name = name,
            sender_number = number,
            message =  message,
        )
        return redirect('index')
    context = {
        'cart':cart,
    }
    return render(request, 'index.html', context)

def Additem(request):
    if request.method == 'POST':
        name = request.POST['name']
        out_number = request.POST['out_number']
        cattigory = request.POST['cattigory']
        color = request.POST['color']
        total = request.POST['total']
        old_price = request.POST['old_price']
        new_price = request.POST['new_price']
        picture = request.FILES.get('picture')
        Items.objects.create(
            item_name = name,
            out_number = out_number,
            catigory = cattigory,
            price = new_price,
            old_price = old_price,
            color = color,
            picture = picture,
            total_quantity = total,
        )
        messages.success(request, f'one item was added to the stock "{out_number}"')
        return redirect('dashboard')
    context = {
        
    }
    return render(request, 'newitem.html', context)

def Pricelist(request):
    price = Items.objects.all().order_by('-id')
    context = {
        'price':price,
    }
    return render(request, 'pricelist.html', context)

def Sells(request):
    item = Items.objects.all().order_by('-id')
    report = SellReports.objects.all().order_by('-id')
    context = {
        'item':item,
        'report':report,
    }
    return render(request, 'sells.html', context)

def Report(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['total']
        price = request.POST['new_price']

        item.total_quantity -= int(quantity)
        item.save()

        SellReports.objects.create(
            item_name = name,
            item_price = price,
            item_quantity = quantity,
        )
        return redirect('sells')

    context = {
        'item':item,
    }
    return render(request, 'report.html', context)

def Message(request):
    message = Messages.objects.all().order_by('-id')
    context = {
        'message':message,
    }
    return render(request, 'messages.html', context)

def Search(request):
    if request.method == 'GET':
        answer = request.GET['search']
        multiple = Q(Q(out_number = answer)|Q(item_name = answer)|Q(catigory = answer))
        search = Items.objects.filter(multiple)
        context = {
            'search':search,
        }
    return render(request, 'search.html', context)

def Answer(request):
    # if request.method == 'GET':
    #     answer = request.GET['search']
    #     multiple = Q(Q(item_name = answer) | Q(out_number = answer))
    #     item = Items.objects.filter(multiple)
    #     if answer is not multiple:
    #         pass
    context = {
        # 'item':item,
    }
    return render(request, 'answer.html', context)

def Store(request):
    store = Items.objects.all().order_by('-id')
    item = Items.objects.all().order_by('-id')
    cart = Carts.objects.all().order_by('-id')
    context = {
        'store':store,
        'item':item,
        'cart':cart,
    }
    return render(request, 'store.html', context)

def Item(request, pk):
    user = request.user
    item = Items.objects.get(id=pk)
    cart = Carts.objects.all().order_by('-id')
    if request.method == 'POST':
        catigory = request.POST['catigory']
        price = request.POST['price']
        item_name = request.POST['item']
        quantity = request.POST['quantity']
        out_number = request.POST['out_number']
        total_price = float(price) * int(quantity)

        Carts.objects.create(
            buyer_name = user,
            price = price,
            catigory = catigory,
            quantity = quantity,
            total_price = total_price,
            item_name = item_name,
            out_number = out_number,
        )
        return redirect('cart')
    context = {
        'item': item,
        'cart':cart,
    }
    return render(request, 'item.html', context)

def Cart(request):
    user = request.user
    cart = Carts.objects.all().order_by('-id')
    total_cart_price = 0
    cart_data = []
    for carts in cart:
        items_data = {
            'name' : carts.item_name,
            'price' : carts.price,
            'quantity' : carts.quantity,
            'total_price' : carts.total_price,
        }
        cart_data.append(items_data)
        total_cart_price += carts.price

    if request.method == 'POST':
        item = request.POST['name']
        price = request.POST['price']
        out_number = request.POST['out_number']
        catigory = request.POST['catigory']
        quantity = request.POST['quantity']
        Histories.objects.create(
            buyer_name = user,
            price = price,
            catigory = catigory,
            quantity = quantity,
            total_price = price,
            item_name = item,
            out_number = out_number,
        )
        cart.delete()
    context = {
        'cart':cart,
        'user':user,
        'total_cart_price':total_cart_price,
    }
    return render(request, 'cart.html', context)

def History(request):
    user = request.user
    history = Histories.objects.all().order_by('-id')
    context = {
        'history':history,
        'user':user,
    }
    return render(request, 'cart.html', context)