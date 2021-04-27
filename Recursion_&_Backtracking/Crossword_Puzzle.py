
mainArr=[]

def printManual(crossword):
    s=""
    for i in range(len(crossword)):
        for j in range(len(crossword)):
            s+=crossword[i][j]
        mainArr.append(s)
        s=""
    

def canPlaceHorizontally(crossword,i,j,word):
    if(j-1>=0 and crossword[i][j-1]!="+"):
        return False
    if(j+len(word)<len(crossword[0]) and crossword[i][j+len(word)]!="+"):
        return False
    
    for jj in range(len(word)):
        if(jj+j>= len(crossword[0])):
            return False
        if(crossword[i][j+jj]=="-" or crossword[i][j+jj]==word[jj]):
            continue
        else:
            return False
    return True

def placeHorizontally(crossword,i,j,word):
    placedPostion=[None]*len(word)    
    for jj in range(len(word)):
        if(crossword[i][j+jj]=="-"):
            crossword[i][j+jj]=word[jj]
            placedPostion[jj]=True
            
    return placedPostion

def unPlaceHorizontally(crossword,i,j,word):
    for jj in range(len(word)):
        if(word[jj]==True):
            crossword[i][j+jj]="-"

def canPlaceVertically(crossword,i,j,word):
    if(i-1>=0 and crossword[i-1][j]!="+"):
        return False
    if(i+len(word)<len(crossword) and crossword[i+len(word)][j]!="+"):
        return False
    for ii in range(len(word)):
        if(ii+i>= len(crossword)):
            return False
        if(crossword[i+ii][j]=="-" or crossword[i+ii][j]==word[ii]):
            continue
        else:
            return False
    return True


def placeVertically(crossword,i,j,word):
    placedPostion=[None]*len(word)
    for ii in range(len(word)):
        if(crossword[i+ii][j]=="-"):
            crossword[i+ii][j]=word[ii]
            placedPostion[ii]=True
            
    return placedPostion

def unPlaceVertically(crossword,i,j,word):
    for ii in range(len(word)):
        if(word[ii]==True):
            crossword[i+ii][j]="-"

    
def crosswordPuzzle(crossword, words,wordIndex):
    print(crossword,words,wordIndex)
    if wordIndex==len(words):
        printManual(crossword)
        return
    # Write your code here
    word=words[wordIndex]
    for i in range(len(crossword)):
        for j in range(len(crossword)):
            if(crossword[i][j]=="-" or crossword[i][j]==word[0]):
                if(canPlaceHorizontally(crossword,i,j,word)):
                    placed=placeHorizontally(crossword,i,j,word)
                    crosswordPuzzle(crossword,words,wordIndex+1)
                    unPlaceHorizontally(crossword,i,j,placed)                    
                
                if(canPlaceVertically(crossword,i,j,word)):
                    placed=placeVertically(crossword,i,j,word)
                    crosswordPuzzle(crossword,words,wordIndex+1)
                    unPlaceVertically(crossword,i,j,placed) 
    
    return mainArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = list(input())
        crossword.append(crossword_item)

    words = input().split(';')

    result = crosswordPuzzle(crossword, words,0)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
