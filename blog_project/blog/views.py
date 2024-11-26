from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Author, Tag, Post
from .forms import PostForm
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.
# def author(request, id):
#     try:
#         author = Author.objects.get(id = id)
#         return render(request, "blog/viewauthor.html", context={"name": f"{author.firstname} {author.lastname}",
#                                                             "email": author.email})
#     except Author.DoesNotExist:
#         raise Http404("Record Not Found.")

class AuthorView(DetailView):
    
    template_name = 'blog/viewauthor.html'
    model = Author
    context_object_name = "author"


# def tag(request, id):
#     try:
#         tag = Tag.objects.get(id = id)
#         return render(request, 'blog/viewslug.html', context={"tag":tag.caption})
#     except Tag.DoesNotExist:
#         raise Http404("Record Not Found.")


class TagClass(DetailView):

    template_name = "blog/viewslug.html"
    model = Tag


# class EachPostView(DetailView):
    
#     template_name = "blog/post.html"
#     model = Post

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         print(self.request.session.get("read_later"))
#         if self.request.session.get("read_later"):
#             if post.slug in self.request.session.get("read_later"):
#                 context['flag'] = True
#         return context
            
def post(request, slug):
        # post = Post.objects.get(slug = slug)
        post = get_object_or_404(Post, slug=slug)
        form = PostForm()
        flag = False

        if request.session.get("read_later"):
            if post.slug in request.session.get("read_later"):
                flag = True
        print(request.session.get("read_later"))
        # if not post:
        #     raise Http404("Not found.")
        # else:
        #     post = post[0]
        return render(request, "blog/post.html", context={"post": post, "authorid": post.author.id, "tagid": post.tag.all()[0].id, "form": form, "flag": flag})


class UpdatePost(UpdateView):

    template_name = "blog/post.html"
    model = Post
    success_url = reverse_lazy("AllPosts")
    fields = ['comments','image_name']

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["all_tags"] = self.object.tag.all()
        context["comments"] = self.object.comments.all()

        return context


# def all_posts(request):
#     posts = Post.objects.all().order_by("slug")

    # return render(request, "blog/all_posts.html", context={"posts": posts})

class AllPostView(ListView):
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name  = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        return  super().get_queryset().order_by("-date")[:3]
        



# class CommentsView(UpdateView):
#     model=Post
#     fields = ["comments", "image_name"]
    
#     def get_success_url(self) -> str:
#         return reverse_lazy("post", kwargs = {"slug": self.object.slug})

    
# def comments(request, slug):
#     post_request = PostForm(request.POST,request.FILES)
#     post = get_object_or_404(Post, slug=slug)
#     if post_request.is_valid():
#         post.comments = post_request.cleaned_data['comments']
#         post.image_name = request.FILES['image_name']
#         post.save()
#         return render(request, "blog/post.html", context={"post": post, "authorid": post.author.id, "tagid": post.tag.all()[0].id, "form": post_request})

#     form = PostForm()
#     return render(request, "blog/post.html", context={"post": post, "authorid": post.author.id, "tagid": post.tag.all()[0].id, "form": form})


class ReadLaterView(View):

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            if not request.session.get('read_later'):
                request.session['read_later'] = [request.POST['slug']]
            else:
                previous_data = request.session['read_later']
                previous_data.append(request.POST['slug'])
                request.session['read_later'] = previous_data
                # request.session['read_later'].append(request.POST['slug'])
                request.session.modified = True
            print(request.session['read_later'])            
            return HttpResponseRedirect(f"/post/{request.POST['slug']}")    
    
# def read_later(request):

#     form = PostForm(request.POST)
#     if form.is_valid():
#         if not request.session.get('read_later'):
#             request.session['read_later'] = [request.POST['slug']]
#         else:
#             previous_data = request.session['read_later']
#             previous_data.append(request.POST['slug'])
#             request.session['read_later'] = previous_data
#             # request.session['read_later'].append(request.POST['slug'])
#             request.session.modified = True
#         print(request.session['read_later'])            
#         return HttpResponseRedirect(f"/post/{request.POST['slug']}")    
    
    
        
             