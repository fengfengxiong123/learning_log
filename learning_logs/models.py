from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField
#一对多
#User（系统自带）--Article（表1）
#Article（表1）--ArtContent（表2）
#Article（表1）--ArtLabel（表3）
#Article（表1）--ArtDiscuss（表5）
#User（系统自带）--ArtDiscuss（表5）
#一对一
#Article（表1）--ArtHot（表4）??
class Article(models.Model):
	"""文章表（表1）"""
	art_name=models.CharField('标题',max_length=200)
	art_add_date=models.DateTimeField(auto_now_add=True)
	art_author=models.CharField('作者',max_length=10,default="")
	user_owner=models.ForeignKey(User,on_delete=models.CASCADE)
	art_type=models.CharField('类型',max_length=200)
	art_status=models.CharField('状态',max_length=200,default="")
	art_introduction=models.CharField('简介',max_length=200,default="")
	art_name_used=models.CharField('曾用名',max_length=200,default="")
		
	def __str__(self):
		if len(self.art_name)>=20:
			art_name_limit=self.art_name[:20]+'...'
		else:
			art_name_limit=self.art_name
			#限制返回文章名字符数
		return art_name_limit 

class ArtContent(models.Model):
	"""文章章节内容表(表2）"""	
	chapter_name=models.CharField('章名',max_length=200)
	chapter_content=HTMLField('文章内容')
	article=models.ForeignKey(Article,verbose_name="文章",on_delete=models.CASCADE,null=True)
	chapter_add_date=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['chapter_add_date']

	
class ArtLabel(models.Model):
	"""标签内容表（表3）"""
	label_content=models.CharField('标签',max_length=20)
	article=models.ForeignKey(Article,on_delete=models.CASCADE)

class ArtHot(models.Model):
	"""文章热度表（表4）"""
	hot_evaluate=models.BigIntegerField('评价值',null=True,blank=True)
	hot_browse=models.BigIntegerField('浏览量',null=True,blank=True)
	hot_relay=models.BigIntegerField('转发数',null=True,blank=True)
	hot_share=models.BigIntegerField('分享数',null=True,blank=True)
	hot_discuss=models.BigIntegerField('讨论值',null=True,blank=True)
	article=models.OneToOneField(Article,on_delete=models.CASCADE)

class ArtDiscuss(models.Model):
	"""文章讨论表（表5)"""
	discuss_content=models.TextField('留言内容')
	discuss_add_date=models.DateTimeField(auto_now_add=True)
	discuss_owner=models.ForeignKey(User,on_delete=models.CASCADE)
	article=models.ForeignKey(Article,on_delete=models.CASCADE)
	



	



