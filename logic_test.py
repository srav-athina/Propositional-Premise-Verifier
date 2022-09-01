import unittest
from logic import is_valid

class TestLogic(unittest.TestCase):

    def test_invalid(self):
        self.assertFalse(is_valid(premises={"P→Q", "Q"}, conclusion="P"))
        self.assertFalse(is_valid(premises={"P→Q", "Q→(P∧R)", "R"}, conclusion="P"))

    def test_valid(self):
        self.assertTrue(is_valid(premises={"P⇔Q", "Q"}, conclusion="P"))


    def test_lecture_example_invalid(self):
        self.assertFalse(is_valid(premises={"P→(Q∨¬R)", "Q→(P∧R)"}, conclusion="P→R"))

    def test_many_propositions_valid(self):
        self.assertTrue(is_valid(premises={"(M∧¬B)→J","(F∨S)→M", "B→T", "F→¬T", "F" }, conclusion="J"))

if __name__ == '__main__':
    unittest.main()
