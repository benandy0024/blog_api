from django.urls import path
from.views import CustomCreateUser
app_name='users'
urlpatterns = [

    path('register/', CustomCreateUser.as_view(),name='create'),

]