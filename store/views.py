from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from store.models import Product, Cart, Order, Promotion


def index(request):
    return render(request, 'store/index.html')


def products(request):
    products = Product.objects.all
    return render(request, 'store/products.html', context={"products": products})


def promotion(request):
    promotions = Promotion.objects.all
    return render(request, 'store/promotion.html', context={"promotions": promotions})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    products = Product.objects.all
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return render(request, 'store/products.html', context={"products": products})


@login_required
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # L'utilisateur n'a pas de cart, le rediriger vers une autre page
        return render(request, 'store/empty_cart.html')

    orders = cart.orders.all().annotate(total=F('quantity') * F('product__price'))
    final_price = orders.aggregate(final_price=Sum('total'))['final_price'] or 0
    items = orders.aggregate(items=Sum('quantity'))['items'] or 0
    final_taxed = final_price + 26000

    context = {
        'orders': orders,
        'final_price': final_price,
        'final_taxed': final_taxed,
        'items': items,
    }

    return render(request, 'store/cart.html', context=context)


def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    return render(request, 'store/cart.html')

def login_required_error(request):
    return render(request, 'store/login_required_error.html')
def contact(request):
    return render(request, 'store/contact.html')
