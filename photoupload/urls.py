

from .viewsets import PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('uploads', PostViewSet, base_name='uploads')

# upload_list_view = PostViewSet.as_view({
#     "get": "list",
#     "post": "create"

# })

# urlpatterns = [
#     #     path('uploads/', include('router.urls')),
#     path('uploads/', upload_list_view),
# ]
