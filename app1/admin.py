from django.contrib import admin
from  .models import Register,Book,Issue
# Register your models here.
admin.site.register(Register)
admin.site.register(Book)
admin.site.register(Issue)
