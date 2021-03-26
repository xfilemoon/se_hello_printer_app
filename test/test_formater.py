from hello_world.formater import plain_text_upper_case
from hello_world.formater import format_to_xml
from hello_world.formater import plain_text
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_to_xml(self):
        name = 'Krysia'
        msg = 'Hello'
        result = format_to_xml(msg, name)
        self.assertEqual(
            result,
            b'<greetings><name>Krysia</name><msg>Hello</msg></greetings>'
            )

    def test_plain_text(self):
        name = 'Basia'
        msg = 'Hi'
        result = plain_text(msg, name)
        self.assertEqual(result, name + ' ' + msg)
