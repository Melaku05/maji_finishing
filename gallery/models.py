from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
