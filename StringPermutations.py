def main():
    s = "ABC"
    n = len(s)
    calculate(s, 0, n-1)

def calculate(str, left, right):
    if left == right:
        print(str)
    else:
        i = left
        while i <= right:
            swapped = swap(str, left, i)
            calculate(swapped, left+1, right)  
            i +=1  

def swap(str, i, j):

    charArray = list(str)
    temp = charArray[i]
    charArray[i] = charArray[j]
    charArray[j] = temp

    new = ""
    for i in charArray:
        new += i
    return new       


if __name__=="__main__":
    main()