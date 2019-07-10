from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Article,ArtContent,ArtLabel,ArtHot,ArtDiscuss
from . forms import ArticleForm,ArtContentForm

from rest_framework import viewsets
from learning_logs.serializers import ArticleSerializers,ArtContentSerializers
from django.core.paginator import Paginator

def index(request):
	"""主页（文章列表页）"""
	articles=Article.objects.order_by('art_add_date')
	context={'articles':articles}
	return render(request,'learning_logs/index.html',context)
	# return render(request,'article/list.html',context)

def article(request,article_id):
	"""文章详情页，具体单页"""
	article=Article.objects.get(id=article_id)
	artcontents=article.artcontent_set.all()
	#分页功能
	#20条一页
	# if len(artcontents)<=20:
	# 	num=len(artcontents)
	# else:
	# 	num=20
	paginator=Paginator(artcontents,10)
	current_page=int(request.GET.get('page',1))
	#分页标签显示7个
	if paginator.num_pages >7 :
		if current_page-3 < 1:
			page_ran=range(1,8)
		elif current_page +3 >paginator.num_pages:
			page_ran=range(paginator.num_pages-6,paginator.num_pages+1)
		else:
			page_ran=range(current_page-3,current_page+4)
		page_range=page_ran
	else:
		page_range=paginator.page_range


	current_page_content=paginator.page(current_page)
	context = {'article':article,'current_page_content':current_page_content,'page_range':page_range}
	return render(request,'learning_logs/article.html',context)

@login_required
def new_article(request):
	"""添加新文章"""
	if request.method != 'POST':
		form = ArticleForm()
	else:
		form = ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save(commit=False)
			new_article.user_owner=request.user
			new_article.save()
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context ={'form':form}
	return render(request,'learning_logs/new_article.html',context)

@login_required
def edit_art_content(request,article_id):
	"""修改文章标题等内容"""
	article = Article.objects.get(id=article_id)
	art_content =article.artcontent_set.all()
	if article.user_owner != request.user:
		raise Http404
	if request.method != "POST":
		form = ArticleForm(instance=article)
	else:
		form = ArticleForm(instance=article,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:article',
				args=[article.id]))
	context={'article':article,'art_content':art_content,'form':form}
	return render(request,'learning_logs/edit_art_content.html',context)

@login_required
def new_chapter(request,article_id):
	article = Article.objects.get(id=article_id)
	art_content=article.artcontent_set.all()
	if article.user_owner != request.user:
		raise Http404	
	if request.method !='POST':
		form=ArtContentForm()		
	else:
		#post的表单中外键article字段为null	
		form=ArtContentForm(request.POST)

		if form.is_valid:
			#验证成功后需要为外键article字段，设置参数（instance.article）为实例（article）
			form.instance.article=article
			#接受了POST以及article实例后保存
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:article',args=[article_id]))
		else:
			raise Http404
	context={'form':form,'article':article}
	return render(request,'learning_logs/new_chapter.html',context)

from django.db.models.aggregates import Count
def look_chapter(request,art_id,chap_id):
	"""查看具体章节"""
	artcontent=ArtContent.objects.get(id=chap_id)
	article=Article.objects.get(id=art_id)

	if int(chap_id) <= 5:
		obj=ArtContent.objects.filter(id__gt=chap_id,article_id=art_id).first()
		context = {'artcontent': artcontent, 'article': article, 'obj': obj}
		return render(request, 'learning_logs/look_chapter.html', context)
	else:
		return HttpResponseRedirect(reverse('learning_logs:index'))

@login_required
def edit_chapter(request,article_id,chapter_id):
	#实例化具体一片文章
	article=Article.objects.get(id=article_id)
	#实例化具体的一章内容
	artcontent=ArtContent.objects.get(id=chapter_id)
	# """修改章节内容"""
	if article.user_owner!=request.user:
		raise Http404
	if request.method != 'POST':
		form=ArtContentForm(instance=artcontent)
	else:
		form=ArtContentForm(instance=artcontent,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:look_chapter',
				args=[article.id,artcontent.id]))
	context ={'artcontent':artcontent,'form':form,'article':article}
	
	
	return render(request,'learning_logs/edit_chapter.html',context)
	

def search(request):
	"""搜索功能"""
	search_name=request.GET.get('search_name')
	error_msg=''

	if not search_name:
		error_msg='请输入关键词'

		return render(request,'learning_logs/index.html',{'error_msg': error_msg})
	articles=Article.objects.filter(art_name__icontains=search_name)
	return render(request,'learning_logs/search_results.html',
		{'error_msg': error_msg,'articles': articles})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all() #集合
    serializer_class = ArticleSerializers  #序列化
class ArtContentViewSet(viewsets.ModelViewSet):
	queryset=ArtContent.objects.all()
	serializer_class=ArtContentSerializers