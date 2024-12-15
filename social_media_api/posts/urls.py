from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# Initialize the router for post and comment viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# Define additional URL patterns for the feed
urlpatterns = [
    path('feed/', FeedView.as_view(), name='user_feed'),
]

# Combine the router's URLs with the manually defined urlpatterns
urlpatterns += router.urls