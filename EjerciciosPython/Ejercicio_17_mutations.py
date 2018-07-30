#https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen
def mutate_string(string, position, character):
    #Make a copy of string S as list2.
    list2=list(string)
    #Replace the character at index i with character c in string S.
    list2[position]=character
    #Return new string with new assigned character.
    return ''.join(list2)
