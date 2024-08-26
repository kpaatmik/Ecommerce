from django import template
from . import gettotal
register=template.Library()
@register.simple_tag(name='tax')
def tax(a):
    total_tax=a*0.18
    
    return total_tax
            
    