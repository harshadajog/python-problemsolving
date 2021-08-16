def findFrequency(A, left, right, freq):
    if left > right:
        return

    if A[left] == A[right]:
        count = freq.get(A[left])
        if count is None:
            count = 0

        freq[A[left]] = count + (right - left + 1)
        return  

    mid = (left+right)//2

    findFrequency(A, left, mid, freq)
    findFrequency(A, mid+1, right, freq)

def main():
    A = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
    freq = {}
    findFrequency(A, 0, len(A)-1, freq)
    print(freq)

if __name__=="__main__":
    main()


