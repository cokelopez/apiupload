from rest_framework import serializers
from .models import PostSession, PostImage
from rest_framework import exceptions


class PostImageRetrieveSerializer(serializers.ModelSerializer):

    # This class present item from `list`, `create` actions or result items after uploaded

    class Meta:
        model = PostImage
        fields = '__all__'


class PostImageUpdateSerializer(serializers.Serializer):

    # This class for validate and save child items purpose

    name = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, )
    file = serializers.ImageField(
        required=True, allow_null=False, allow_empty_file=False, )

    def create(self, validated_data):
        session_name = validated_data.get('name')
        image_file = validated_data.get('file')

        if session_name and isinstance(session_name, str):
            # what does the '_' does here?
            session, _ = PostSession.objects.get_or_create(name=session_name, )
        else:
            session = None

        instance = PostImage.objects.create(
            name=session,
            file=image_file,
        )
        return self.update(
            instance=instance,
            validated_data=validated_data,
        )

    def update(self, instance, validated_data):
        instance.save()
        return instance


class PostUploadSerializer(serializers.Serializer):

    # This class for form upload with action `upload_images` from viewsets.py

    images = serializers.ListField(
        child=PostImageUpdateSerializer(
            required=True, allow_null=False, many=False, ),
        required=True,
        allow_null=False,
        allow_empty=False,
    )

    def validate(self, attrs):
        images_list = attrs.get('images')
        if not isinstance(images_list, list):
            raise exceptions.ValidationError(detail={
                'images': ['`images` field must be a list of dict object!', ],
            })

        return attrs

    def save_many(self):
        images_list = self.validated_data.get('images')
        post_image_instances = []

        for image_obj in images_list:
            try:
                post_image_serializer = PostImageSerializer(
                    context=self.context,
                    data=image_obj,
                    many=False,
                )
                post_image_serializer.is_valid(raise_exception=True, )
                post_image = post_image_serializer.save()
                post_image_instances.append(post_image)
                # I don´t know exactly what to use in the exception
            except:
                pass

        return post_image_instances

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
