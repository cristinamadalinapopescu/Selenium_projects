# Sa se scrie clase pentru urmatoarele:
# 1. FirstDegreeEquation, pentru a * x + b = 0
# cu proprietatile a, b, si metoda solutie(), care returneaza x.
# class FirstDegreeEquation:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def solutie(self):
#         x = -self.b / self.a
#         return x
#
#
# la_solutia = FirstDegreeEquation(3, 15)
# la_solutia = FirstDegreeEquation(2, 1)
# print(la_solutia.solutie())
def solutie(a, b):
    x = -b / a
    return x
