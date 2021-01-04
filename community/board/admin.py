from django.contrib import admin
from .models import Board
# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer')
    #admin site에서 실제 값들을 쉽게 확인하기 위해 필드명들 명시하면 -> 나온당

admin.site.register(Board, BoardAdmin)