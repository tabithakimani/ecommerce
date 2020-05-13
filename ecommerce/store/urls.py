from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('home/', views.store, name="store"),
	path('register/', views.sign_up, name='sign_up'),
	path('login/', views.sign_in, name='sign_in'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('dashboard', views.user_dashboard, name='user_dashboard'),
	path('update_item/', views.updateItem, name="update_item"),

]