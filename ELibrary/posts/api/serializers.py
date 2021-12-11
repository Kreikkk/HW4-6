from posts.models import Post, Category
from rest_framework import serializers

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from posts.documents import *


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['pk', 'title', 'body', 'author', 'pub_datetime', 'category', 'author_username']

    def get_author_username(self, post):
        return post.author.username

    def validate_author(self, instance):
        if '_' in instance.username:
            raise serializers.ValidationError(f'Author username shouldnt contain _')

        return instance

    def validate(self, data):
        for key in ('title', 'body'):
            if 'hello' in data[key].lower():
                raise serializers.ValidationError(f'{key} field contains hello, I dont like it')

        return data

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']

    
class PostsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Post
        document = PostsDocument

        fields = ('title', 'body')

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}