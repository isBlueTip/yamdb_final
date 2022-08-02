from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    re_path(r'^admin/?$', admin.site.urls),
    path('api/', include('api.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="YamDB API",
        default_version='v1',
        description="Документация для API проекта YamDB",
        contact=openapi.Contact(email="rhinorofl@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^redoc/?$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
