from django.urls import path
from .views import indexfunc, signupfunc

urlpatterns = [
    path('index/', indexfunc),
    path('signup/', signupfunc)
]