from .models import Article,ArtContent
from django.contrib.auth.models import User, Group
from rest_framework import serializers

#serializers定义api的表现形式
class ArticleSerializers(serializers.HyperlinkedModelSerializer):
    #外键序列化
    user_owner=serializers.CharField(source='user_owner.username')
    user_id = serializers.IntegerField(source='user_owner.id')
    #使用ModelSerializer序列化model模型
    class Meta:
    #指定序列化的模型
        model=Article
        fields=('art_name','art_add_date','art_author','art_type','art_status','art_introduction','art_name_used','user_owner','user_id')
    		
class ArtContentSerializers(serializers.HyperlinkedModelSerializer):
    article=serializers.CharField(source='article.art_name')
    article_id=serializers.IntegerField()
    class Meta:
        model=ArtContent
        fields=('chapter_name','chapter_content','chapter_add_date','article','article_id')

