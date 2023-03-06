
    
    #using reduce function
from  functools import reduce
for i in range(1,100):

      add=reduce(lambda x,y:x+y,list(range (1,100)))
print (add)