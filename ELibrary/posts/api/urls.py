from rest_framework.routers import DefaultRouter
from posts.api.views import PostViewSet, CategoryViewSet


router = DefaultRouter()
router.register('api/posts', PostViewSet, basename='posts')
router.register('api/categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls