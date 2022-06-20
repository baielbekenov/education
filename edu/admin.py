from django.contrib import admin

from edu.models import Task, Homework, Razdel, User, Teacher

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Homework)
admin.site.register(Razdel)
admin.site.register(Teacher)