from chef.views import ReceitasViewSet
from rest_framework.routers import DefaultRouter

app_name = 'chef' # Nome do módulo para referenciar URLs

router = DefaultRouter()
router.register(r'', ReceitasViewSet)
urlpatterns = router.urls
