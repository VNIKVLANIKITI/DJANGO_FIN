from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import EditView, RegisterView
from users.views import get_users_list
from users.apps import UsersConfig
from django.contrib.auth import views as auth_views


app_name = "users"


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


urlpatterns = [
    path("list/", get_users_list, name='users_list'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
]
