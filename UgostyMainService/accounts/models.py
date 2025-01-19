from django.db import models
from django.contrib.auth.models import User

class DonationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=120)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='buns/', null=True, blank=True)
    status_banned = models.BooleanField(default=False)


    buns = models.ManyToManyField('Buns', through='DonationBunQuantity', related_name='donation_profiles')

    telegram_profile = models.OneToOneField('TelegramProfile', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'donation_profiles'

    def __str__(self):
        return self.user.username


class TelegramProfile(models.Model):
    id_telegram = models.CharField(max_length=120,unique=True)
    chat_id = models.IntegerField() # айди чата с ботом(для отправки сообщения)

    class Meta:
        db_table = 'telegram_profiles'


    def __str__(self):
        return f"{self.id_telegram}"

class TelegramPostsWithBot(models.Model):
    thumbnail = models.TextField(null=True, blank=True)
    text = models.TextField()
    button_text = models.TextField(blank=True)
    button_link = models.TextField(blank=True)


class Payment(models.Model):
    donation_profile = models.ForeignKey(DonationProfile, on_delete=models.CASCADE, related_name='payments')
    payment_id = models.CharField(max_length=120)
    status = models.CharField(max_length=50)
    social_media = models.CharField(max_length=50)
    donation_message = models.TextField()
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    payment_amount = models.IntegerField(blank=True,default=0)
    type_payout = models.BooleanField(default=False, null=True)



    class Meta:
        db_table = 'payments'

    def __str__(self):
        return (f'Донат от {self.social_media} '
                f'Автору {self.donation_profile.nickname} '
                f'Статус {self.status} '
                f'Дата создания {self.created_at}')


class Buns(models.Model):
    name = models.CharField(max_length=120)
    img_buns = models.ImageField(upload_to='buns')
    price = models.IntegerField(default=0)
    created_at = models.CharField(max_length=50)
    color_treats = models.TextField(max_length=120)

    class Meta:
        db_table = 'Buns'


    def __str__(self):
        return f'{self.name} по цене {self.price}'



class DonationBunQuantity(models.Model):
    donation_profile = models.ForeignKey(DonationProfile, on_delete=models.CASCADE)
    bun = models.ForeignKey(Buns, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'donation_buns'
        unique_together = ('donation_profile', 'bun')

    def __str__(self):
        return f'{self.quantity} x {self.bun.name} для {self.donation_profile.nickname}'


