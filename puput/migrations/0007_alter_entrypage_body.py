# Generated by Django 3.2.3 on 2023-05-12 11:34

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('puput', '0006_entrypage_markdown_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrypage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='body'),
        ),
    ]
