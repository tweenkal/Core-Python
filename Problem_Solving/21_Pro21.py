from pkgutil import resolve_name

from django.utils.functional import empty
from setuptools import find_packages

a = {1,2,3,4,5,6}
b = {2,3,5,2,8,9}

print("The union is:",a | b)
print("The intersection is:",a & b)
print("The difference is:",a - b)
print("The symmetric difference:",a ^ b)


