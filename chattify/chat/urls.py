# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index.html'),
    path('login/', views.login, name='login_url'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    # path('<str:room_name>/', views.index, name='index'),
]

# # from django.contrib.auth.views import LoginView,LogoutView

# urlpatterns = [
#     path('<str:room_name>/', views.index, name='index'),
#     path('login/', LoginView.as_view(), name='login_url'),
#     path('signup/', views.signup, name='signup'),
#     path('logout/', LogoutView.as_view(), name='logout'),
# ]