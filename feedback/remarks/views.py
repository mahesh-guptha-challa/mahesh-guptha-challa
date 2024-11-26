from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .form import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .form import FeedbackForm


class FeedbackView(CreateView):

    form_class = FeedbackForm
    model = Feedback
    template_name = "remarks/feedback.html"
    success_url  = "/thank-you"




# class FeedbackView(FormView):

#     template_name = "remarks/feedback.html"
#     form_class = FeedbackForm
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class FeedbackView(View):
    
#     def get(self, request):

#         data_form = FeedbackForm()
#         return render(request, 'remarks/feedback.html', {"form": data_form})   

#     def post(self, request):
#         data_form = FeedbackForm(request.POST)

#         if data_form.is_valid():
#             data_form.save()
#             return HttpResponseRedirect("/thank-you")
        
#         return render(request, 'remarks/feedback.html', {"form": data_form})   


# Create your views here.
# def feedback(request):

#     if request.method == 'POST':

#         # for updating the existing record use the following code
#         # previous_record = Feedback.objects.get(id = 1)
#         # data_form = FeedbackForm(request.POST, instance=previous_record)
#         data_form = FeedbackForm(request.POST)

#         if data_form.is_valid():
#             # The data is in the following varibale.
#             # print(data_form.cleaned_data['user_name'])
#             # cleaned_data = data_form.cleaned_data
#             # feedback = Feedback(rating = cleaned_data['rating'], description = cleaned_data['remarks'],
#             #                     username = cleaned_data['user_name'])
#             # feedback.save()

#             data_form.save()
        


#         # if not request.POST['username'].strip():
#         #     return render(request, 'remarks/feedback.html', {"has_error": True})
        
#         # print(request.POST['username'])

#             return HttpResponseRedirect("/thank-you")
#     else:
#         data_form = FeedbackForm()

#     return render(request, 'remarks/feedback.html', {"form": data_form})


class ThankYouView(TemplateView):

    template_name = "remarks/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['test'] = "That Work's"
        return context


class ReviewView(ListView):

    template_name = "remarks/reviews.html"
    model = Feedback    
    context_object_name = "remarks"    

    # def get_queryset(self) -> QuerySet[Any]:
    #     query = super().get_queryset().filter(rating__gte=5)
    #     return query

class ReviewEachView(DetailView):

    template_name = "remarks/detail.html"
    model = Feedback

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_object = self.object
        request = self.request
        print(request.session.get_expiry_age())
        context["favourite"] = request.session.get("favourite") == str(loaded_object.id)
        return context

class FavouriteView(View):

    def post(self, request):
        id = request.POST["review_id"]
        request.session["favourite"] = id

        return HttpResponseRedirect(reverse('data', args=[id])) 


# def thankyou(request): 

#     return HttpResponse("Succesfully Submitted")
