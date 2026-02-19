from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services', verbose_name=_("Category"))
    title = models.CharField(_("Title"), max_length=200)
    short_description = models.TextField(_("Short Description"), blank=True)
    description = models.TextField(_("Full Description"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title
