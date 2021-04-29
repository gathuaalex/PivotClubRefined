from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from .models import Profile

def member_profile(sender, instance, created,**kwargs):
    if created:
        group = Group.objects.get(name='Members')
        instance.groups.add(group)

        Profile.objects.create(
                user=instance,
                name=instance.username,
            )

post_save.connect(member_profile,sender=User)

def update_user_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated!')

post_save.connect(update_user_profile,sender=User)