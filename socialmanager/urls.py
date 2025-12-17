from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from social_posts.views import PostViewSet, analytics_report, fetch_external_posts

# API router
router = DefaultRouter()
router.register(r'posts', PostViewSet)

# Homepage view for root URL
def home(request):
    return HttpResponse(
        """
        <h2>✅ SocialMediaManager is running on Railway!</h2>
        <p>Admin panel: <a href="/admin/">/admin/</a></p>
        <p>API endpoints: <a href="/api/">/api/</a></p>
        <p>Your app link: <a href="https://web-production-1504c.up.railway.app/" target="_blank">https://web-production-1504c.up.railway.app/</a></p>
        """
    )

urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin
    path('api/', include(router.urls)),        # API endpoints
    path('api/report/', analytics_report),     # Analytics report
    path('api/external-posts/', fetch_external_posts),  # Fetch external posts
    path('', home),                            # Root URL
]
