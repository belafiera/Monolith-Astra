from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Author)
admin.site.register(Library)
