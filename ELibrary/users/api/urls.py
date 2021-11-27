from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet


router = DefaultRouter()
router.register('api/users', UserViewSet, basename='users')

urlpatterns = router.urls