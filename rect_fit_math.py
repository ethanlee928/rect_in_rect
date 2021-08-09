import argparse
import math

def checking_first(a, b, p, q):
    if p <= a and q <= b:
        return True
    else:
        return False

def checking_second(a, b, p, q):
    num1 = 2 * p * q * a
    num2 = p * p + q * q
    num3 = (p * p - q * q) * math.sqrt(num2 - a * a)
    mysterious_number = (num1 + num3) / num2
    if p > a and b >= mysterious_number:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='fit one rect in another rect')
    parser.add_argument("--p", type=float, help='longer side of the rect to fit inside another rect')
    parser.add_argument("--q", type=float, help='shorter side of the rect to fit inside another rect')
    parser.add_argument("--a", type=float, help='longer side of the rect to be fitted')
    parser.add_argument("--b", type=float, help='shorter side of the rect to be fitted')

    args = parser.parse_args()
    p = args.p
    q = args.q
    a = args.a
    b = args.b

    fit_boolean = (checking_first(a, b, p, q) or checking_second(a, b, p, q))

    if fit_boolean:
        print(f'It fits!')
    else:
        print(f'It does not fit')