from modeltranslation.translator import register, TranslationOptions
from .models import Category, Service

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')
