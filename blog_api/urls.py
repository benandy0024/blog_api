from django.urls import path
from.views import PostViewCreate,PostViewDetail
app_name='blog_api'
urlpatterns = [

    path('create/', PostViewCreate.as_view(),name='create'),
    path('<int:pk>/', PostViewDetail.as_view(), name='detail'),

]