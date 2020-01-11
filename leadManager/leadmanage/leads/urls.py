from rest_framework import routers
from .views import LeadViewSet

router = routers.DefaultRouter()
router.register('api/lead',LeadViewSet,'leads')

urlpatterns = router.urls