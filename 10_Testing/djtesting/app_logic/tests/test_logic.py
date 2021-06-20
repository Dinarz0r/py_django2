from django.test import SimpleTestCase
from app_logic.helpers import check_access_by_age, open_clock, text_connection


class BusinessLogicTest(SimpleTestCase):
    def test_access_denied(self):
        for i in range(18):
            self.assertFalse(check_access_by_age(i))

    def test_access_18_and_over_age(self):
        for i in range(18, 140):
            self.assertTrue(check_access_by_age(i))

    def test_open_clock(self):
        for i in range(0, 8):
            self.assertFalse(open_clock(i))
        for i in range(8, 13):
            self.assertTrue(open_clock(i))
        for i in range(14, 21):
            self.assertTrue(open_clock(i))
        self.assertEqual(open_clock(13), False)

    def test_text_connection(self):
        text = text_connection('ab', 'cd')
        self.assertEqual(text, 'abcd')
