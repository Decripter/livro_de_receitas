from rest_framework import urlpatterns
from rest_framework import routers
from receitas.views import ReceitasViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ReceitasViewSet)
urlpatterns = router.urls