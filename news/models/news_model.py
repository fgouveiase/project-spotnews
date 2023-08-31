from django.db import models
from .user_model import Users
from news.validation import title_count_validation


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[title_count_validation]
    )
    content = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
