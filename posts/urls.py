from django.contrib import admin
from django.urls import path, include
from .views import PostList, VoteCreate,PostRetrieveDestroy

urlpatterns = [
    path('api/posts', PostList.as_view()),
    path('api/posts/<int:pk>', PostRetrieveDestroy.as_view()),
    path('api/posts/<int:pk>/vote', VoteCreate.as_view()),
]