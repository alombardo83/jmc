from django.contrib import admin

from .models import Rating, Response


class ResponseInline(admin.StackedInline):
    model = Response
    extra = 0


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('username', 'rating', 'body', 'date')
    fields = ('username', 'rating', 'body')
    inlines = [ResponseInline]
