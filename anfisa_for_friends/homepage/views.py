from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Для переноса длинной строки замыкаем её в скобки.
    # Будьте внимательны.
    ice_cream_list = IceCream.objects.values(
        'title', 'description'
    ).filter(
        Q(is_on_main=True)
        & Q(is_published=True)
        | Q(title__contains='пломбир')
        & Q(is_published=True)
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)