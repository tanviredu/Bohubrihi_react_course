# Generated by Django 4.1.1 on 2022-09-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("APP_LEARNING", "0002_alter_book_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(blank=True, upload_to="cover/"),
        ),
        migrations.AddField(
            model_name="book",
            name="descrption",
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name="book",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name="book",
            name="published",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]