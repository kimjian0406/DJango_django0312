# users/urls.py
from django.urls import path
from . import cb_views

urlpatterns = [
    path('signup/', cb_views.SignupView.as_view(), name='signup'),
    path('login/', cb_views.CustomLoginView.as_view(), name='login'),
    path('logout/', cb_views.LogoutView.as_view(), name='logout'),
    path('verify/<str:token>/', cb_views.verify_email, name='verify_email'),
]

# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # LogoutView는 django.contrib.auth.views에서 가져옵니다.
    path('verify/<signed_data>/', views.verify_email, name='verify'),
    path('signup_done/', views.SignupDoneView.as_view(), name='signup_done'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
]

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

