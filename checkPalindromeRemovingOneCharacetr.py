def isPalindrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True

def checkOneCharacterRemoval(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            if isPalindrome(s, low+1, high):
               return low     
            if isPalindrome(s, low, high-1):
                return high
            return -1    
    return -2

def main():
    s = "radarb"
    idx = checkOneCharacterRemoval(s)
    if idx == -1:
        print(s, " is cannot become a palindrome")
    elif idx == -2:
        print(s, " is a palindrome without removing any character")
    else:
        print(s, " becomes a palindrome after removing character: ", idx)    

if __name__=="__main__":
    main()