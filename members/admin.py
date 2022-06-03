from django.contrib import admin
from . models import Individual, Member, EventInfo
# Register your models here.

admin.site .register(Individual)
admin.site .register(Member)
admin.site .register(EventInfo)
