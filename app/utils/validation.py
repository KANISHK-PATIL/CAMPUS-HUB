import re
from urllib.parse import urlparse

def clean(value): return (value or '').strip()
def valid_email(value): return bool(re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', value)) and len(value)<=120
def password_ok(value): return isinstance(value,str) and len(value)>=8 and len(value)<=128
def valid_url(value):
    try: return urlparse(value).scheme in {'http','https'} and bool(urlparse(value).netloc) and len(value)<=500
    except Exception: return False

def limited(value, max_len, required=True):
    value=clean(value)
    if required and not value: raise ValueError('This field is required.')
    if len(value)>max_len: raise ValueError(f'Maximum length is {max_len} characters.')
    return value
