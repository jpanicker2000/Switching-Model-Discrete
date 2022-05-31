
#################################################################
### Discrete event simulation model - Analysis of switch traffic
#################################################################
import numpy as np
import matplotlib.pyplot as plt

g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #simulated inputs
m_q_size =[]
m_q_delay = []
m_systime = []

for j in g:
#We use a for loop to simulate inputs of 1-> 10 for either arrival rate or service rate.
 
    
 
    #Case 1 - arrival rate constant, service rate increasing
    #Comment using '#' to disable | Delete comment '#' to enable
    
    l = float(1) # lambda (arrival rate)
    m = float(j) # mu (service rate)
    
    #Case 2 - arrival rate increasing, service rate constant
    #Comment using '#' to disable | Delete comment '#' to enable
    
    l = float(j) # lambda (arrival rate)
    m = float(1) # mu (service rate)
    
    #Case 3 - arrival rate and service rate increasing with in equal proportion
    #Comment using '#' to disable | Delete comment '#' to enable
    
    l = float(j) # lambda (arrival rate)
    m = float(j) # mu (service rate)
    
    
    T=10000 # array size
    Ta=np.random.exponential(1/l,T) # array of inter-arrival times according to 1/lambda
    Ts=np.random.exponential(1/m,T) # array of exponential service times
    TD=np.zeros(T) # array of departure times
    
    TS=np.zeros(T)
    
    TA=np.zeros(T) # array of arrival times (time difference between adjacent arrivals)
    TA[0]=Ta[0]
    
    for t in range(1,T):
        TA[t]=TA[t-1]+Ta[t]
        
    t=0 # time of an event
    ne=0 # number of departure events
    nw=0 # number of times queue was non-empty
    Tw=0 # sum of waiting times of arrivals in the queue
    W=[] # Waiting times spent by those arrival which were in queue
    Nw=[] # queue status under queuing events
    
    while(t<=TA[T-100]):    
        if TA[ne]+Ts[ne] < TA[ne+1]: # Check if departure event happens before next arrival
            TD[ne]=TA[ne]+Ts[ne] # Update departure event
            t=TD[ne] # update referen1ce time of the event
            TS[ne]=Ts[ne]
            ne +=1 # update number of departed events
        if TA[ne]+Ts[ne] >= TA[ne+1]: # Check if departure event happens after some arrivals
           w=np.where(TA[ne]+Ts[ne]>TA[ne+1:]) # Find all the waiting arrivals prior to preent departure
           TD[ne]=TA[ne]+Ts[ne] # Update present departure event
           t=TD[ne] # update reference time of the event
           tmp=TD[ne]           
           TS[ne]=Ts[ne]
           ne +=1 # update number of departed events
           nw = nw + len(w[0]) # update number of waiting arrivals
           Nw.append(len(w[0]))
           for i in range(len(w[0])): # make all waiting arrivals to depart
               tw = tmp-TA[ne] # update waiting time for the next arrival               
               Tw=Tw+tw # update the total waiting time
               W.append(tw) # update waiting time
               TD[ne]=TA[ne]+tw+Ts[ne] # Update departure of the waiting arrival
               TS[ne]=Ts[ne]+tw
               tmp=TD[ne]
               t=TD[ne] # update reference time of the event
               ne +=1 # update number of departed events
    
    
    m_q_size.append(np.mean(Nw))  # mean queue size
    m_q_delay.append(np.mean(W)) #mean queueing delay
    m_systime.append(np.sum(TS)/(T-100-1))  #mean time spent on system


#Plotting parameters
d = range(0,len(g),1)
plt.figure()
plt.plot(d,m_q_size,'r',label='Mean queue size')
plt.plot(d,m_q_delay,'b-x',label='Mean queue delay')
plt.plot(d,m_systime,'g-o',label='Mean systime')
plt.legend(loc=0,fontsize=14)

#Case 1
#Comment using '#' to disable | Delete comment '#' to enable
plt.xlabel('Service Rate', fontname = 'Times', fontsize = 14, fontweight ='bold') 

#Case 2
#Comment using '#' to disable | Delete comment '#' to enable
#plt.xlabel('Arrival Rate', fontname = 'Times', fontsize = 14, fontweight ='bold') 

#Case 3
#Comment using '#' to disable | Delete comment '#' to enable
#plt.xlabel('Arrival Rate/Service Rate', fontname = 'Times', fontsize = 14, fontweight ='bold') 

plt.ylabel('Values', fontname = 'Times', fontsize = 14,fontweight ='bold')
plt.title('Packet Flow in Switching (Discrete)', fontname = 'Times', fontsize = 18,fontweight ='bold')
