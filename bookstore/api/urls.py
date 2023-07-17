from django.urls import path
from .views import Home, BookRUD

from drf_yasg.views import get_schema_view as gsv
from drf_yasg import openapi
from rest_framework import permissions


schema_view = gsv( # new
openapi.Info(
title="Blog API",
default_version="v1",
description="API endpoints for bookstore",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="contact@blogapi.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', Home.as_view(), name='home-api' ),
    path('book/<uuid:pk>/', BookRUD.as_view(), name = "book-rud"),



    # Endpoints as a result of drf_yasg
    path('swagger/', schema_view.with_ui( # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]