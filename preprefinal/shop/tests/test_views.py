from django.test import TestCase, Client
from django.urls import reverse
from cart.views import cart_detail, cart_remove, cart_add
import json


