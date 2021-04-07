from django.urls import path
from.views import PostViewCreate,PostViewDetail,PostListView
app_name='blog_api'
urlpatterns = [

    path('create/', PostViewCreate.as_view(),name='create'),
path('list/',PostListView.as_view(),name='create'),
    path('list/<int:pk>/', PostViewDetail.as_view(), name='detail'),

]