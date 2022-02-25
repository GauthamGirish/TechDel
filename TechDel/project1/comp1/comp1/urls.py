"""comp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_details import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.user),
    path("login/",views.login1),
    path("welcome/",views.welcome),
    #path("index/",views.index),
    path("homepage1/",views.homepage),
    path("products/",views.product),
    #path("categories/",views.category),
    path("cart/",views.cart),
    path("add_to_cart/",views.add_to_cart),
    path("checkout/",views.check_out),
    path("place_order/",views.place_order),
    path("your_account/",views.update),
    path("your_orders/",views.your_orders),
    path("logout/",views.logout),
    path("update_cart/",views.update_cart),

]
#url(r'^users/(?P<user_id>\d+)/$', 'viewname', name='urlname'
#path("products/<int:pid>",views.product),