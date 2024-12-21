from rest_framework import routers

from api.views import AccountPage, HousePage, HousesPage, HomePage

router = routers.DefaultRouter()

router.register(r'account', AccountPage, basename='account')
router.register(r'house', HousePage, basename='house')
router.register(r'houses', HousesPage, basename='houses')
router.register(r'home', HomePage, basename='home')
