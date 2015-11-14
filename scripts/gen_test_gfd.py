# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
'''
Uses numerical integration to calculate accurate values to test against.

This should only be run after `python setup.py build_ext --inplace`.
'''

import os
import sys
import fdint
tests_dir = os.path.join(os.path.dirname(__file__), '../fdint/tests/')

import warnings
import numpy
from numpy import exp, sqrt
from scipy.integrate import quad

def quad_gfdk(k, phi, beta):
    def func(x):
        return (x)**(k)*sqrt(1+beta*x/2.)/(1.+exp(x-phi))
    r = quad(func, 0, numpy.inf,epsabs=1e-300,epsrel=1e-13,limit=100)
    return r[0], r[1]

def get_assertRTOL2(f, x, b, y, rtol):
    return ('            self.assertRTOL({}({}, {}),\n'
            '        '
            '                   '
            ' {:.17e},\n'
            '        '
            '                   '
            ' {:.0e})\n'
            ''.format(f, x, b, val, rtol))

def get_assert_all_rtol2(f, x, b, y, rtol):
    return ('            '
            'self.assert_all_rtol({}(numpy.array(({},)),\n'
            '            '
            '                               '
            'numpy.array(({},))),\n'
            '            '
            '                     '
            '({:.17e},),\n'
            '            '
            '                     '
            '({:.0e},))\n'
            ''.format(f, x, b, val, rtol))

phi = numpy.array([-50,-3,-2,-1,0,1,4,5,7,10,15,20,30,40,50], dtype=float)

def write_header(f, modname, dependencies=''):
    f.write("""# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.

# This file was generated by `scripts/gen_test_gfd.py`.
# Do not edit this file directly, or your changes will be lost.
'''
Tests the `{modname}` module.
'''
# Make sure we import the local package
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from fdint import {modname}
import unittest
import numpy
import warnings
""".format(modname=modname))
    f.write(dependencies)
    f.write('\n')
    f.write('class Test_{modname}(unittest.TestCase):\n'
            ''.format(modname=modname.upper()))
    f.write('''
    def assertRTOL(self, a, b, RTOL):
        assert RTOL >= 0
        rerr = abs(a-b)/a
        if rerr > RTOL:
            self.fail('Outside of relative tolerance of {}: {}'
                      ''.format(RTOL, rerr))
''')
    f.write('''
    def assert_all_rtol(self, a, b, rtol):
        assert rtol >= 0
        a = numpy.array(a)
        b = numpy.array(b)
        rtol = numpy.array(rtol)
        rerr = abs(a-b)/a
        if (rerr > rtol).all():
            self.fail('Outside of relative tolerance of {}: {}'
                      ''.format(rtol, rerr))
''')

#################
# Test gfd module
modname='gfd'
fpath = os.path.join(tests_dir, 'test_{modname}.py'.format(modname=modname))
beta = numpy.linspace(0., 0.3, 5)
with open(fpath, 'w') as f:
    mod = getattr(fdint, modname)
    write_header(f, modname)
    for k2 in xrange(-1,6,2):
        k = k2/2.
        k2s = str(k2).replace('-','m')

        # scalar
        i = 0
        for b in beta:
            for x in phi:
                i += 1
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    quad_val, quad_aerr = quad_gfdk(k, x, b)
                    val = getattr(mod,'gfd{k2s}h'.format(k2s=k2s))(x,b)
                aerr = abs(val-quad_val)
                # scalar
                f.write('\n')
                f.write('    def test_gfd{k2s}h_{i}(self):\n'.format(k2s=k2s,i=i))
                f.write('        with warnings.catch_warnings():\n')
                f.write('            warnings.simplefilter("ignore")\n')
                rtol = max(abs(2*aerr/quad_val), abs(2*quad_aerr/quad_val))
                f.write(get_assertRTOL2('{modname}.gfd{k2s}h'
                                       ''.format(modname=modname,k2s=k2s),
                                       x, b, val, rtol))
                # vector
                f.write('\n')
                f.write('    def test_vgfd{k2s}h_{i}(self):\n'.format(k2s=k2s,i=i))
                f.write('        with warnings.catch_warnings():\n')
                f.write('            warnings.simplefilter("ignore")\n')
                f.write(get_assert_all_rtol2('{modname}.gfd{k2s}h'
                                            ''.format(modname=modname,k2s=k2s),
                                            x, b, val, rtol))

    f.write('\n')
    f.write('if __name__ == "__main__":\n')
    f.write('    unittest.main()')
