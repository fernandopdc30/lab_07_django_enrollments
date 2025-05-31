from rest_framework.routers import DefaultRouter
from MyWebApps.api.views import ProductoViewSet 

router = DefaultRouter()
router.register('productos', ProductoViewSet, basename='producto')
urlpatterns = router.urls