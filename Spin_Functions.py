import math
from itertools import combinations

def total_states(N, M):
    states = math.comb(2*M, N)
    return states

def total_states_spin(N, M, S):
    comb1a = (M + 1)
    comb1b = (N//2 - S)
    comb2a = (M+1)
    comb2b = (N//2 + S + 1)
    states = float((2*S + 1)/(M + 1)) * math.comb(comb1a, comb1b) * math.comb(comb2a, comb2b)
    return states