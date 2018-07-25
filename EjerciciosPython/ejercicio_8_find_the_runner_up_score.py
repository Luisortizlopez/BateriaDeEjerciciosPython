if __name__ == '__main__':

    #https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
    n = int(raw_input())
    arr = map(int, raw_input().split())

    #Look for highest num in array
    highest = max(arr)
    #Set value of i to start at 0
    i=0
    #Iterate arr using while loop
    while (i<n):
        #if highest is equal to highest num in arr, remove highest num.
        if highest == max(arr):
            arr.remove(max(arr))
        i+=1
     #Then we'll just print the second highest num
    print(max(arr))
