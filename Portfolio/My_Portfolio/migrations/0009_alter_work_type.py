# Generated by Django 4.1.7 on 2023-06-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("My_Portfolio", "0008_rename_img1_work_gif_rename_img2_work_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="work",
            name="type",
            field=models.CharField(
                choices=[["Commercial", "Commercial"], ["Personal", "Personal"]],
                max_length=100,
                null=True,
            ),
        ),
    ]
