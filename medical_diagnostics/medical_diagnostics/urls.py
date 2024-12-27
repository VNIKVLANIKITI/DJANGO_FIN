from django.urls import include
from django.contrib import admin
from django.urls import path
from medical_diagnostics.views import get_general_page, about, contacts

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get_general_page, name='home'),
    path("about/", about, name='about'),
    path("contacts/", contacts, name='contacts'),
    path('users/', include('users.urls', namespace='users')),
    path('medical/', include('medical.urls', namespace='medical')),
]
