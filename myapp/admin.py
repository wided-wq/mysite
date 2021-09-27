from django.contrib import admin
from .models import Categories, Courses


class CoursesAdmin(admin.ModelAdmin):
    search_fields = ['title','course_details']


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Categories, CategoriesAdmin)
