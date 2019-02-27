from django import template

register = template.Library()


@register.filter
def to_eng(value):
    return value.replace("es", "en")


@register.filter
def to_spa(value):
    return value.replace("en", "es")