from .serializer import PostUploadSerializer, PostImageRetrieveSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from .models import PostImage


class PostViewSet(viewsets.GenericViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser, ]
    serializer_class = PostImageRetrieveSerializer
    queryset = PostImage.objects.all()

    @action(methods=['POST', ], detail=False, serializer_class=PostUploadSerializer, )
    def upload_images(self, request, *args, **kwargs):
        upload_serializer = PostUploadSerializer(
            context={'request': request, },
            data=request.data,
            many=False,
        )
        upload_serializer.is_valid(raise_exception=True, )
        post_image_instances = upload_serializer.save_many()

        serializer = self.get_serializer(
            post_image_instances,
            many=True,
        )
        return response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
