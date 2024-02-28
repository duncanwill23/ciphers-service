from django.test import TestCase
from .ciphers import caesar_encode
# Create your tests here.

class CipherTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = "hello"
        shift = 1
        expected = "ifmmp"
        result = caesar_encode(plain_text, shift)
        self.assertEqual(result, expected)

    def test_caesar_encoding_2(self):
        plain_text = 'winter'
        shift = 3
        expected = 'zlqwhu'
        result = caesar_encode(plain_text, shift)
        self.assertEqual(result, expected)