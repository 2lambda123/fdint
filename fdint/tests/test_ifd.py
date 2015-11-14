# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.

# This file was generated by `scripts/gen_test_ifd.py`.
# Do not edit this file directly, or your changes will be lost.
'''
Tests the `ifd` module.
'''
# Make sure we import the local package
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from fdint import ifd
import unittest
import numpy
import warnings
from fdint import fd

class Test_IFD(unittest.TestCase):

    def assertRTOL(self, a, b, RTOL):
        assert RTOL >= 0
        rerr = abs(a-b)/a
        if rerr > RTOL:
            self.fail('Outside of relative tolerance of {}: {}'
                      ''.format(RTOL, rerr))

    def assert_all_rtol(self, a, b, rtol):
        assert rtol >= 0
        a = numpy.array(a)
        b = numpy.array(b)
        rtol = numpy.array(rtol)
        rerr = abs(a-b)/a
        if (rerr > rtol).all():
            self.fail('Outside of relative tolerance of {}: {}'
                      ''.format(rtol, rerr))

    def test_ifd1h_1(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(-50.0)), -50.0, 1e-14)

    def test_vifd1h_1(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((-50.0,)))),
                             (-50.0,), (1e-14,))

    def test_ifd1h_2(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(-3.0)), -3.0, 1e-14)

    def test_vifd1h_2(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((-3.0,)))),
                             (-3.0,), (1e-14,))

    def test_ifd1h_3(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(-2.0)), -2.0, 1e-14)

    def test_vifd1h_3(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((-2.0,)))),
                             (-2.0,), (1e-14,))

    def test_ifd1h_4(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(-1.0)), -1.0, 1e-14)

    def test_vifd1h_4(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((-1.0,)))),
                             (-1.0,), (1e-14,))

    def test_ifd1h_5(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(0.0)), 0.0, 1e-14)

    def test_vifd1h_5(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((0.0,)))),
                             (0.0,), (1e-14,))

    def test_ifd1h_6(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(1.0)), 1.0, 1e-14)

    def test_vifd1h_6(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((1.0,)))),
                             (1.0,), (1e-14,))

    def test_ifd1h_7(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(4.0)), 4.0, 1e-14)

    def test_vifd1h_7(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((4.0,)))),
                             (4.0,), (1e-14,))

    def test_ifd1h_8(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(5.0)), 5.0, 1e-14)

    def test_vifd1h_8(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((5.0,)))),
                             (5.0,), (1e-14,))

    def test_ifd1h_9(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(7.0)), 7.0, 1e-14)

    def test_vifd1h_9(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((7.0,)))),
                             (7.0,), (1e-14,))

    def test_ifd1h_10(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(10.0)), 10.0, 1e-14)

    def test_vifd1h_10(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((10.0,)))),
                             (10.0,), (1e-14,))

    def test_ifd1h_11(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(15.0)), 15.0, 1e-14)

    def test_vifd1h_11(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((15.0,)))),
                             (15.0,), (1e-14,))

    def test_ifd1h_12(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(20.0)), 20.0, 1e-14)

    def test_vifd1h_12(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((20.0,)))),
                             (20.0,), (1e-14,))

    def test_ifd1h_13(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(30.0)), 30.0, 1e-14)

    def test_vifd1h_13(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((30.0,)))),
                             (30.0,), (1e-14,))

    def test_ifd1h_14(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(40.0)), 40.0, 1e-14)

    def test_vifd1h_14(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((40.0,)))),
                             (40.0,), (1e-14,))

    def test_ifd1h_15(self):
        self.assertRTOL(ifd.ifd1h(fd.fd1h(50.0)), 50.0, 1e-14)

    def test_vifd1h_15(self):
        self.assert_all_rtol(ifd.ifd1h(fd.fd1h(numpy.array((50.0,)))),
                             (50.0,), (1e-14,))

if __name__ == "__main__":
    unittest.main()