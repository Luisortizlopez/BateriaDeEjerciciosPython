if __name__ == '__main__':

    #https://www.hackerrank.com/challenges/python-tuples/problem
    n = int(raw_input())
    #Convert list elements from strings to ints
    #Iterate list replacing strings to ints, split string into a list
    integer_list = map(int, raw_input().split())

    #Convert list of ints to a tuple of ints (tuples are hash able, list are not)
    #Used to quickly compare dictionary keys during a dictionary lookup.
    t = tuple(integer_list)

    #Print the result of hash(t)
    print hash(t)
