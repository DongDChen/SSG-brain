import numpy as np

"""Given P, N, ACC, SEN, calculate SPE"""



#SPE= (ACC*(N+P) -SEN *P)/N

P = 110
N = 147
ACC = (74.12)/100
SEN = (71.96)/100
SPE = (ACC*(N+P) - (SEN*P))/N

print(SPE)