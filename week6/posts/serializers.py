from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import Post,Comment

class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'
        #fields=['id','writer','content']

class PostListModelSerializer(PostModelSerializer):
    class Meta:
        class Meta(PostModelSerializer.Meta):
            fields = ['id','image','created_at','view_count','writer',]
            #exclude = ['content',]
            depth = 1

class PostCreateModelSerializer(PostModelSerializer):
    fields = ['image','content']

class PostDeleteModelSerializer(PostModelSerializer):
    pass

class CommentHyperlinkModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields='__all__'

class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        depth = 1