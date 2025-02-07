from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect  # Correcte import van redirect
from django.contrib.auth.views import LogoutView
from DjangoProject2.views import CustomLoginView, user_dashboard, realtime_energie_view

urlpatterns = [
    path('', lambda request: redirect('login', permanent=False)),  # Gebruik redirect
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('realtime-energie/', realtime_energie_view, name='realtime-energie'),
    path('admin/login/', CustomLoginView.as_view(template_name='admin_login.html'), name='admin_login'),
    path('admin/', admin.site.urls),
]
