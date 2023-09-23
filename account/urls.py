from django.urls import path
from .views import register, code, login_user, logout_user
app_name = 'account'
urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
    path('register/code/<str:first_name>/<str:last_name>/<str:phone_number>/<str:city>/<str:password1>/', code, name='code'),
    
]