from django.contrib import admin
from .models import Course, Quiz, Question, Choice

admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)