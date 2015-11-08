import unittest

import ex2
import ex3
import factory


class TestExamples(unittest.TestCase):
    def test_ex2(self):
        Y = factory.get(type='random').get_list(size=1, min=0, max=1000000000)
        D = factory.get(type='random').get_list(size=1, min=0, max=100000000)
        print(ex2.solution(0, Y[0], D[0]))

    def test_ex3(self):
        A = factory.get(type='fixed').get_list()
        print(ex3.solution(A))
        pass
