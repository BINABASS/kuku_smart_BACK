from rest_framework import serializers
from .models import Category, Article, Comment, FAQ

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author_name = serializers.CharField(source='author.email', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('category_name', 'author_name')

class CommentSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(source='article.title', read_only=True)
    author_name = serializers.CharField(source='author.email', read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article_title', 'author_name')

class FAQSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = FAQ
        fields = '__all__'
        read_only_fields = ('category_name',) 