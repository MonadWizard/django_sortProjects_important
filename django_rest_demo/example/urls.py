from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# আমরা url path manually দিব না। rest-framework থেকে নিব। 
router = DefaultRouter()
router.register('industries', views.IndustryView)
router.register('companies', views.CompanyView)
router.register('persions', views.PersonView)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
