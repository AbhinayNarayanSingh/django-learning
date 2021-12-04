from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published').order_by('-publish')


class Compose(models.Model):

    status_choice=(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, unique_for_date='publish', default="")
    
    body=models.TextField()
    description=models.TextField()
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status=models.CharField(max_length=250, choices=status_choice, default='draft')


    objects = models.Manager() # The default manager.
    query = PublishManager() # Our custom manager.

    class Meta:
        verbose_name_plural = "Composes"
        ordering = ('-status',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:postslug", args= [self.pk, self.slug])
    



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])


class Feedback(models.Model):

    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=250)
    message=models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:home")
