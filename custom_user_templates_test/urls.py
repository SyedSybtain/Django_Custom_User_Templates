from django.contrib import admin
from django.urls import path
from .views import home,register
from django.contrib.auth.views import (LoginView,
    PasswordResetView,PasswordResetDoneView,
    PasswordResetConfirmView,PasswordResetCompleteView,
    PasswordChangeView,PasswordChangeDoneView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('login/', LoginView.as_view(next_page = 'home'), name = 'login'),
    path('register/', register ,name='register'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name= 'password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(),name= 'password_reset_complete'),
    path('password_change/', PasswordChangeView.as_view(), name= 'password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),name= 'password_change_done'),
]
