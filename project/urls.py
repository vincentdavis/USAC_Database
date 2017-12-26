from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, \
    verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  re_path(r'^$', RedirectView.as_view(url='/api/v1/')),
  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path('api/v1/', include('apps.usac.urls')),
  path('token/auth/', obtain_jwt_token),
  path('token/refresh/', refresh_jwt_token),
  path('token/verify/', verify_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
