from django.contrib import admin

from .models import HSK
from .models import Metric
from .models import Post

admin.site.register(Post)
admin.site.register(HSK)
admin.site.register(Metric)
