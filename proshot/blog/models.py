from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
    
LENGUAGES_PERSON = (
  ('es', 'Español'),
  ('en', 'Inglés'),
  ('de', 'Alemán'),
  ('fr', 'Francés'),
  ('pt', 'Portugués'),
  ('ru', 'Ruso'),
)

ESPECIALIDAD_CATEGORY =(
  (1,'Matrimonio'),
  (2,'Fiesta'),
  (3,'Eventos Musicales'),
  (4,'Eventos Deportivos'),
  (5,'Mascota'),
  (6,'Fotografía de producto'),
  (7,'Fotografía aérea'),
)

DISPONIBILIDAD_CATEGORY =(
  (1, 'Full Time'),
  (2, 'Part Time'),
  (3, 'Casual'),
  (4, 'Fin de Semanas'),
  (8, 'Festivos'),
  (5, 'Mañanas'),
  (6, 'Tardes'),
  (7, 'Noches'),

)

REGION_CHILE = [
  ('XV', 'Arica y Parinacota'),
  ('I', 'Tarapacá'),
  ('II', 'Antofagasta'),
  ('III', 'Atacama'),
  ('IV', 'Coquimbo'),
  ('V', 'Valparaíso'),
  ('RM', 'Santiago'),
  ('VI', 'Libertador General Bernardo Ohiggins'),
  ('VII', 'Maule'),
  ('XVI', 'Ñuble'),
  ('VIII', 'Biobío'),
  ('IX', 'La Araucanía'),
  ('XIV', 'Los Ríos'),
  ('X', 'Los lagos'),
  ('XI', 'Aysen'),
  ('XII', 'Magallanes y Antártica')
]

class Person(models.Model):
    #nombre y apellidos
    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=30)
    #region 
    region = models.CharField(max_length=40, choices=REGION_CHILE)
    #instagram
    instagram = models.CharField(max_length=50, null= True)
    #url con el portafolio
    portafolio = models.URLField()
    #insertar 3 imagenes que representen al fotografo (opcional)
    rutaImagen = models.FileField(null = True)
    #idioma que domina el fotografo
    idioma = MultiSelectField(choices=LENGUAGES_PERSON,  null=True)
    #categoria de las cuales maneja en fotografia
    categoriasEspecialidad = MultiSelectField(choices = ESPECIALIDAD_CATEGORY,  null=True)
    #disponibilidad 
    disponibilidad = MultiSelectField(choices = DISPONIBILIDAD_CATEGORY,  null=True)
    #status se refiere a que si está dentro del sistema o no 
    status = models.IntegerField()
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
      return sef.title
#    
#    def get_absolute_url(self):
#        return reverse('blog_post_detail', args=[self.slug])#
#
#    def save(self, *args, **kwargs):
#        if not self.slug:
#            self.slug = slugify(self.title)
#        super(Post, self).save(*args, **kwargs)
#        
#    class Meta:
#        ordering = ['created_on']
#        # acá me sale error 
#        def __unicode__(self):
#            return self.title

class PostPicture(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.post.title