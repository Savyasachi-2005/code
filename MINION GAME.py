def minion_game(string):
    Vowels='AEIOU'
    abhi=0
    shek=0
    
    for i in range(len(s)):
        if s[i] in Vowels:
            abhi += len(s)-i
        else :
            shek += len(s)-i
            
    if abhi>shek:
        print(f" abhi {abhi}")
    elif shek > abhi:
        print(f"shek {shek}")
        
        
        
if __name__ == '__main__':
    s=input('Enter the string\n')
    minion_game(s)
                        