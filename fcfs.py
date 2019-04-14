from proccessClass import Proccess
pro = []
pro.append(Proccess(0,8,"P1",1))
pro.append(Proccess(1,4,"P2",1))
pro.append(Proccess(2,9,"P3",1))
pro.append(Proccess(3,5,"P4",1))
def FCFS (ProccessList):
    time =0
    count=0
    last_time = -1
    out=[]
    Q = []
    while (1):
        for index in range(len(ProccessList)):
            if(ProccessList[index].arrival_t <= time and ProccessList[index].arrival_t > last_time):
                Q.append(ProccessList[index])
                count =count+1
        last_time=time
        Q.sort(key=lambda x: x.arrival_t)
        if (len(Q)>0):
            while(Q[0].duration > 0):
                time = time + 1
                Q[0].duration = Q[0].duration - 1
                out.append(Q[0].name)
            del Q[0]
        else:
            time=time+1
            out.append("NOP")
        if(len(Q) == 0 and len(ProccessList) == count):
            break
    return out
out = []
out = FCFS(pro)
print(out)

               
         
         
        
     