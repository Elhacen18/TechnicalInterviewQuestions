

# Problem solving

'''
During my internship interview, I was asked a whiteboard question to reverse an array by swapping the first element with the last, the second with the second last, and so on. They wanted to see my thinking process and how I handled edge cases like an empty array or an array with one element.

Example:
- Given: [3, 2, 7, 4, 5, 6]
- Result: [6, 5, 4, 7, 2, 3]
'''
def ReverseArray(Arr):
    
    lp = 0  
    rp = len(Arr)-1
    while (lp<rp):
        tmp1 = Arr[lp] 
        tmp2 = Arr[rp]
        Arr[lp]=tmp2
        Arr[rp]=tmp1
        lp+=1
        rp-=1
    print(Arr)
ReverseArray([1,5,3,4,5])
ReverseArray([3,2,7,4,5,6,7,8])

'''
outputs
[5, 4, 3, 5, 1]
[8, 7, 6, 5, 4, 7, 2, 3]

'''

    