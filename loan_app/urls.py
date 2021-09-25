from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.root,name='root'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('loan',views.loan,name='loan'),
    path('amount',views.amount,name='amount'),
    path('logout',views.logout,name='logout'),
]
