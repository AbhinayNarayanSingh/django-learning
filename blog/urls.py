from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name='blog'

urlpatterns = [
    path("", PostsListView.as_view(), name="home"),
    path('post/<int:pk>',PostDetailView.as_view(), name='post' ),
    path('post/<int:pk>/<slug:slug>',PostDetailView.as_view(), name='postslug' ),
    path('post/create/',PostCreateView.as_view(), name='create' ),
    
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path("feedback/edit/<int:pk>", FeedbackUpdateView.as_view(), name="feedback-edit"),
    path("feedback/delete/<int:pk>", FeedbackDeleteView.as_view(), name="feedback-delete"),

    path('feedBack/', FeedbackView.as_view(), name='feedbackview'),



    path("wp-admin/sign-up", SignUpCreateView.as_view(), name="signup"),

    path("wp-admin/", auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page ="blog:login"), name='logout'),

    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/password.html', success_url='blog:user_password_change_done'), name="user_password_change"),
    path("chnage-password/done/", auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_done.html'), name="user_password_change_done"),

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/password.html', success_url='done/'), name="user_password_reset"),
    path("reset-password/done/", auth_views.PasswordResetDoneView.as_view(template_name='registration/password_done.html'), name="user_password_reset_done"),

    # ! path("reset-password/set-new-password/", auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset.html'), name="user_password_reset_confirm")         # don't know why it's not working

    

]
