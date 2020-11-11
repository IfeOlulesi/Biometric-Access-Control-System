from django import forms
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


class CollectFPrint(forms.Form):
  finger_img = forms.ImageField()
  # file_data = {'img': SimpleUploadedFile('test.png', <file data>)}
  # form = ImageForm({}, file_data)