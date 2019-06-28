from django import forms
from .models import Article,ArtContent

from django.forms import ModelForm

class ArticleForm(forms.ModelForm):
	#帖子表
	class Meta:
		model = Article
		# fields = ['invitation_text','invitation_title','invitation_label',
		# 	'invitation_energy','invitation_owner']
		fields = ['art_name','art_author','art_type',
			'art_status','art_introduction']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class ArtContentForm(forms.ModelForm):
	class Meta:
		model=ArtContent
		fields=['chapter_name','chapter_content']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
		
	def __new__(cls, *args, **kwargs):
		#fields循环打印出组件
		#django是通过“__new__”方法，找到ModelForm里面的每个字段的，然后循环出每个字段添加自定义样式
		#cls.base_fields是一个元祖，里面是 所有的  【(字段名，字段的对象),(),()】
		for field_name in cls.base_fields:
			filed_obj = cls.base_fields[field_name]
			#添加属性
			filed_obj.widget.attrs.update({'class':'form-control'})

		return ModelForm.__new__(cls)
