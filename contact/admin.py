from django.contrib import admin
from .models import ContactMessage
from django.utils.html import format_html
from msigana_ecommerce.admin_site import admin_site

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    readonly_fields = ('full_name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('created_at',)


    def email_login_link(self, obj=None):
        return format_html(
            '<a href="{}" target="_blank" style="color: green; font-weight: bold;">Email Login</a>',
            'https://sonaplc.com:2096/webmaillogout.cgi/'
        )
    email_login_link.short_description = 'Email Login'  # Display name in admin

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['email_login_link'] = self.email_login_link()  # Pass the link to template context
        return super().changelist_view(request, extra_context=extra_context)

    # Optionally, add the link to the admin page as a readonly field
    readonly_fields = ('email_login_link',)


admin_site.register(ContactMessage, ContactMessageAdmin)
