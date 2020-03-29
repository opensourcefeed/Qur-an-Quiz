from django.contrib import admin

from django.contrib import admin
from api.models import User
from api.models import Level
from api.models import Category
from api.models import Question
from api.models import Option
from api.models import Score
from api.models import Attempt

class OptionInline(admin.TabularInline):
    model = Option
        

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionInline
    ]

admin.site.register(User)
admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Score)
admin.site.register(Attempt)
