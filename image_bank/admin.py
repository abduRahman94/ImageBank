from django.contrib import admin
from .models import Image, Payment, ImageBankUser, Tag, Licence
from django import forms
# Register your models here.


class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ['name', 'auteur', 'description', 'image', 'licence', 'status', 'payment_required', 'price', 'format', 'taille']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class ImageModelAdmin(admin.ModelAdmin):
    form = ImageForm

admin.site.register(Image, ImageModelAdmin)
admin.site.register(Payment)
admin.site.register(ImageBankUser)
admin.site.register(Tag)
admin.site.register(Licence)