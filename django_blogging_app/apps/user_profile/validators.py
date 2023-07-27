from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Must contain only letters")

# ToDo: more custom validators
