from proccessClass import Proccess
 def FCFS (self,proccessList)
     count=0
     time=0
     out=[]
     
     sorted_array=[]
     while (1):
        sorted_array=proccessList
        sorted_array.sort(key=lambda x: x.arrival_t)
        for index in range(len(sorted_array)):
            if(sorted_array[index].arrival_t<= time):
                while(sorted_array[index].duration >0):
                    time=time+1
                    sorted_array[index].duration = sorted_array[index].duration - 1
                    out.append(sorted_array[index].name)
            else:
                time=time+1
                out.append("NOP")
                index=index-1    
                
     return out
#x=[]
#x[0]=Proccess(1,3,"p1",0)
#x[1]=Proccess(2,4,"p2",0) 
#print(FCFS(x))
print("kkk"")
               
         
         
        
     