from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cust out all values of arge from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
