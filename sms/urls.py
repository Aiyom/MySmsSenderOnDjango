from django.urls import path
from django.contrib.auth import views as authViews
from sms import views

urlpatterns = [
    path('', authViews.LoginView.as_view(template_name="pages/login.html"), name='auth'),
    path('logout', authViews.LogoutView.as_view(), name='exit'),
    path('students', views.index, name='students'),
    path('send', views.sendSms, name='send'),
    path('listkurs', views.listKurs, name='listkurs'),
]