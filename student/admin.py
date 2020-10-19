from django.contrib import admin
from .models import Student

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    model = Student
    # list_display = ('username', 'email')
    fieldsets = ((
        None,
        {
            'fields':  (
                'email',
                'password',
                'name',
                'surname',
                'phone',
                'photo',
            )
        }
    ),)
