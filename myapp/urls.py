from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ArticleViewSet
from .views import user_permissions
# from .views import assign_permissions
from .views import assign_model_permissions


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my-permissions/', user_permissions),  # <- Add this line
    # path('assign-permissions/', assign_permissions),
    path('assign-model-permissions/', assign_model_permissions),


]



