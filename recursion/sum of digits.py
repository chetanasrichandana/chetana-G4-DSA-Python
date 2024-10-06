class Test:
   def helper(self):
      print(self.rec(int(input("Enter any number "))))

   def rec(self,num: int)->int:
      if num<10:
         return num
      return num%10+self.rec(num//10)


obj=Test()
obj.helper()


