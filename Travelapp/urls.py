from django.urls import path
from . import views


urlpatterns=[

	path('register/',views.registerPage,name="register"),
	path('login/',views.loginPage,name='login'),
	path('logout/',views.logoutUser,name="logout"),

	path('',views.home,name="home"),
	path('packages/',views.packeges,name='packages'),
	path('customer/<str:pk>/',views.customer,name="customer"),

	path('create_customer/',views.createcustomer,name='create_customer'),
	path('update_customer/<str:pk>/',views.updatecustomer,name='update_customer'),

	path('create_package',views.createpackage,name='create_package'),


	path('create_order/<str:pk>/', views.createOrder,name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder,name="delete_order"),

	path('gallery/',views.gallery,name='gallery')
]