from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, CategoryViewSet, UserViewSet
from knox import views as knox_views
from api.views import LoginAPI
from api.views import RegisterAPI

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('registro', RegisterAPI.as_view(), name='register'),
    path('login', LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),    

 ]