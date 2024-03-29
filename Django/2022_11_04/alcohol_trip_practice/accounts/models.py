from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")
    profile_image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 80},
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"