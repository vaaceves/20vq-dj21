from django.contrib import admin
from .models import Topic, Question


# SCHOOL
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_eng',)}


# SCHOOL
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('speaker',)}


# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
