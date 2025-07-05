
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primer_app/',include('primer_app.urls')),
    
]
