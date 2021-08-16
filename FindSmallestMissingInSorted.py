def findSmallestMissing(A, left,right):
    if left > right:
        return left
    mid = (left+right) // 2

    if A[mid] == mid:
        return findSmallestMissing(A, mid+1, right)
    else:
        return findSmallestMissing(A, left, mid-1)

def main():
    A = [0,1,2,3,4,5,6,7,9]
    (left, right) = (0, len(A)-1) 
    print("smallest missing element:", findSmallestMissing(A, left, right)) 

if __name__=="__main__":
    main()           