from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect ,HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, View, CreateView
from .forms import CustomUserCreationForm

def registration_view(request):
    form = CustomUserCreationForm(request.POST)
    # print(dir(form))
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,"Siz royhatdan ottiz , endi kiring!")
        return HttpResponseRedirect("login/")
    else:
        messages.add_message(request,messages.INFO,"Xatolik!")
        return render(request, "registration/register.html", {"form":form})

    return render(request, "registration/register.html", {"form":form})


# def my_login(request):
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)

#         # Redirect to a success page.
#         return HttpResponseRedirect("/")
    
#     else:
#         # Return an 'invalid login' error message.
#         return render(request, "registration/login.html")
    
#     return render(request, "registration/login.html")

# def logout_view(request):
#     logout(request)
#     messages.add_message(request,messages.INFO,"Siz chiqdiz!") #INFO, SUCCESS, WARNING, ERROR,DEBUG
#     return HttpResponseRedirect("/")


# def login_view(request):
#     # return render(request, "registration/login.html", {"forms":forms})
#     pass



# def register_view(request):
#     return render(request, "registration/register.html",  {"forms":forms})


# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = "registration/register.html"