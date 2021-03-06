from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, UserWithdrawRequest, UserWithdrawRequestBonus, NewsletterSignup, ManagerWalletAddress, UserDepositRequest, Account_level, ManagerContactInfo, ContactForm, RecentPayouts, User_Photo_Upload
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    

   

    



    list_display = ('email','first_name','last_name','date_joined','is_staff','is_superuser','is_admin','account_level','deposit_amount',
    'trade_progress','trade_profit', 'profile_image','trade_complete','trade_complete_message','trade_bonus','phone','verify_otp', 'email_not_verified','withdraw_not_eligable','silver','gold','platinum','show_message','user_message','user_button_text','place_on_hold','enable_error_sound','enable_photo_upload','photo_upload_error_message','user_voice_message')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    ordering = ('email',)
    filter_horizontal =()
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields':('email','is_staff','is_superuser','is_admin','password')}),
        ('Personal info',{'fields':('first_name','last_name','account_level','deposit_amount',
    'trade_progress','trade_profit','profile_image','trade_complete','trade_complete_message','trade_bonus','phone','verify_otp','email_not_verified','withdraw_not_eligable','silver','gold','platinum','show_message','user_message','user_button_text','place_on_hold','enable_error_sound','enable_photo_upload','photo_upload_error_message','user_voice_message')}),
        
       
    )
     
    add_fieldsets = (
        (None, {'fields':('email','is_staff','is_superuser','is_admin','password1','password2')}),
        ('Personal info',{'fields':('first_name','last_name','account_level','deposit_amount',
    'trade_progress','trade_profit','profile_image', 'trade_complete','trade_complete_message','trade_bonus','phone','verify_otp','email_not_verified','withdraw_not_eligable','silver','gold','platinum','show_message','user_message','user_button_text','place_on_hold','enable_error_sound','enable_photo_upload','photo_upload_error_message','user_voice_message')}),
        
       
    )



class UserWithdrawRequestAdmin(admin.ModelAdmin):
    list_display = ('wallet_address', 'email','withdraw_amount','time','confirmed')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']

class UserWithdrawRequestBonusAdmin(admin.ModelAdmin):
    list_display = ('wallet_address', 'email','withdraw_amount','time','confirmed')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']

class UserDepositRequestAdmin(admin.ModelAdmin):
    list_display = ( 'email','deposit_amount','image','time','confirmed')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']   

class ManagerWalletAddressAdmin(admin.ModelAdmin):
    list_display = ('btc_wallet_address','eth_wallet_address')
    list_filter = ('btc_wallet_address','eth_wallet_address')
    search_fields = ['btc_wallet_address','eth_wallet_address']
    


class Account_levelAdmin(admin.ModelAdmin):
    list_display = ('silver_min','silver_max','silver_duration','silver_profit','gold_min','gold_max','gold_duration','gold_profit','platinum_min','platinum_max','platinum_duration','platinum_profit')


class ManagerContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email','phone')

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message','time')


class RecentPayoutsAdmin(admin.ModelAdmin):
    list_display = ('name','country','amount_invested','payout_amount','payout_date','account_type')


class User_Photo_UploadAdmin(admin.ModelAdmin):
    list_display = ( 'email','front_image','time')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']   

class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')

admin.site.register(User, UserAdmin)
admin.site.register(UserWithdrawRequest, UserWithdrawRequestAdmin)
admin.site.register(UserWithdrawRequestBonus, UserWithdrawRequestBonusAdmin)
admin.site.register(UserDepositRequest, UserDepositRequestAdmin)
admin.site.register(ManagerWalletAddress, ManagerWalletAddressAdmin)
admin.site.register(Account_level, Account_levelAdmin)
admin.site.register(ManagerContactInfo, ManagerContactInfoAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(RecentPayouts, RecentPayoutsAdmin)
admin.site.register(User_Photo_Upload, User_Photo_UploadAdmin)
admin.site.register(NewsletterSignup, NewsletterSignupAdmin)


 
    