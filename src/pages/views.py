import markdown
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader

from .models import Interest
from .models import Post


def home(request):
    posts = Post.objects.filter(published=True)[:5]
    template = loader.get_template("pages/blog.html")
    context = {"posts": posts}
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, "pages/about.html")


def vocabulary(request):
    return render(request, "pages/vocabulary.html")


def start(request):
    return render(request, "pages/underconstruction.html")


def resources(request):
    return render(request, "pages/resources.html")


def submit_email(request):
    if request.method == "POST":
        email = request.POST["email"]
        Interest.objects.create(email=email)
    return render(request, "pages/home.html")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    html = markdown.markdown(post.content)
    return render(
        request, "pages/post_detail.html", {"post": post, "html": html}
    )
