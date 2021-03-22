from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    """Inline owners"""
    model = Owner.flats.through
    raw_id_fields = ["owner"]
    extra = 1


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    """Flat admin representation"""
    search_fields = ["town", "address"]
    readonly_fields = ["created_at"]
    list_display = [
        "address", "price", "new_building",
        "construction_year", "town", "show_owner_phone"
    ]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ["liked", "owners"]
    inlines = [OwnerInline, ]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Owner admin representation"""
    raw_id_fields = ["flats"]


@admin.register(Complaint)
class ComplainAdmin(admin.ModelAdmin):
    """Complains admin representation"""
    raw_id_fields = ["user", "flat"]
