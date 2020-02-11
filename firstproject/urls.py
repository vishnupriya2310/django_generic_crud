"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings 
from django.conf.urls import url
from helloworld.views import ContactList, ContactDetail, ContactCreate, ContactUpdate, ContactDelete

urlpatterns = [
    url('admin/', admin.site.urls),
     url(r'^$', ContactList.as_view()),
    # url('contacts/', ContactList.as_view()),
    url('contacts', ContactList.as_view(), name='contact_list'),
    # url('contact/<int:pk>', ContactDetail.as_view(), name='contact_detail'),
    url(r'^contact/(?P<pk>\d+)$', ContactDetail.as_view(), name='contact_detail'),
    url('create', ContactCreate.as_view(), name='contact_create'),
    url(r'^update/(?P<pk>\d+)$', ContactUpdate.as_view(), name='contact_update'),
    url(r'^delete/(?P<pk>\d+)$', ContactDelete.as_view(), name='contact_delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG: # new
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
