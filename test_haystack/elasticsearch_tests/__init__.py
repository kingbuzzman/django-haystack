import unittest


def load_tests(loader, standard_tests, pattern):
    raise unittest.SkipTest("'elasticsearch>=1.0.0,<2.0.0' not installed.")
