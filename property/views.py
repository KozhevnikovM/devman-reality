from django.shortcuts import render


from .models import Flat


def format_price(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def show_flats(request):
    town = request.GET.get("town")
    max_price = format_price(request.GET.get("max_price"))
    min_price = format_price(request.GET.get("min_price"))
    new_building = request.GET.get("new_building")
    
    possible_filters = {
        'town': town,
        'price__gt': min_price,
        'price__lt': max_price,
        'new_building': new_building
    }

    current_filter = {
        param: choice for param, choice in possible_filters.items() if choice
    }

    flats = Flat.objects.filter(**current_filter)
    towns = Flat.objects.values_list(
        "town", flat=True).distinct().order_by("town")
    
    return render(
        request,
        "flats_list.html",
        {
            "flats": flats[:10],
            "towns": towns,
            "active_town": town,
            "max_price": max_price,
            "min_price": min_price,
            "new_building": new_building
        }
    )
