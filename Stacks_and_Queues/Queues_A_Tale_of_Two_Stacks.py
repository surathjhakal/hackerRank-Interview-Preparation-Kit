class MyQueue(object):
    myStack=[]    
    back=-1
    def peek(self):
        if self.back>-1:
            return self.myStack[self.back]
        
    def pop(self):
        if self.back>-1:
            self.back-=1
        
    def put(self, value):
        self.myStack.insert(0,value)
        self.back+=1
