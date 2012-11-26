from django import template
#from django.db import models

register = template.Library()

@register.filter("arrange", is_safe=True)
def arrange(value): return value
'''	try:
		try:
			wishlist = value.objects.filter(name='Wishlist')
		except:
			wishlist = []
		return wishlist + list(value.objects.filter(~Q(name='Wishlist')).order_by('last_change'))
    except (ValueError, TypeError):
        return value # Fail silently.'''