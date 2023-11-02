from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    owner = models.ForeignKey(
        "users.User", related_name="notes", on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.name