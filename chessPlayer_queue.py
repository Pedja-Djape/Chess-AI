class queue:
    def __init__(self):
        self.store=[]

    def add(self,x):
        self.store = self.store + [x]
        return True

    def disc(self):
        if len(self.store)==0:
            return False
        elif len(self.store)==1:
            rval=self.store[0]
            self.store=[]
            return rval
        else:
            rval=self.store[0]
            self.store=self.store[1:len(self.store)]
            return rval
