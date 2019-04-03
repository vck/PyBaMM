#
# Tests for the lithium-ion models
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import pybamm
import tests
import numpy as np
import unittest


class TestSPM(unittest.TestCase):
    def test_basic_processing(self):
        model = pybamm.lithium_ion.SPM()
        modeltest = tests.StandardModelTest(model)
        modeltest.test_all()

    def test_surface_concentration(self):
        model = pybamm.lithium_ion.SPM()
        modeltest = tests.StandardModelTest(model)
        modeltest.test_all()
        T, Y = modeltest.solver.t, modeltest.solver.y

        # check surface concentration decreases in negative particle and
        # increases in positive particle for discharge
        np.testing.assert_array_less(
            model.variables["Negative particle surface concentration"].evaluate(T, Y)[
                1:
            ],
            model.variables["Negative particle surface concentration"].evaluate(T, Y)[
                :-1
            ],
        )
        np.testing.assert_array_less(
            model.variables["Positive particle surface concentration"].evaluate(T, Y)[
                :-1
            ],
            model.variables["Positive particle surface concentration"].evaluate(T, Y)[
                1:
            ],
        )
        # test that surface concentrations are all positive
        np.testing.assert_array_less(
            0, model.variables["Negative particle surface concentration"].evaluate(T, Y)
        )


class TestSPMe(unittest.TestCase):
    def test_basic_processing(self):
        model = pybamm.lithium_ion.SPMe()
        modeltest = tests.StandardModelTest(model)
        modeltest.test_all()


class TestDFN(unittest.TestCase):
    def test_basic_processing(self):
        model = pybamm.lithium_ion.DFN()
        var = pybamm.standard_spatial_vars
        self.default_var_pts = {
            var.x_n: 3,
            var.x_s: 3,
            var.x_p: 3,
            var.r_n: 1,
            var.r_p: 1,
        }

        modeltest = tests.StandardModelTest(model)
        modeltest.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()
