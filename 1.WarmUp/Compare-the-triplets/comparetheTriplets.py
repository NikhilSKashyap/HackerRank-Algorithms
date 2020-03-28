def compareTriplets(a, b):
    x= []
    y =[]
    for m,n in zip(a, b):
        if m > n:
            x.append(1)
        elif m < n:
            y.append(1) 

    return [sum(x),sum(y)]

if __name__ == '__main__':
    print(compareTriplets([5,6,7],[3,6,10]))


