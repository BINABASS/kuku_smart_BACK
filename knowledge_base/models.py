from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'knowledge_categories_tb'
        verbose_name = _('Knowledge Category')
        verbose_name_plural = _('Knowledge Categories')
    
    def __str__(self):
        return self.name

class Article(models.Model):
    ARTICLE_TYPES = [
        ('guide', 'Guide'),
        ('tutorial', 'Tutorial'),
        ('faq', 'FAQ'),
        ('news', 'News'),
        ('tip', 'Tip'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=20, choices=ARTICLE_TYPES, default='guide')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = models.JSONField(default=list)
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'knowledge_articles_tb'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'knowledge_comments_tb'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author.email} on {self.article.title}"

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'knowledge_faqs_tb'
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.question[:50] + "..." if len(self.question) > 50 else self.question
