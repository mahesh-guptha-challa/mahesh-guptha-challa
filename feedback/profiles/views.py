from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.

async def write_file(file):

    with open(f"temp/{file.name}", "wb") as f:

        for i in file.chunks():
            f.write(i)

    return "Done"

# class CreateProfileView(View):
#     async def get(self, request):
#         return render(request, "profiles/create_profile.html")

#     async def post(self, request):
#         print(request.FILES)
#         file = request.FILES['image']
#         await write_file(file)
#         return HttpResponseRedirect("/profiles/")

# class CreateProfileView(View):

#     def get(self, request):

#         form = ProfileForm()

#         return render(request, "profiles/create_profile.html", context={"form":form})
    
#     def post(self, request):

#         profile_from = ProfileForm(request.POST, request.FILES)

#         if profile_from.is_valid():
#             user_profile = UserProfile(image_file = profile_from.cleaned_data['user_image'])
#             user_profile.save()
#             return HttpResponse("Uploaded")
#         else:
#             print(profile_from.errors)
        
#         return render(request, "profiles/create_profile.html", context={"form":profile_from})


class CreateProfileView(CreateView):

    template_name = "profiles/create_profile.html"
    model = UserProfile
    context_object_name = "form"
    success_url = reverse_lazy(viewname="image")
    fields = "__all__"




class viewsListProfileView(ListView):

    template_name = "profiles/profile.html"
    model = UserProfile
    context_object_name = "profiles"
    

