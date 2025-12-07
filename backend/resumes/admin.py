from django.contrib import admin
from .models import Resume, Education, Experience, Project, Skill

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "country", "user", "created_at")
    search_fields = ("full_name", "email", "phone", "country", "user__username")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "resume", "institute", "degree", "start_date", "end_date")
    search_fields = ("school", "degree")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "resume", "company", "role", "start_date", "end_date")
    search_fields = ("company", "role")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "resume", "title")
    search_fields = ("title",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "resume", "name", "level")
    search_fields = ("name",)
