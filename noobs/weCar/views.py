from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin, StaffuserRequiredMixin
from .forms import UserForm
from .models import Deal



class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'weCar/index.html'
    context_object_name = 'all_deals'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Deal.objects.filter(title__icontains=query)
        else:
            return Deal.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Deal
    template_name = 'weCar/detail.html'

class DealCreate(StaffuserRequiredMixin, CreateView):
    model = Deal
    fields = ['title', 'details', 'RRP', 'price', 'tippingPoint', 'expiry', 'pic']

class DealUpdate(StaffuserRequiredMixin, UpdateView):
    model = Deal
    fields = ['title', 'details', 'RRP', 'price', 'tippingPoint', 'expiry', 'pic']

class DealDelete(StaffuserRequiredMixin, DeleteView):
    model = Deal
    success_url = reverse_lazy('index', kwargs={})

class UserFormView(AnonymousRequiredMixin, View):
    authenticated_redirect_url = u"index"
    form_class = UserForm
    template_name = 'wecar/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # retreive form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned, normailsed data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})
