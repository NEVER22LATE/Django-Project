from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreatedForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from shop.models import Product

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save()
            s = 0
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
                s += int(item["price"])
                stock = Product.objects.get(name=item['product']).stock - item["quantity"]
                Product.objects.filter(name=item['product']).update(stock=stock)
            if s == 0:
                messages.info(request, 'There is no item in the cart')
                return redirect("/cart")
            cart.clear()
        return render(request, "orders/order/created.html", {"order": order,"price": OrderItem})
    else:
        form = OrderCreatedForm()
    return render(request, "orders/order/create.html", {"form": form})
