import unittest

from .utils import check_pkg_exists


class TestSystemPkgs(unittest.TestCase):
    def test_curl(self):
        # Checks for successful installation of CURL
        self.assertTrue(check_pkg_exists('curl'))

    def test_dos2unix(self):
        # Checks for successful installation of dos2unix
        self.assertTrue(check_pkg_exists('dos2unix'))

    def test_gcc(self):
        # Checks for successful installation of gcc compiler
        self.assertTrue(check_pkg_exists('gcc'))

    def test_gdb(self):
        # Checks for successful installation of GDB
        self.assertTrue(check_pkg_exists('gdb'))

    def test_git(self):
        # Checks for successful installation of Git
        self.assertTrue(check_pkg_exists('git'))

    def test_gpp(self):
        # Checks for successful installation of g++ compiler
        self.assertTrue(check_pkg_exists('g++'))

    def test_graphviz(self):
        # Checks for successful installation of Graphviz
        self.assertTrue(check_pkg_exists('dot'))

    def test_htop(self):
        # Checks for successful installation of htop
        self.assertTrue(check_pkg_exists('htop'))

    def test_lshw(self):
        # Checks for successful installation of lshw
        self.assertTrue(check_pkg_exists('lshw'))

    def test_nano(self):
        # Checks for successful installation of nano
        self.assertTrue(check_pkg_exists('nano'))

    def test_openssl(self):
        # Checks for successful installation of openssl
        self.assertTrue(check_pkg_exists('openssl'))

    def test_tree(self):
        # Checks for successful installation of tree
        self.assertTrue(check_pkg_exists('tree'))

    def test_vim(self):
        # Checks for successful installation of vim
        self.assertTrue(check_pkg_exists('vim'))

    def test_wget(self):
        # Checks for successful installation of wget
        self.assertTrue(check_pkg_exists('wget'))

    def test_zip(self):
        # Checks for successful installation of zip
        self.assertTrue(check_pkg_exists('zip'))
