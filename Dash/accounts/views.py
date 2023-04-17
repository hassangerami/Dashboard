from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm, SignInForm
from usermodel.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin



class SignUpView(View):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(full_name=cd['full_name'], email=cd['email'], password=cd['password'])

            messages.success(request, 'you have successfully registered')
            return redirect('accounts:user_signin')

        return render(request, self.template_name, {'form': form})


class SignInView(View):
    template_name = 'accounts/signin.html'
    form_class = SignInForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])

            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully')
                return redirect('dashboards:user_panel')
            else:
                messages.error(request, 'Email or Password invalid!')

        return render(request, self.template_name, {'form': form})


class SignOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you are logged out successfully')
        return redirect('accounts:user_signin')
