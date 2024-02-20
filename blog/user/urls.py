from django.contrib import admin
from django.urls import path
from user  import views

app_name = "user"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('profile/<int:id>',views.profile,name="profile"),
    path('profiledelte/<int:id>',views.ProfileDelete,name="profiledelete")
    

]