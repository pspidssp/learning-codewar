# Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
# Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# Test.assert_equals(find_even_index(range(1,100)),-1)
# Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# Test.assert_equals(find_even_index(range(-100,-1)),-1)
# mark = 0
# n = 0
# p = [1,2,3,4,3,2,1]
# num = len(p)
# if sum (p[:0:-1]) == 0:
#     print(0)
#     #return 0
# else:
#     for i in range(1,num+1) :
#         a = sum ( p [n: i-1 : ] )
#         b = sum ( p [: i-1 : -1 ] )
#         print(a,b)
#         if a == b :
#             print(i-1)
#             mark = 1
#             break
#             #return i
#         if mark == 1:
#             print(-1)
        
def find_even_index(arr):
    n = 0
    p = arr
    num = len(p)
    if sum (p[:0:-1]) == 0:
        print(0)
        return 0
    else:
        for i in range(1,num+1) :
            a = sum ( p [n: i-1 : ] )
            b = sum ( p [: i-1 : -1 ] )
            
            if a == b :
                print(i-1)                
                return i-1
            
            if i == num :
                print(-1) 

find_even_index([1,2,3,4,5,6])

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

    

    
    