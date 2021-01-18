# Generated by Django 3.1.5 on 2021-01-17 21:18

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('region', models.CharField(choices=[('XV', 'Arica y Parinacota'), ('I', 'Tarapacá'), ('II', 'Antofagasta'), ('III', 'Atacama'), ('IV', 'Coquimbo'), ('V', 'Valparaíso'), ('RM', 'Santiago'), ('VI', 'Libertador General Bernardo Ohiggins'), ('VII', 'Maule'), ('XVI', 'Ñuble'), ('VIII', 'Biobío'), ('IX', 'La Araucanía'), ('XIV', 'Los Ríos'), ('X', 'Los lagos'), ('XI', 'Aysen'), ('XII', 'Magallanes y Antártica')], max_length=40)),
                ('instagram', models.CharField(max_length=50, null=True)),
                ('portafolio', models.URLField()),
                ('rutaImagen', models.FileField(null=True, upload_to='')),
                ('idioma', multiselectfield.db.fields.MultiSelectField(choices=[('es', 'Español'), ('en', 'Inglés'), ('de', 'Alemán'), ('fr', 'Francés'), ('pt', 'Portugués'), ('ru', 'Ruso')], max_length=17, null=True)),
                ('categoriasEspecialidad', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Matrimonio'), (2, 'Fiesta'), (3, 'Eventos Musicales'), (4, 'Eventos Deportivos'), (5, 'Mascota'), (6, 'Fotografía de producto'), (7, 'Fotografía aérea')], max_length=13, null=True)),
                ('disponibilidad', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Full Time'), (2, 'Part Time'), (3, 'Casual'), (4, 'Fin de Semanas'), (8, 'Festivos'), (5, 'Mañanas'), (6, 'Tardes'), (7, 'Noches')], max_length=15, null=True)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.person'),
        ),
    ]
