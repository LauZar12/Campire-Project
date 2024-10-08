# Miguel Angel Cock Cano
from django.urls import path
from .views import Home, Login, Logout, Signup, Games, GameView, Cart, Account

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
    path('games/', Games.as_view(), name='games'),
    path('game/', GameView.as_view(), name='game'),
    path('cart/', Cart.as_view(), name='cart'),
    path('account/', Account.as_view(), name='account'),
]
