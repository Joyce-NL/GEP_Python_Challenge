def sumevenfibonaccinumbers(startnumber, endvalue):

    if type(startnumber) not in [int, float] or type(endvalue) not in [int, float]:
        raise TypeError("Both parameters need to be integers or floats.")
    if startnumber < 0:
        raise ValueError("The first parameter should be a non-negative number.")
    if endvalue < startnumber:
        raise ValueError("The second parameter should be higher than the first parameter.")

    fibsequence = fibonaccisequence(startnumber)

    allfibnrsinrange = []
    allfibnrsinrange.extend(fibsequence[-2:])

    sumevenfibnrsinrange = 0
    for number in allfibnrsinrange:
        if number % 2 == 0 and number <= endvalue:
            sumevenfibnrsinrange += number

    i = sum(allfibnrsinrange[-2:])

    while i <= endvalue:
        if i % 2 == 0:
            sumevenfibnrsinrange += i

        allfibnrsinrange.extend([i])
        i = sum(allfibnrsinrange[-2:])

    print(sumevenfibnrsinrange)
    return sumevenfibnrsinrange


def fibonaccisequence(maxnumber):
    fibsequence = [0, 1]
    i = sum(fibsequence[-2:])

    while i < maxnumber:
        fibsequence.extend([i])
        i = sum(fibsequence[-2:])

    fibsequence.extend([i])
    i = sum(fibsequence[-2:])
    fibsequence.extend([i])

    return fibsequence

