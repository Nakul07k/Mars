def min_cost(limits, wear_factors, targets, D):

    L1, L2, L3 = limits
    W1, W2, W3 = wear_factors

    # Generate all valid configurations for a given target
    def valid_configs(target):
        configs = []
        for inner in range(min(L1, target) + 1):
            for middle in range(min(L2, target - inner) + 1):
                outer = target - inner - middle
                if 0 <= outer <= L3 and abs(inner - outer) <= D:
                    configs.append((inner, middle, outer))
        return configs

# Compute cost of moving from configuration a → b
    def move_cost(a, b):
        return abs(a[0]-b[0])*W1 + abs(a[1]-b[1])*W2 + abs(a[2]-b[2])*W3

    # Dynamic Programming dictionary:
    # key = configuration, value = minimum cost to reach it
    dp = {(0, 0, 0): 0}

    for target in targets:
        next_configs = valid_configs(target)
        if not next_configs:
            return -1  

        new_dp = {}
        for nxt in next_configs:
            new_dp[nxt] = min(prev_cost + move_cost(prev, nxt)
                              for prev, prev_cost in dp.items())
        dp = new_dp

    return min(dp.values())

def main():
    limits = eval(input("Enter limits(list): "))
    wear_factors = eval(input("Enter wear factors(list): "))
    targets = eval(input("Enter targets(list): "))
    D = int(input("Enter maximum allowed difference between Inner and Outer: "))

    print("Total cost = ",min_cost(limits, wear_factors, targets, D))

if __name__ == "__main__":
    main()
