from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django_registration.backends.activation.views import RegistrationView

from .forms import UserLoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('courses:list')


class UserLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('accounts:login')


class UserRegistrationView(RegistrationView):
    form_class = UserRegistrationForm

    def get_initial(self):
        initial = super().get_initial()
        email = self.request.session.get('account_verified_email')
        if email:
            initial['email'] = email

        return initial
