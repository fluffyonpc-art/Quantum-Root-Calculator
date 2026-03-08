import Spin_Functions as s
import math


N = int(input("How many electrons are in your actice orbitals?: "))
M = int(input("How many orbitals are in your system?: "))
S = int(input("What is the S value of your system?: "))
print("")

print("Your configuration has a total of " + str(int(s.total_states(N, M))) + " states")

while S >= 0:
    print(str(int(s.total_states_spin(N, M, S))) + " states for total spin " + str(int(2*S + 1)))
    S = S - 1