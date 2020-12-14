import numpy
from numpy import log as ln

from sympy import lambdify, symbols, diff


def derived_function(f):
    sx = symbols("x")
    return lambdify(sx, diff(f(sx), sx))


def bisection(f, range1, deff, eps):
    def bisection_method(f, range2, eps):
        # print(range2)
        err = ((-1) * ln(eps / (range2[1] - range2[0]))) / ln(2)

        a = range2[0]
        ya = f(a)  # numpy.longdouble(f(a))

        b = range2[1]
        yb = f(b)  # numpy.longdouble(f(b))

        c = (b + a) / 2
        yc = f(c)  # numpy.longdouble(f(c))

        # c_prev = eps
        n = 1
        while n < err:
            c_prev = c

            if ya * yc < 0:
                b = c
                yb = yc
            # elif yc * yb < 0:
            elif ya * yc >= 0:
                a = c
                ya = yc
            else:
                return None

            c = (b + a) / 2
            yc = f(c)  # numpy.longdouble(f(c))

            ++n  # next row done

            if abs(c - c_prev) < eps:
                return c

    def bisection_scan(f, range1, deff):
        # eps = 10 ** -10

        x2 = range1[0]
        y2 = f(x2)
        ret = []
        while x2 <= range1[1]:
            x1 = x2
            y1 = y2

            x2 += deff
            y2 = f(x2)

            if y1 * y2 < 0:
                # bisection_method(f, (x1, x2), eps)
                # print(str(bisection_method(f, (x1, x2), eps)))

                ret.append(bisection_method(f, (x1, x2), eps))
                # print(f(tmp))
                # print("%.2f" % f(tmp))
        return ret

    roots = bisection_scan(f, range1, deff)
    possible_roots = bisection_scan(derived_function(f), range1, deff)
    for item in possible_roots:
        if abs(f(item)) < eps:
            roots.append(item)
    print("The roots are:")
    for item in roots:
        print("%.6f" % item)


def main():
    power = int(input("Enter the highest power of the polynomial : "))
    temp = []

    i = power
    while i >= 0:
        if i != 0:
            temp.append(int(input("Enter the number*(X**" + str(i) + ") : ")))
        else:  # if k == 0:
            temp.append(int(input("Enter a free number: ")))
        i -= 1

    start = float(input("Enter the start of range: "))
    end = float(input("Enter the end of range: "))
    range1 = (start, end)

    f = numpy.poly1d(temp)

    deff = 0.1
    eps = 10 ** -10

    bisection(f, range1, deff, eps)


main()
