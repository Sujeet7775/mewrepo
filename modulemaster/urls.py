from django.urls import path
from .views import ModuleMasterCreateView

urlpatterns = [
    path('', ModuleMasterCreateView.as_view(), name='modulemaster-create'),
]