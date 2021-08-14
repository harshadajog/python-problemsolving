def main():
    findMaxAndMin([6,7,40,3,5,10])

def findMaxAndMin(arr):
    min = 999999
    max=0
    for itr in arr:
        if itr < min:
            min = itr
        elif itr > max:
            max = itr    
    print("Largest number in array: ", max)
    print("Smallest number in array: ", min)

if __name__=="__main__":
    main()        