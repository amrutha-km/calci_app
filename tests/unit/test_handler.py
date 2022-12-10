import json

import unittest

from hello_world import app

class TestCalc(unittest.TestCase)

    def test_add(self):
        self.assertEqual(app.add(10,5),15)
        self.assertEqual(app.add(-1,1),0)
        self.assertEqual(app.add(-1,-1),-2)

    def test_sub(self):
        self.assertEqual(app.sub(10,5),5)
        self.assertEqual(app.sub(-1,1),-2)
        self.assertEqual(app.sub(-1,-1),0)

    def test_multi(self):
        self.assertEqual(app.multi(10,5),50)
        self.assertEqual(app.multi(-1,1),-1)
        self.assertEqual(app.multi(-1,-1),1)

if __name__== '__main__':
    unittest.main()


