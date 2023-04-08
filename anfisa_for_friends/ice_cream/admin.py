from django.contrib import admin

from .models import Category
from .models import IceCream
from .models import Wrapper
from .models import Topping

admin.site.register(Category)
admin.site.register(IceCream)
admin.site.register(Wrapper)
admin.site.register(Topping)
