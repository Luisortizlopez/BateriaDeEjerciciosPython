if __name__ == '__main__':
    #https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
    s = raw_input()

    print any(c.isalnum() for c in s)
    print any(c.isalpha() for c in s)
    print any(c.isdigit() for c in s)
    print any(c.islower() for c in s)
    print any(c.isupper() for c in s)
