from django import template
from core.models import *

register = template.Library()

@register.filter
def arrange(value):
	try:
		wishlist = value.objects.filter(name='Wishlist')
	except:
		wishlist = []
	return wishlist + list(value.objects.filter(~Q(name='Wishlist')).order_by('last_change'))