import unittest


class TestMyPackage(unittest.TestCase):

    @staticmethod
    def _get_target_class():
        from mypackage import MyPackage

        return MyPackage

    def test_spam(self):
        cls = self._get_target_class()
        assert cls().spam() == 'eggs'
