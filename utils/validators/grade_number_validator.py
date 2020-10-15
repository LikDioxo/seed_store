import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def grade_number_validator(grade_number: str):
    if not grade_number.isupper():
        raise ValidationError(
            _('All characters must be upper case in grade_number!'),
            params={'value': grade_number}
        )

    match = re.fullmatch(r'^\w{2,3}-\w{5,6}-[0-9]', grade_number)
    if match is None or int(grade_number[-1]) != len(grade_number[0:-1].replace('-', '')):
        raise ValidationError(
            _('Grade number does not fit the template!'),
            params={'value': grade_number}
        )

