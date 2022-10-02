from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
# router.register('product-on-stock', ProductPositionViewSet)

urlpatterns = router.urls
