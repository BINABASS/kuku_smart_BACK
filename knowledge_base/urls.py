from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ArticleViewSet, CommentViewSet, FAQViewSet

router = DefaultRouter()
router.register(r'knowledge/categories', CategoryViewSet)
router.register(r'knowledge/articles', ArticleViewSet)
router.register(r'knowledge/comments', CommentViewSet)
router.register(r'knowledge/faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 