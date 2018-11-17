from django.contrib import admin
from notes.models import notes,UserProfileInfo,Comment,Feedback

# Register your models here.
admin.site.register(notes)
admin.site.register(UserProfileInfo)
admin.site.register(Comment)
admin.site.register(Feedback)
