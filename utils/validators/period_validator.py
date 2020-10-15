from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate(start, end):
    if end <= start:
        raise ValidationError(
            _("Expiration date can't be lower than breed date!")
        )
