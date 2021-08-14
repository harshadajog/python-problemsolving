def main():
    print("Inside main")
    arr = [6,3,5,2,1,7]
    findPair(arr, 9)

def findPair(arr, X):
    print("Inside findPair")
    new_dict = dict()
    i=0
    while i < len(arr):
        num = arr[i]
        if(num > X):
            i = i + 1
        if(num < X):
            y = X - num
            if y in new_dict.keys():
                print("Pair found. First number: ", num, " at position: ",i)
                print("Second number: ", y, " at position: ",new_dict.get(y))
                break
            new_dict.update({num:i})
            i = i+1

if __name__=="__main__":
    main()