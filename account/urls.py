

from django.urls import path
import account.views

urlpatterns = [
    path('signup/', account.views.signup, name='注册页面'),
    path('login/', account.views.login, name='登录页面'),
    path('logout/', account.views.logout, name='退出页面'),

]