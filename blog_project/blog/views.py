from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Author, Tag, Post

# Create your views here.
def author(request, id):
    try:
        author = Author.objects.get(id = id)
        return render(request, "blog/viewauthor.html", context={"name": f"{author.firstname} {author.lastname}",
                                                            "email": author.email})
    except Author.DoesNotExist:
        raise Http404("Record Not Found.")

def tag(request, id):
    try:
        tag = Tag.objects.get(id = id)
        return render(request, 'blog/viewslug.html', context={"tag":tag.caption})
    except Tag.DoesNotExist:
        raise Http404("Record Not Found.")

def post(request, slug):
        post = Post.objects.get(slug = slug)
        post = get_object_or_404(Post, slug=slug)
        # if not post:
        #     raise Http404("Not found.")
        # else:
        #     post = post[0]
        return render(request, "blog/post.html", context={"post": post, "authorid": post.author.id, "tagid": post.tag.all()[0].id})

def all_posts(request):
    posts = Post.objects.all().order_by("slug")

    return render(request, "blog/all_posts.html", context={"posts": posts})