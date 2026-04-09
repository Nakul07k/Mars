import statistics

def muchiko(data, window):
    output = []
    for i in range(len(data) - window + 1):
        L = data[i : i + window]
        avg = sum(L) / window
        output.append(avg)
    return output

def sanchiko(data, window):
    output = []
    for i in range(len(data) - window + 1):
        L = data[i : i + window]
        median = statistics.median(L)
        output.append(median)
    return output

# Hybrid filter: applies Sanchiko first, then Muchiko
def hybrid(data, window):
    S = sanchiko(data, window)
    M = muchiko(S, window)
    return M


        

def main():
    data=eval(input("Enter list: "))
    window=int(input("Enter window size: "))

    Muchiko= muchiko(data, window)
    Sanchiko= sanchiko(data, window)
    Hybrid= hybrid(data, window)

    print("Muchiko: ",Muchiko)
    print("Sanchiko: ",Sanchiko)
    print("Hybrid: ",Hybrid)

    variances = {}
    # Variance requires at least 2 values
    if len(Muchiko)  >= 2: variances["Muchiko"] = statistics.variance(Muchiko)
    if len(Sanchiko) >= 2: variances["Sanchiko"] = statistics.variance(Sanchiko)
    if len(Hybrid)   >= 2: variances["Hybrid"] = statistics.variance(Hybrid)

    if variances:
        best = min(variances.values()) # Determine which filter has the lowest variance (best smoothing and noise removed)
        filters=[]
        for i in variances:
            if variances[i]==best:
                filters.append(i)

        print(filters,"is best with a variance of",best)
    else:
        print("No best")

 
if __name__ == "__main__":
    main()
