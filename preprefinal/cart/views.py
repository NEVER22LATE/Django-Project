from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
import sqlite3
from django.contrib import messages 
from django.http import HttpResponseRedirect



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    #print(Product.objects.all().values_list('id', flat = True))
    product = get_object_or_404(Product, id=product_id)
    #print("1234......................")
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        if cd["quantity"] > 0 and cd["quantity"] <= Product.objects.get(id=product_id).stock:
            cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
        else :
            messages.info(request, 'quantity exceeded')
            return redirect("/cart")
    return redirect("cart:cart_detail")

def cart_remove(request, product_id):
    cart = Cart(request)
    #print("12344......................")
    #print(Product.objects.all().values_list('id', flat = True))
    product = get_object_or_404(Product, id=product_id)
    #print(product)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    #print("1234555......................")
    #print(Product.objects.all().values_list('id', flat = True))
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "update": True}
        )
    return render(request, "cart/detail.html", {"cart": cart})

