from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):

    #index.htmlを描画する
    template_name = 'index.html'

    #参照するモデルを指定する
    queryset = BlogPost.objects.order_by('-posted_at')

    #1ページに表示する件数
    paginate_by = 4

class BlogDetail(DetailView):
    
    #post.htmlを描画する
    template_name = 'post.html'

    #参照するモデルを設定
    model = BlogPost