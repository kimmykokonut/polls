from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3 #3 slots to add data

# to customize admin form
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {"fields": ["question_text"]}),
    ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
  ]
  inlines = [ChoiceInline]
  # default str() of ea obj displayed. want to display ind. fields
  list_display = ["question_text", "pub_date", "was_published_recently"]
  # adds filter 
  list_filter = ["pub_date"]
  # adds search capability within q-text
  search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
