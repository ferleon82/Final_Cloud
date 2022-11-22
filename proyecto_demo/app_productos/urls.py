from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/v1.0/productos',ProductoViewSet)

urlpatterns = router.urls

