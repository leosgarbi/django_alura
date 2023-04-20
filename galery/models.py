from django.db import models
from datetime import datetime

class Photos(models.Model):
    category_options= [
    ("PORTRAIT", "Portrait"),
    ("B&W", "B&W"),
    ("LANDSCAPE", "Landscape"),
    ("PHOTOJOURNALISM", "Photojournalism"),
    ]
    name = models.CharField(max_length=100, null=False, blank=False)
    subtittle = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=category_options, default='')
    description = models.TextField(null=False, blank=True)
    photo = models.CharField(max_length= 100, null=False, blank=False)
    published = models.BooleanField(default=False)
    photo_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"photography [nome={self.name}]"