from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_cart, cart, delete_cart, promotion, products, login_required_error, contact, remove_from_cart
from accounts.views import signup, logout_user, login_user

from SHOP import settings

urlpatterns = [
                  path('', index, name='index'),
                  path('admin/', admin.site.urls),
                  path('promotion/', promotion, name='promotion'),
                  path('products/', products, name='products'),
                  path('signup/', signup, name='signup'),
                  path('login/', login_user, name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('cart/', cart, name='cart'),
                  path('contact/', contact, name='contact'),
                  path('cart/delete', delete_cart, name='delete-cart'),
                  path('product/<str:slug>', product_detail, name="product"),
                  path('product/<str:slug>/add-to-cart', add_to_cart, name="add-to-cart"),
                  path('cart/remove/<int:order_id>/', remove_from_cart, name='remove_from_cart'),
                  path('login-required-error/', login_required_error, name='login_required_error'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
