from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Work)
admin.site.register(message_detail)

admin.site.register(Home_page)