from django.contrib import admin
from django.apps import apps

# Register your models here.
for model in apps.get_app_config('blog').get_models():
    # if "auth" not in model.name:
    admin.site.register(model)