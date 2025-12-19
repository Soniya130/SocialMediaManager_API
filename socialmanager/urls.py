from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse

from social_posts.views import PostViewSet, analytics_report, fetch_external_posts

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

def home(request):
    return HttpResponse("""
        <h2>✅ SocialMediaManager is running on Railway!</h2>
        <p>Admin panel: <a href="/admin/">/admin/</a></p>
        <p>API endpoints: <a href="/api/">/api/</a></p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/report/', analytics_report),
    path('api/external-posts/', fetch_external_posts),
    path('', home),
]
