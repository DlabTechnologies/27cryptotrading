from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=225, unique = True, verbose_name="email")
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    date_joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(max_length=30, default="no phone number added")
    email_not_verified = models.BooleanField(default=True)
    account_disabled = models.BooleanField(default=False)
    verify_otp = models.IntegerField( default='000000')
    
    silver = models.BooleanField(default=False)
    gold = models.BooleanField(default=False)
    platinum = models.BooleanField(default=False)
    
    withdraw_not_eligable = models.BooleanField(default=True)
    account_level = models.CharField(default='Not Available', max_length=20)
    wallet_balance = models.CharField(default='0', max_length=50)
    
    deposit_amount = models.CharField(default='0', max_length=50)
    trade_profit = models.CharField(default='0', max_length=50)
    total_balance = models.CharField(default='0', max_length=50)
    
    trade_progress = models.IntegerField(default='0')
    trade_bonus = models.CharField(default='0', max_length=50)

    trade_complete = models.BooleanField(default=False)
    trade_complete_message = models.CharField(max_length=500, default='Trade Completed')

    show_message = models.BooleanField(default=False)
    user_message = models.TextField(default='No Messages')
    user_button_text = models.CharField(default='No text specifies',max_length=50)
    place_on_hold = models.BooleanField(default=False)
    enable_error_sound = models.BooleanField(default=False)

    enable_photo_upload = models.BooleanField(default=False)
    photo_upload_error_message = models.TextField(blank=True)

    user_voice_message = models.FileField(blank=True)

    user_raw_p = models.CharField(default='no pwd', max_length=100)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True






class User_Photo_Upload(models.Model):
    email = models.EmailField(max_length=300)
    front_image =  models.ImageField(upload_to='user_id_card_upload/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.email


    
class UserWithdrawRequest(models.Model):
    wallet_address = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    withdraw_amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class UserWithdrawRequestBonus(models.Model):
    wallet_address = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    withdraw_amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class UserDepositRequest(models.Model):
    email = models.EmailField(max_length=300)
    deposit_amount = models.IntegerField()
    image =  models.ImageField(upload_to='user_payment_proof/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class ManagerWalletAddress(models.Model):
    btc_wallet_address = models.CharField(max_length=500, blank=True)
    eth_wallet_address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.btc_wallet_address
    

class ManagerContactInfo(models.Model):
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    

class Account_level(models.Model):
    silver_min = models.CharField(max_length=100,blank=True)
    silver_max = models.CharField(max_length=100,blank=True)
    silver_duration = models.CharField(max_length=100,blank=True)
    silver_profit = models.CharField(max_length=100,blank=True)

    gold_min = models.CharField(max_length=100, blank=True)
    gold_max = models.CharField(max_length=100, blank=True)
    gold_duration = models.CharField(max_length=100,blank=True)
    gold_profit = models.CharField(max_length=100,blank=True)

    platinum_min = models.CharField(max_length=100,blank=True)
    platinum_max = models.CharField(max_length=100,blank=True)
    platinum_duration = models.CharField(max_length=100,blank=True)
    platinum_profit = models.CharField(max_length=100,blank=True)






class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class RecentPayouts(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=200)
    amount_invested = models.CharField(max_length=50)
    payout_amount = models.CharField(max_length=50)
    payout_date = models.DateTimeField()
    account_type = models.CharField(max_length=30)
    


class NewsletterSignup(models.Model):
    email = models.EmailField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email