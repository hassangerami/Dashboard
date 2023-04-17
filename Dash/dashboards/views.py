from django.shortcuts import render, redirect
from django.views import View
from .forms import CreateForm, TicketForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CreateModel, TicketModel


class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboards/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:user_signin')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        reads = CreateModel.objects.all()
        return render(request, self.template_name, {'reads': reads})


class CreateView(LoginRequiredMixin, View):
    template_name = 'dashboards/create.html'
    form_class = CreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:user_signin')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            CreateModel.objects.create(first_name=cd['first_name'], last_name=cd['last_name'], address=cd['address'])

            return redirect('dashboards:user_panel')
        return render(request, self.template_name, {'form': form})


class TicketView(LoginRequiredMixin, View):
    template_name = 'dashboards/ticket.html'
    form_class = TicketForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:user_signin')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            TicketModel.objects.create(title=cd['title'], description=cd['description'])

            return redirect('dashboards:user_panel')
        return render(request, self.template_name, {'form': form})
