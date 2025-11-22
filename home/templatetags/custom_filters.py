from django import template
from babel import numbers

register = template.Library()

@register.filter()
def get(dictionary, value):
    return dictionary[value]

@register.filter()
def count(list_var):
    return list_var.count()

@register.filter()
def rupee(value):
    try:
        value = float(value)
        formatted = numbers.format_currency(value, 'INR', locale='en_IN')
        # formatted = f"₹{value:,.2f}"
        # formatted = formatted.replace(',', 'X').replace('X', ',')
        return formatted
    except (ValueError, TypeError):
        return value

@register.filter()
def multiply(val1, val2):
    return val1 * val2