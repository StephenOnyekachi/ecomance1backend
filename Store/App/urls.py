from django.urls import path
from . import views

urlpatterns = [
    path('deleteItem/<int:pk>/', views.DeleteItem, name='deleteItem'),
    path('deletecart/<int:pk>/', views.DeleteCart, name='deletecart'),
    path('viewItem/<int:pk>/', views.ViewItem, name='viewItem'),
    path('outofstock/<int:pk>/', views.Outofstock, name='outofstock'),
    path('remove/<int:pk>/', views.Remove, name='remove'),
    path('editImage/<int:pk>/', views.EditImage, name='editImage'),

    path('login/', views.UserLogin, name="login"),
    path('signup/', views.UserSignUp, name="signup"),
    path('logout/', views.UserLogout, name="logout"),

    path('', views.Index, name='index'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('newstatff/', views.NewStaff, name='newstaff'),
    path('users/', views.Userss, name='users'),

    path('additem/', views.Additem, name='additem'),
    path('pricelist/', views.Pricelist, name='pricelist'),
    path('sells/', views.Sells, name='sells'),
    path('report/<int:pk>/', views.Report, name='report'),
    path('message/', views.Message, name='message'),
    path('search', views.Search, name='search'),
    path('answer', views.Answer, name='answer'),

    path('store/', views.Store, name='store'),
    path('item/<int:pk>/', views.Item, name='item'),
    path('cart/', views.Cart, name='cart'),
    path('history/', views.History, name='history'),
]