# Import Python test module and test classes
import unittest

from tests.test_python import *
from tests.test_slurm import *
from tests.test_system_pkgs import *
from tests.test_system_props import TestSystem, TestSystemStandard

# Run tests
if (__name__ == '__main__'):
    unittest.main(verbosity=2, catchbreak=True)
