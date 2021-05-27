from django import template

register = template.Library()


@register.filter
def percentage(value1, value2=100):
    try:
        a = int(value1) / int(value2) * 100
    except:
        a = 0
    return a
