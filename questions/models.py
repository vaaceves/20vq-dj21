from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now


# media files directory organization function
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}/'.format(
        instance.slug,
        filename
    )


# # USER ABSTRACT MODEL
# # We extend the default django user model, by using AbstractUser class
# class User(AbstractUser):
#   # This are the types of users that Graham Sports have, we use a tupple because it cant be modified one its declared
#     LANGUAGE_CHOICES = (
#         (0, 'SPA'),
#         (1, 'ENG'),
#     )
#     # Extra Field we use to indicate the type of user, using as options the items declared in the previous tupple
#     language = models.PositiveSmallIntegerField(choices=LANGUAGE_CHOICES, null=True, default=1)


# Create your models here.
class Topic(models.Model):
    # SPANISH
    name_spa = models.CharField(max_length=149, default='Topic')
    cover_spa = models.ImageField(upload_to=user_directory_path, null=True)
    # ENGLISH
    name_eng = models.CharField(max_length=149, default='Topic')
    cover_eng = models.ImageField(upload_to=user_directory_path, null=True)
    # COMMON
    slug = models.SlugField(max_length=149)

    def _get_unique_slug(self):
        slug_string = self.name_eng
        slug = slugify(slug_string)
        unique_slug = slug
        num = 1
        while Topic.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_eng


class Question(models.Model):
    # SPANISH
    name_spa = models.CharField(max_length=149, default='Question')
    video_spa = models.CharField(max_length=149, default='0000000')
    pdf_spa = models.FileField(upload_to=user_directory_path, null=True)
    pdf_link_spa = models.URLField(max_length=349, default='https://gls-demo-f4707.firebaseapp.com/DISCUSSIONGUIDES/DISC01/Craig_Groeschel.pdf')
    issuu_spa = models.URLField(max_length=149, default='https://e.issuu.com/anonymous-embed.html?u=onelmedia&d=craig_groeschel')
    # ENGLISH
    name_eng = models.CharField(max_length=149, default='Question')
    video_eng = models.CharField(max_length=149, default='0000000')
    # COMMON
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=user_directory_path, null=True)
    banner = models.ImageField(upload_to=user_directory_path, null=True)
    speaker = models.CharField(max_length=149, default='Speaker')
    slug = models.SlugField(max_length=149)

    def _get_unique_slug(self):
        slug_string = self.speaker
        slug = slugify(slug_string)
        unique_slug = slug
        num = 1
        while Question.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.speaker
