from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from social_posts.views import PostViewSet, analytics_report
from social_posts.views import fetch_external_posts

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/report/', analytics_report),
    path('api/external-posts/', fetch_external_posts),

]

