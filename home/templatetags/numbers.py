from django import template

register  = template.Library()

def format_num(value):
    return f"{value:,}"

register.filter('format_num',format_num)
