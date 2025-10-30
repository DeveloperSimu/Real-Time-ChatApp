from django.urls import path
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # ✅ Login route
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),

    # ✅ Logout route (GET & POST দুটোই handle করবে)
    path("auth/logout/", LogoutView.as_view(next_page="login-user"), name="logout-user"),
]
