from .views import OrganizationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)

urlpatterns = router.urls