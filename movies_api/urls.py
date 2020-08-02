from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework.renderers import JSONOpenAPIRenderer

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'movies', views.MovieViewSet)

schema_view = get_schema_view(title="Movies API", renderer_classes=[JSONOpenAPIRenderer])

from django.views.generic import TemplateView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^schema$', schema_view, name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
