# ref: https://stackoverflow.com/questions/4651172/reference-list-item-by-index-within-django-template/29664945
# ref: https://docs.djangoproject.com/en/dev/howto/custom-template-tags/

from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library() # "To be a valid tag library, the module must contain a module-level variable named register that is a template.Library instance, in which all the tags and filters are registered."

@register.simple_tag
def define(indexable, i, attr): # define variable from template: usage {% define number_models forloop.counter0 "numbermodels" as n_models %}
  return int(getattr(indexable[i], attr))

@register.simple_tag
def define_single_var(var): # define variable from template: usage {% define number_models forloop.counter0 "numbermodels" as n_models %}
  return int(var)

@register.filter
def index(indexable, i): # get specific object in a list, passing it's index, usage: {{ number_models | index: forloop.counter0 }}
    return indexable[i]

@register.filter
def getattrfilterDict(dict, key): # get value of a dictionary attribute
    try:
        return dict.get(key, None) # return None if not exists
    except:
        raise

@register.filter(name='getattr')
def getattrfilter(o, attr): # get value of a object attribute, usage: {{ number_models | index: forloop.counter0 | get_attr:numbermodels }}
    try:
        return getattr(o, attr)
    except:
        raise

@register.simple_tag
def filter_range(start, end): # range filter to use in a for loop
    limits = range(start, end)
    return limits

@register.simple_tag
def define_int(x, y): # sum to variables
    return int(x+y)

# passing values from django template to javascript in a safety way: https://stackoverflow.com/questions/298772/django-template-variables-and-javascript
@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))