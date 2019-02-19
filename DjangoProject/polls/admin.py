from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
class QuestionAdmin(admin.ModelAdmin):
    # fields = [
    #     (None,                  {'fields':['question_text']}),
    #     ('Date information',    {'fields':['pub_date'], 'classes':['collapse']}),
    # ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)