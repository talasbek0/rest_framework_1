from django.contrib import admin
from .models import *


admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Person)