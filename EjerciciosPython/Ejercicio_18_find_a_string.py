#https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def count_substring(string, sub_string):
    #Sums start and the items of an iterable from left to right and returns the total
    #Itrate through string using for loop, and ifstatement to compare and identify sub string in string
    return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)])
