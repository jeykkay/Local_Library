from django.contrib import admin
from catalog.models import Author, Book, BookCopy, Genre, Language, Country


class BookInline(admin.TabularInline):
    model = Book


class BookCopyInline(admin.StackedInline):
    model = BookCopy


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'pseudonym')
    search_fields = ('pseudonym', 'first_name', 'last_name')
    inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    search_fields = ('title', 'author__pseudonym', 'author__first_name', 'genre__name')
    inlines = [BookCopyInline]


class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'isbn', 'status')
    fieldsets = (
        ('Group 2', {
            'fields': ('book', 'isbn', 'languages')
        }),
        ('Group 2', {
            'fields': ('borrower', 'due_back', 'status')
        })
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookCopy, BookCopyAdmin)

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
