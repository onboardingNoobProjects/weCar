from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deal
from .forms import UserForm



# Create your views here.

def index(request):
    all_deals = Deal.objects.all()
    return render(request, 'weCar/index.html', {'all_deals' : all_deals})

def detail(request, deal_id):
    deal = get_object_or_404(Deal, pk=deal_id)
    return render(request, 'weCar/detail.html', {'deal': deal})

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'wecar/registration_form.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request.self.template_name, {'form': form})
#
#     # retreive form data
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit=False)
#
#             # cleaned, normailsed data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # returns User object if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('wecar:index')
#
#         return render(request, self.template_name, {'form': form})
