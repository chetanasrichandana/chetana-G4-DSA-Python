class Test:
   def helper(self):
      print(self.rec(int(input("Enter any number ")),2))

   def rec(self,num: int,i: int)->int:
      if i==num:
         return True
      if num%i==0:
        return False
      else:
        if i<num:
            return self.rec(num,i+1)
         
obj=Test()
obj.helper()



