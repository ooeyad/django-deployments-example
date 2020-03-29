from django import template

register = template.Library()

@register.filter
def cut_replace(value,arg):
    """
        This will replace any arg from value
    """
    return value + " and "+ arg
