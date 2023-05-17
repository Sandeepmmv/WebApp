from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    # path('user/',views.user_view,name='user'),
    path('upload/',views.upload_view,name='upload'),
    path('search/',views.search_view,name='search/'),
    path('follow/',views.follow_view,name='follow'),
    path('profile/<str:pk>/',views.profile_view,name='profile'),
    path('post_like/',views.post_like_view,name='post_like'),
    path('account_setting/',views.AccountSetting_view,name='account_setting'),
    path('signup/',views.SignUp_view,name='signup'),
    path('signin/',views.SignIn_view,name='signin'),
    path('signout/',views.SignOut_view,name='signout'),

]