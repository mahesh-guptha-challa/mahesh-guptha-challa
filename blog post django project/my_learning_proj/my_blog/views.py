from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
blogs = {"Test1": "this is test data every one please test it and write your test cases as soon as possible and let me know who it is working and if it is fine we can go further and rock it",
"Test2": "Simply test."}



def main(request):

    return render(request, "my_blog/homepage.html", {"latestblogs": "Test1"})

def all_posts(request):
    
    
    return render(request, "my_blog/allblogs.html", {"data" : blogs})

def single_post(request , post_name):

    return render(request, "my_blog/singleblog.html", {"each_post" : blogs[post_name]})