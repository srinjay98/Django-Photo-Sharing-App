from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class MemoryPost(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memory_posts'
    )

    image = models.ImageField(
        upload_to='memories/'
    )

    description = models.TextField(
        max_length=500
    )

    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Memory Post'
        verbose_name_plural = 'Memory Posts'

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username} - {self.description[:30]}"

# admin password :  eva12#098