from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Studio, Class, Trainer, Review, Studio_User

# Register your models here.
UserAdmin.fieldsets +=  ('City', {'fields': ('city',)}), ('Profile photo', {'fields': ('profile_photo',)}), ('Classes', {'fields': ('classes',)}), ('Reviews', {'fields': ('reviews',)}), ('Is studio owner?', {'fields': ('studio_owner',)}), ('Current plan', {'fields': ('plan',)}), ('Credits amount', {'fields': ('credits',)}),

admin.site.register(User, UserAdmin)
admin.site.register(Studio)
admin.site.register(Class)
admin.site.register(Trainer)
admin.site.register(Review)
admin.site.register(Studio_User)