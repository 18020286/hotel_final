# from tabination.views import TabView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import *
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView
# from .models import User
from booking.models import Reservation

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()


def index(request):
    return render(request, 'pages/home.html')


class SiteLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             messages.success(request, 'Sign up successfully')
#             login(request, user)
#             return redirect('login')
#         else:
#             return render(request, 'pages/register.html', {"form": form})
#     form = CustomUserCreationForm()
#     return render(request, 'pages/register.html', {"form": form})


# class SiteRegisterView(FormView):
#     template_name = 'pages/register.html'
#     form_class = RegisterForm
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         new_user = User.objects.create_user(
#             username=data['username'],
#             password=data['password1'],
#             email=data['email']
#         )
#         # url = f"{reverse('register_ok')}?username={new_user.username}"
#         # return redirect(url)
#
class SiteRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_message = 'Sign up successfully'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteRegisterOkView(TemplateView):
    template_name = 'pages/register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


@login_required()
class ReservationsListView(ListView):
    queryset = User.objects.all()
    template_name = 'pages/profile.html'
    context_object_name = 'reservations'


@login_required()
def edit_profile(request):
    if request.GET.get('rev'):
        rev = Reservation.objects.get(pk=request.GET.get('rev'))
        rev.status = 'cancel'
        rev.save()
    my_bookings = Reservation.objects.all().filter(user=request.user.id)
    num_bookings = len(my_bookings)
    form = ProfileEditForm(instance=request.user)
    pass_form = PasswordChangeForm(request.user)
    if request.method == "POST":
        if 'first_name' in request.POST:
            form = ProfileEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('/profile')
        elif 'new_password1' in request.POST:
            pass_form = PasswordChangeForm(request.user, request.POST)
            if pass_form.is_valid():
                user = pass_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/profile')
    content = {
        'form': form,
        'pass_form': pass_form,
        'my_bookings': my_bookings,
        'num_bookings': num_bookings
    }
    return render(request, 'pages/profile.html', content)


@staff_member_required
def view_admin_page(request):
    return render(request, 'admin/admin-page.html')


# class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
#
#     def test_func(self):
#         return self.request.user.is_superuser


# class AdminPageSite(TemplateView, AdminStaffRequiredMixin):
#     template_name = 'admin/admin-page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
