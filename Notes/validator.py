from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_first_name_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError(
            _("Your name must start with a letter!"),
            code="invalid_first_character",
        )

def validate_last_name_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError(
            _("Your name must start with a letter!"),
            code="invalid_first_character",
        )
        

def validate_name(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")