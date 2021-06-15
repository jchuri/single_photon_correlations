from collections import Counter

def calculate_N_c(chA:list[int], chB:list[int]) -> dict[int,int]:
    difference_matrix = [j - i for j in chB for i in chA]
    return dict(Counter(difference_matrix))

def calculate_g2(tau_c : int, T : int, chA:list[int], chB:list[int]) -> dict[int, float]:
    N_0 = (len(chA) + len(chB)) / 2
    normalization_const = T / (tau_c * N_0**2)
    Nc = calculate_N_c(chA, chB)
    return {key : value*normalization_const for key, value in Nc.items()}

if __name__ == "__main__": 
    chA = [0,2,4,6,8,10]
    chB = [1,3,5,7,9,11]
    print([j-i for j in chB for i in chA])
    T = 100 
    tc = 10
    print(calculate_g2(tc, T, chA, chB))