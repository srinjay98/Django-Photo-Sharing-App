from django.contrib import admin
from django.db.models import Count

from .models import MemoryPost


@admin.register(MemoryPost)
class MemoryPostAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
        'short_description',
        'total_likes',
        'created_at',
    ]

    list_display_links = [
        'id',
        'user',
    ]

    search_fields = [
        'user__username',
        'description',
    ]

    list_filter = [
        'created_at',
    ]

    ordering = [
        '-created_at',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    list_per_page = 10

    date_hierarchy = 'created_at'

    def get_queryset(self, request):

        queryset = super().get_queryset(request)

        queryset = queryset.annotate(
            likes_count=Count('likes')
        )

        return queryset

    def total_likes(self, obj):
        return obj.likes_count

    total_likes.short_description = 'Likes'

    def short_description(self, obj):
        return obj.description[:40]

    short_description.short_description = 'Description'