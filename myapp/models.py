from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_read_book", "Can read book"),
            ("can_create_book", "Can create book"),
            ("can_update_book", "Can update book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_read_article", "Can read article"),
            ("can_create_article", "Can create article"),
            ("can_update_article", "Can update article"),
            ("can_delete_article", "Can delete article"),
        ]

    def __str__(self):
        return self.title
