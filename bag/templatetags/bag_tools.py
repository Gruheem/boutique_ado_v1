from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    '''A template tag to calculate the subtotal for an item in the bag'''
    return price * quantity