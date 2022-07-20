from django.contrib import admin
from .models import*
from mptt.admin import MPTTModelAdmin



admin.site.register(Category, MPTTModelAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'serves', 'prep_time','cook_time']
    
class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category','author']
    inlines = [RecipeInline]
    prepopulated_fields = {'slug': ('title',)}
    save_as= True
    save_on_top= True

