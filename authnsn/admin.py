from django.contrib import admin
from .models import Student, Staff,StaffPassword,StudentPassword

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'get_full_name', 'student_type', 'email', 'is_registered', 'age')
    search_fields = ('roll_number', 'email', 'mobile_number')
    list_filter = ('student_type', 'is_registered', 'date_of_birth')  # Filtering by student type and registration status
    ordering = ('-date_of_birth',)  # Orders by date of birth descending by default
    
    def get_full_name(self, obj):
        return f"{obj.roll_number} - {obj.get_student_type_display()}"
    get_full_name.short_description = 'Full Name'

    def age(self, obj):
        from datetime import date
        return (date.today() - obj.date_of_birth).days // 365
    age.short_description = 'Age'

    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'date_of_birth', 'email', 'mobile_number', 'is_registered')
    search_fields = ('staff_id', 'email', 'mobile_number')
    list_filter = ('is_registered',)
    ordering = ('-date_of_birth',)
    
@admin.register(StaffPassword)
class StaffPasswordAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'role', 'created_at', 'updated_at']
    list_filter = ['role', 'created_at']
    search_fields = ['identifier']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    fieldsets = (
        ('User Information', {
            'fields': ('identifier', 'role', 'password_hash')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return False  # Prevent manual password hash creation
    
@admin.register(StudentPassword)
class StudentPasswordAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'role', 'created_at', 'updated_at']
    list_filter = ['role', 'created_at']
    search_fields = ['identifier']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    fieldsets = (
        ('User Information', {
            'fields': ('identifier', 'role', 'password_hash')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return False  # Prevent manual password hash creation
    
    # Customizing Admin Titles
admin.site.site_header = "Department of Information Technology"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to the Admin Dashboard"


# 2. Update your admin.py file to include the custom announcement interface

# authnsn/admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Announcement  # Import your other models as well

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_at', 'is_active')
    list_filter = ('priority', 'is_active', 'created_at')
    search_fields = ('title', 'message')
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-announcement/', self.admin_site.admin_view(self.send_announcement_view), 
                 name='send-announcement'),
        ]
        return custom_urls + urls
    
    def send_announcement_view(self, request):
        if request.method == 'POST':
            title = request.POST.get('title')
            message_text = request.POST.get('message')
            priority = request.POST.get('priority')
            
            # Create and save the announcement
            announcement = Announcement.objects.create(
                title=title,
                message=message_text,
                priority=priority
            )
            
            messages.success(request, f'Announcement "{title}" has been sent successfully!')
            return redirect('admin:authnsn_announcement_changelist')
        
        return render(request, 'admin/send_announcement.html', {
            'title': 'Send New Announcement',
            'priorities': Announcement._meta.get_field('priority').choices,
        })

admin.site.register(Announcement, AnnouncementAdmin)