"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
admin.site.site_header = 'The Better Dynamics Portal'
admin.site.site_title = 'Admin Portal'
admin.site.index_title = 'Admin Portal'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('script/', include('rx.urls', namespace='script')),
    path('users/', include('users.urls')),
    path('', include('website.urls', namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),
    url(r'^chaining/', include('smart_selects.urls')),
]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
