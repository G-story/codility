import unittest

import ex2
import ex3
import ex4
import ex5
import factory


class TestExamples(unittest.TestCase):
    def test_ex2(self):
        Y = factory.get(type='random').get_list(size=1, min=0, max=1000000000)
        D = factory.get(type='random').get_list(size=1, min=0, max=100000000)
        print(ex2.solution(0, Y[0], D[0]))

    def test_ex3(self):
        A = factory.get(type='fixed').get_list()
        print(ex3.solution(A))

    def test_ex4(self):
        X = 5
        A = factory.get(type='random').get_list(size=10, min=1, max=X+1)
        result = ex4.solution(X, A)
        print(A, result)

    def test_ex5(self):
        A = factory.get(type='fixed').get_list()
        result = ex5.solution(A)
        print(A, result)
