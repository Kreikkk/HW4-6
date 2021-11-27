from rest_framework.utils import model_meta
from posts.models import Post, Category
from rest_framework import serializers


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

    