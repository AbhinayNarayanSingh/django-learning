from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import UserCreationForm

from .models import *

from .form import *



# Create your views here.
class PostsListView(ListView):
    model = Compose
    template_name = "index.html"
    context_object_name = 'posts'

    # add extra manager methods to an existing manager
    # // queryset= Compose.objects.filter(status='published').order_by('-publish')

    # reate a new manager by modifying the initial QuerySet that the manager returns
    queryset= Compose.query.all()


class PostDetailView(DetailView):
    model = Compose
    template_name = "post.html"
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Compose
    template_name = "newpost.html"
    fields = ['title', 'slug', 'description', 'body', 'author']
    url="/"


class FeedbackView(View):
    model = Feedback
    def get(self, request):
        template_name = "feedback.html"
        form=FeedbackForm()
        ctx = {'form': form}
        return render(request, template_name, ctx)

    def post(self, request):
        form=FeedbackForm(request.POST)
        newfeedback=form.save()
        return redirect( reverse('blog:feedbackview'), msg)





class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    fields = ['name', 'email','subject','message']
    success_url = reverse_lazy('blog:feedback')


class FeedbackUpdateView(UpdateView):
    model = Feedback
    template_name = "feedback.html"
    fields = ['name', 'email','subject','message']
    success_url = reverse_lazy('blog:feedback')


class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = "feedback_del.html"
    fields = ['name', 'email','subject','message']
    success_url = reverse_lazy('blog:feedback')


class SignUpCreateView(CreateView):
    model = User
    # form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url= reverse_lazy('blog:login')
    fields = ['username', 'password', 'first_name', 'last_name', 'email']
