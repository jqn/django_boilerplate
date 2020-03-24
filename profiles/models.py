from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    FIRST = '1st'
    SECOND = '2nd'
    THIRD = '3rd'
    FOURTH = '4th'
    YEAR_CHOICES = (
        (FIRST, 'First Year'),
        (SECOND, 'Second Year'),
        (THIRD, 'Third Year'),
        (FOURTH, 'Fourth Year'),
    )
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, default=FIRST)

    TUTOR = 'tutor'
    TUTEE = 'tutee'
    BOTH = 'tutor_tutee'
    USER_CHOICES = (
        (FIRST, 'Tutor'),
        (SECOND, 'Tutee'),
        (THIRD, 'Tutor and Tutee'),
    )
    user_type = models.CharField(
        max_length=15, choices=USER_CHOICES, default=TUTOR)
    subjects = models.CharField(max_length=500, default="")
    bio = models.TextField(default=' ')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

