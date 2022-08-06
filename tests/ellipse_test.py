import unittest

import numpy as np

from geometry_543 import Ellipse

class EllipseTestCase(unittest.TestCase):

    def setUp(self):
        self.ellipse = Ellipse(1,1./np.pi)


    def test_calc_area(self):
        result = self.ellipse.calc_area()
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
        
