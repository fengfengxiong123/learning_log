from django.contrib import admin

# Register your models here.
#引用
from learning_logs.models import Article,ArtContent,ArtLabel,ArtHot,ArtDiscuss

class  ArtLabelInline(admin.TabularInline):
	"""文章内容页面折叠显示在文章页面"""
	model=ArtLabel
	extra=1

class ArticleAdmin(admin.ModelAdmin):
	"""创建模型后台类"""
	#给Article模型中字段排序
	# 如fields=['art_author','art_name']
	
	#字段集,把字段分类后显示
	fieldsets=[
		('主要信息',{'fields':['art_name','art_author','art_introduction']}),
		('次要信息',{'fields':['user_owner','art_type','art_status','art_name_used']})
	]

	inlines=[ArtLabelInline]
	#以列的形式展示对象
	list_display=('art_name','art_author','user_owner','art_type','art_status',
		'art_introduction','art_name_used','art_add_date')
	#过滤器
	list_filter=['art_add_date']
	#搜索框
	search_fields=['art_name']


admin.site.register(Article,ArticleAdmin)
admin.site.register(ArtContent)
admin.site.register(ArtLabel)
admin.site.register(ArtHot)
admin.site.register(ArtDiscuss)