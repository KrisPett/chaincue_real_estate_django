from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'home', views.HomePage, basename='home')
router.register(r'account', views.AccountPage, basename='account')
router.register(r'house', views.HousePage, basename='house')
router.register(r'houses', views.HousesPage, basename='houses')
