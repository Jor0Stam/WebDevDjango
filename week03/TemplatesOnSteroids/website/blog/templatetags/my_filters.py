from django import template
from markdown import markdown

register = template.Library()

@register.filter(name='do_markdown')
def do_markdown(value):
    return markdown(value)
