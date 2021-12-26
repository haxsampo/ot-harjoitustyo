import unittest
from sprites.button import Button

class StubFuncHold:
    def __init__(self):
        pass

    def function_for_testing(self, dic):
        dic['butt'].button_value = dic['x_value'] + dic['y_value']

class TestButton(unittest.TestCase):

    def test_run_func(self):
        """
        Test that the given function is fired correctly
        """
        stubber = StubFuncHold()
        butt = Button(5, 5, "70x70_button.png", 10, 10, stubber.function_for_testing, "tester")
        dic = {'x_value':120, 'y_value':30, 'butt':butt}
        butt.run_func(dic)
        self.assertEqual(butt.button_value, 150)
