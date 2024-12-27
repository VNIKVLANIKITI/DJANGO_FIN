from django.shortcuts import render
from users.models import User
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserEditForm, UserLogoutForm
from django.urls import reverse_lazy


def get_users_list(request):
    users_list = User.objects.all()
    context = {
        'object_list': users_list,
        'active_menu': 'users',
    }
    return render(request, 'users/users_list.html', context)


class EditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "users/edit.html"
    success_url = reverse_lazy('users:edit')

    def get_success_url(self):
        return reverse_lazy('users:edit', kwargs={'pk': self.object.pk})


class LogoutView(UpdateView):
    model = User
    form_class = UserLogoutForm
    template_name = "users/logout.html"
    success_url = reverse_lazy('/')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')
