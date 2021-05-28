def _get_latest_post(queryset):
    return queryset.filter(is_public=True).order_by('created_at')[:5]
