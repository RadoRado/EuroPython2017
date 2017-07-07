from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from django.shortcuts import redirect

from django.views.generic import View, FormView
from django.contrib.auth import views as auth_views

from .forms import RegisterForm
from .services import user_registration_flow


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def get_redirect_url(self):
        return reverse('repl:index')


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        try:
            user_registration_flow(**form.cleaned_data)
        except ValidationError as error:
            for field, errors in error.error_dict.items():
                for error in errors:
                    form.add_error(field, error)

            return self.form_invalid(form)

        return redirect('users:login')


class LogoutView(auth_views.LogoutView):
    pass
