from django.contrib import admin, messages
from .models import Movie,Director,Actor,DressingRoom
from django.db.models import QuerySet


# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor','number','actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'Рейтинг'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий рейтинг'),
            ('от 40 до 59', 'Средний рейтинг'),
            ('от 60 до 84', 'Высокий рейтинг'),
            ('>=85', 'Очень высокий рейтинг'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 84':
            return queryset.filter(rating__gte=60).filter(rating__lt=85)
        if self.value() == '>=85':
            return queryset.filter(rating__gte=85)

        # return queryset


class NameFilter(admin.SimpleListFilter):
    title = 'Начинается на букву'
    parameter_name = 'words'

    def lookups(self, request, model_admin):
        return [
            ('A', 'Начинается на А'),
            ('B', 'Начинается на B'),
            ('C', 'Начинается на C'),
            ('M', 'Начинается на M'),
            ('S', 'Начинается на S'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'A':
            return queryset.filter(name__startswith='A')
        if self.value() == 'B':
            return queryset.filter(name__startswith='B')
        if self.value() == 'C':
            return queryset.filter(name__startswith='C')
        if self.value() == 'M':
            return queryset.filter(name__startswith='M')
        if self.value() == 'S':
            return queryset.filter(name__startswith='S')
        # return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['rating','name']
    # exclude = ['slug']
    # readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'rating_names', 'director','currency']
    list_editable = ['rating', 'director','currency']
    ordering = ['-rating']
    filter_horizontal = ['actors']
    list_per_page = 10
    actions = ['make_all_euro', 'make_all_rub', 'make_all_usd']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['currency', RatingFilter, NameFilter]

    @admin.display(ordering='rating', description='Отзывы челов')
    def rating_names(self, mov: Movie):
        if mov.rating < 50:
            return 'Low rating'
        if mov.rating < 70:
            return 'Normal rating'
        if mov.rating < 86:
            return 'Good'
        return 'Excellent'

    @admin.action(description='Установить валюту ЕВРО')
    def make_all_euro(self, request, qr: QuerySet):
        count_changes = qr.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_changes} полей'
        )

    @admin.action(description='Установить валюту РУБЛЬ')
    def make_all_rub(self, request, qr: QuerySet):
        count_changes = qr.update(currency=Movie.RUB)
        self.message_user(
            request,
            f'Было обновлено {count_changes} полей'
        )

    @admin.action(description='Установить валюту ДОЛЛАР')
    def make_all_usd(self, request, qr: QuerySet):
        count_changes = qr.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_changes} полей',

        )

# admin.site.register(Movie, MovieAdmin)
