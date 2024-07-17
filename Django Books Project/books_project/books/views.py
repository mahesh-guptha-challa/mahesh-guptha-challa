from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from . import models
from django.db.models import Count, Sum
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json


# Create your views here.

def all_books(request):
    
    data = models.Book.objects.all().order_by("id")
    
    output_data = []

    count = data.aggregate(Count("id"), Sum("rating"))
    for i in data:
        output_data.append({"title": i.title, "rating": i.rating, "id": i.id})
    # return JsonResponse(output_data, status = 200, safe=False)
    # return JsonResponse(list(data.values("id", "title", "rating")), status = 200, safe=False)
    # data = serializers.serialize("json", data)
    # return JsonResponse({"data":data} , status = 200, safe=False)

    return render(request, "allbooks.html", {"data": data, "count": count})

    

@csrf_exempt
def add_book(request):  
    print("Received request: %s", request.body)
    if request.method  == 'POST':

        data = json.loads(request.body.decode('utf-8'))

        title = data.get('title')

        rating = data.get('rating')

        if rating and title:
            books_saved = models.Book(title=title, rating=rating)
            books_saved.save()
            # saved_book = models.Book.objects.create(title= title, rating=rating)

            return JsonResponse({"id": books_saved.id, "message": "data saved succesfully"}, status = 201)

    
    return HttpResponseBadRequest("error occured")

@csrf_exempt
def delete_book(request, id):

    if request.method == "DELETE":
        models.Book.objects.filter(id = id).delete()

        return JsonResponse({"message": "Deleted succesufully", "id" : id}, status = 204)
    
    return HttpResponseBadRequest("Request Reponse not found")

def detail_book(request, slug):

    # render("book.html")
    # return "test"
    return HttpResponse(models.Book.objects.get(slug=slug).id)
    