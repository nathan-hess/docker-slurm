import sys
import unittest


class TestPython(unittest.TestCase):
    def test_python_version(self):
        # Checks that Python 3 is installed and that version is at least 3.8
        self.assertEqual(sys.version_info.major, 3)
        self.assertGreaterEqual(sys.version_info.minor, 8)

    def test_pip_version(self):
        # Checks that pip version is at least 22.0
        import pip
        pip_version = pip.__version__.split('.')

        self.assertGreaterEqual(int(pip_version[0]), 22)
