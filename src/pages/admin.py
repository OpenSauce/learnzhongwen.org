from django.contrib import admin

from .models import Interest
from .models import Post

admin.site.register(Post)
admin.site.register(Interest)
