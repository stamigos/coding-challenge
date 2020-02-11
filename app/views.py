from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View
from butter_cms import ButterCMS

client = ButterCMS('fef6b0175571c4faa36934f8f116dc1ce5e530d3')


class HomePage(TemplateView):
    template_name = "index.html"


class BlogHome(View):
    def get(self, request, page=1):
        response = client.posts.all({'page_size': 10, 'page': page})

        try:
            recent_posts = response['data']
        except:
            raise Http404('Page not found')

        next_page = response['meta']['next_page']
        previous_page = response['meta']['previous_page']

        return render(request, 'blog_list.html', {
            'recent_posts': recent_posts,
            'next_page': next_page,
            'previous_page': previous_page
        })


class BlogPost(View):
    def get(self, request, slug=None):
        try:
            response = client.posts.get(slug)
        except:
            raise Http404('Post not found')

        post = response['data']
        return render(request, 'blog_post.html', {
            'post': post
        }) 