"""
A example to show how to profile a python script
"""
order = ['PM2.5', 'PM10', 'SO2', 'NO2', 'O3', 'CO']
pri_polls = ['CO', 'SO2', 'NO2', 'PM2.5']
concs = [1.223, 15.4, 0.34, 74.807]
ord_dict = {k: i for i, k in enumerate(order)}


@profile
def func1():
    for p in order:
        if p in pri_polls:
            x = p
            i = pri_polls.index(p)
            y = concs[i]
            break
    return x, y


@profile
def func2():

    for ord_p in order:
        for i, p in enumerate(pri_polls):
            if p == ord_p:
                x = p
                y = concs[i]
                return x, y


@profile
def func3():

    x = sorted(pri_polls, key=lambda x: ord_dict[x])[0]
    i = pri_polls.index(x)
    y = concs[i]
    return x, y


if __name__ == '__main__':
    N = 1000000
    for _ in xrange(N):
        func1()
        func2()
        func3()
