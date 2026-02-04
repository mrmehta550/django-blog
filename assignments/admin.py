from django.contrib import admin
from .models import About, SocialLink

# Edit admin for not adding more than 1 about now it not showing add button after adding 1 about


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)