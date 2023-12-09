from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# posts = [
#     {
#         "heading": "Web Developers Posts",
#         "author": "Alex Ladwong",
#         "email": "alexladwong@gmail.com",
#         "title": "https://ladwongdevelopers.com/",
#         "content": "The Official Webdev. Blog site",
#         "date_created": "Wed. 6. Dec. 2023",
#     },
#     {
#         "heading": "Accounting Posts",
#         "author": "Alal Susan",
#         "email": "susanalal2010@gmail.com",
#         "title": "https://mrs.susanladwongacounting.com/",
#         "content": "The Official Acoountants Blog site",
#         "date_created": "Tues. 10. Nov. 2023",
#     },
# ]


# Create your views here.
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "myblogApp/home.html", context)


def about(request):
    return render(request, "myblogApp/about.html", {"title": "About Us Blog"})
