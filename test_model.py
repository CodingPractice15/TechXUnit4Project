from tabnanny import check
import unittest
from TechXUnit4Project.model import * 

class TestModel(unittest.TestCase):

    def test_empty(self):
        # when the input field is empty.
        self.assertEquals(is_empty(""), True)
        # when the input field is not empty.
        self.assertEquals(is_empty("123f"), False)
        self.assertEquals(is_empty("123.@!FSgs"), False)
    
    def test_password_length(self):
        # when the type is not correct.
        self.assertRaises(TypeError, check_password_length, 123)

        # when the password lenght is not correct.
        self.assertEquals(check_password_length(""), True)
        self.assertEquals(check_password_length("12345"), True)
        self.assertEquals(check_password_length("abcde"), True)
        self.assertEquals(check_password_length("a432e"), True)
        # when the password lenght is as expected.
        self.assertEquals(check_password_length("a432efsfs"), False)
        self.assertEquals(check_password_length("!#$@gsFS"), False)
    
    def test_password_validation(self):
        # when the type is not correct and the value is not correct.
        self.assertRaises(TypeError, check_password_validation, 123)
        self.assertRaises(ValueError, check_password_validation, "12Fs")
        self.assertRaises(ValueError, check_password_validation, "3 gs ")
        self.assertRaises(ValueError, check_password_validation, "")
        
        # when the password is not validated.
        self.assertEquals(check_password_validation("fdsafdsfs"), True)
        self.assertEquals(check_password_validation("323131231"), True)
        self.assertEquals(check_password_validation("$@$@#$@$"), True)
        self.assertEquals(check_password_validation("5245gsgs"), True)
        self.assertEquals(check_password_validation("4567$%$^$"), True)
        self.assertEquals(check_password_validation("&*^*&GGHI"), True)
        self.assertEquals(check_password_validation("gyGYHGIhbhi"), True)
        # when password is validated.
        self.assertEquals(check_password_validation("hi12!@THERE"), False)
        self.assertEquals(check_password_validation("Hellow11!@sir"), False)

if __name__ == '__main__':
    unittest.main()