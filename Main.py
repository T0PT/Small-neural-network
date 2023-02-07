import numpy as np
import json
import time

first_dim=784
second_dim=512
third_dim=256
fourth_dim=112
exit_dim=10
step=0.005

def new_values():

    global w1,w2,w3,w4,b1,b2,b3,b4,x2,x3,x4,x5

    w1=np.random.uniform(-0.005, 0.005,[first_dim, second_dim])
    b1=np.random.uniform(0, 0.1,[second_dim])
    x2=np.zeros(second_dim)

    w2=np.random.uniform(-0.005, 0.005,[second_dim, third_dim])
    b2=np.random.uniform(0, 0.1,[third_dim])
    x3=np.zeros(third_dim)

    w3=np.random.uniform(-0.005, 0.005,[third_dim, fourth_dim])
    b3=np.random.uniform([fourth_dim])
    x4=np.zeros(fourth_dim)

    w4=np.random.uniform(-0.005, 0.005,[fourth_dim, exit_dim])
    b4=np.random.uniform(0, 0.1,[exit_dim])
    x5=np.zeros(exit_dim)    

def save_values():
    with open('weights_and_biases', 'w+') as out:
        json.dump([w1.tolist(), w2.tolist(), w3.tolist(), w4.tolist(), b1.tolist(), b2.tolist(), b3.tolist(), b4.tolist()], out)

def load_values():
    global w1,w2,w3,w4,b1,b2,b3,b4
    with open('weights_and_biases', 'r') as inpt:        
        data = json.load(inpt)
        w1 = np.array(data[0])
        w2 = np.array(data[1])
        w3 = np.array(data[2])
        w4 = np.array(data[3])
        b1 = np.array(data[4])
        b2 = np.array(data[5])
        b3 = np.array(data[6])
        b4 = np.array(data[7])

def ReLu(x):
    for y in x:
        if y>=0: return x
        else: return 0

def sigmoid(s):
    new=np.array([])
    for l in s:        
        out=np.exp(l)
        new= np.append(new, out/(out+1))
        
    return new        

def forward(answer=0):
    global x1, x2, x3, x4, x5, e
    x2= x1.dot(w1)
    x2=sigmoid(x2)
    x3= x2.dot(w2)
    x3=sigmoid(x3)
    x4= x3.dot(w3)
    x4=sigmoid(x4)
    x5= x4.dot(w4)
    x5=sigmoid(x5)
    t=np.zeros(10)
    t[answer]=1
    e= t-x5 # np.square(t-x5)
    print('error: '+str(np.sum(np.square(t-x5)))) 
    #error=np.sum(t-x5)  
    #print(x5)  
    return e

def backward():
    global e4, w1,w2,w3,w4,b1,b2,b3,b4,x2,x3,x4,x5
    e4=e.dot(np.transpose(w4))
    #print(w4)    
    for j in range(exit_dim):
        for k in range(fourth_dim):
            w4[k][j]+=step*e4[k]*x4[k]*(1-x4[k])*x5[j]# delta_w[k][j]=step*e4[k]*x4[k]*(1-x4[k])*x5[j]    
    e3=e4.dot(np.transpose(w3))
    for j in range(fourth_dim):
        for k in range(third_dim):
            w3[k][j]+=step*e3[k]*x3[k]*(1-x3[k])*x4[j]# delta_w[k][j]=step*e4[k]*x4[k]*(1-x4[k])*x5[j]   
    e2=e3.dot(np.transpose(w2)) 
    for j in range(third_dim):
        for k in range(second_dim):
            w2[k][j]+=step*e2[k]*x2[k]*(1-x2[k])*x3[j]# delta_w[k][j]=step*e4[k]*x4[k]*(1-x4[k])*x5[j]    
    #print(w4)

# new_values()
# save_values()
start = time.process_time()   
with open('10k_digits.json', 'r') as raw_data:
    data=json.load(raw_data)
    global x1
    load_values()
    #for m in range(1000):
    g=np.random.randint(len(data))
    h=np.random.randint(len(data[g]))
    j=np.random.randint(len(data[g][h]))
    ans=data[g][h][0]
    x1=np.array(data[g][h][1:])
    forward(answer = ans)
    backward()
    forward(answer = ans)        
        
    #print(ans)
save_values()

# load_values()
# start = time.process_time()
# forward(answer = ans)
# backward()
# forward(answer = ans)
print(time.process_time() - start)