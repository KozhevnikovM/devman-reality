# Generated by Django 2.2.4 on 2021-03-19 14:12

from django.db import migrations
import phonenumbers


def format_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        except phonenumbers.NumberParseException:
            continue
        if phonenumbers.is_valid_number(number):
            flat.owner_pure_phone = phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            flat.save()

def backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(format_phones, backward)
    ]
