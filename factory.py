import random


class FixedListFactory:
    @staticmethod
    def get_list():
        return [1, 3, 6, 4, 1, 2]


class RandomListFactory:
    @staticmethod
    def get_list(size=10, min=0, max=100):
        ret = []
        for i in range(size):
            ret += [random.randrange(min, max)]
        return ret


def get(type='fixed'):
    factories = dict(fixed=FixedListFactory, random=RandomListFactory)
    return factories[type]
