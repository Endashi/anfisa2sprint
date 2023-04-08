from django.contrib import admin

from .models import Category
from .models import IceCream
from .models import Wrapper
from .models import Topping

# admin.site.register(Category)
# admin.site.register(IceCream)
admin.site.register(Wrapper)
admin.site.register(Topping)


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    empty_value_display = 'Не задано'

    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.empty_value_display = 'Не задано'
