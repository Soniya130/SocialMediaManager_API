import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer

# --- CRUD API for Posts ---
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [JSONRenderer]

# --- Analytics endpoint ---
@api_view(['GET'])
def analytics_report(request):
    report = Post.objects.values('category').annotate(
        total_posts=Count('id')
    ).order_by('-total_posts')
    return Response(report)

# --- Fetch external posts from JSONPlaceholder ---
@api_view(['GET'])
def fetch_external_posts(request):
    """
    Fetch sample posts from JSONPlaceholder API.
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            data = response.json()
            # Optional: return only first 10 posts
            return Response(data[:10])
        else:
            return Response({"error": "Failed to fetch data"}, status=500)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
