# Generated by Django 3.1.6 on 2021-03-04 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.person'),
        ),
        migrations.AlterField(
            model_name='postpicture',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='blog.post'),
        ),
    ]
