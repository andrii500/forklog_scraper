from django import template

register = template.Library()


@register.filter
def custom_split(value, splitter):
    return value.split(splitter)[0]
