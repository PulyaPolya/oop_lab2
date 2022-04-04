from func import get_full_name
from survey import Survey
import unittest
'''
class NamesTest(unittest.TestCase):
    def test_first_last(self):
        formatted = get_full_name('polina', 'kozarovitskaya')
        self.assertEqual(formatted, 'Polina Kozarovitskaya')
    def test_middle(self):
        formatted = get_full_name(name = 'polina', second = 'best', last = 'kozarovitskaya')
        self.assertEqual(formatted, 'Polina Best Kozarovitskaya')
'''
class SurveyTest(unittest.TestCase):
    def setUp(self):
        question = 'language'
        self.my_survey = Survey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_save_resp(self):

        for response in self.responses:
            self.my_survey.store_resp(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.respones)
unittest.main()