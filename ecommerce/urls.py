"""e-commerce URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^register/$', register_page, name='register'),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^admin/', admin.site.urls),
]

#different settings in production. in particular, static files will only be
#served when DEBUG == True
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #media files are whatever we upload ourselves
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)