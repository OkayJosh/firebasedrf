from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, OtherFinancialsViewSet


router = DefaultRouter()
router.register('income', IncomeViewSet, basename='acc-income')
router.register('expense', ExpenseViewSet, basename='acc-expense')
router.register('others', OtherFinancialsViewSet, basename='acc-other')

urlpatterns = [
    
] + router.urls