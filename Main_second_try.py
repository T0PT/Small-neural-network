import numpy as np
import json
import time

first_dim=784
second_dim=128
third_dim=10
step=0.005
x1=np.zeros(third_dim)

def new_values():

    global w1, w2, x2, x3, b1, b2

    w1=np.random.uniform(-0.05, 0.05,[first_dim, second_dim])    
    b1=np.random.uniform(-0.05, 0.05,[second_dim])    
    x2=np.zeros(second_dim)

    w2=np.random.uniform(-0.05, 0.05,[second_dim, third_dim])
    b2=np.random.uniform(-0.05, 0.05,[third_dim])     
    x3=np.zeros(third_dim)

def save_values():
    with open('weights_and_biases_v0.2', 'w+') as out:
        json.dump([w1.tolist(), w2.tolist(), b1.tolist(), b2.tolist()], out)

def load_values():
    global w1, w2, b1, b2
    with open('weights_and_biases_v0.2', 'r') as inpt:        
        data = json.load(inpt)
        w1 = np.array(data[0])
        w2 = np.array(data[1])  
        b1 = np.array(data[2])
        b2 = np.array(data[3])      

def ReLu(Z):
    return np.maximum(Z, 0)

def ReLu_deriv(x):
    return x > 0

def sigmoid(s, array=1):
    if array==1:
        new=np.array([])
        for l in s:        
            out=np.exp(-l)
            new= np.append(new, 1/(1+out))        
        return new 
    else:
        return 1/(1+np.exp(-s))

def sigmoid_der(s):
    try:
        out=sigmoid(s,array=0)
        return out*(1-out)
    except:
        new=np.array([])
        for l in s:        
            out=sigmoid(l)
            new= np.append(new, out/(1-out))        
        return new 
    # if array==1:
    #     new=np.array([])
    #     for l in s:        
    #         out=sigmoid(l)
    #         new= np.append(new, out/(1-out))        
    #     return new 
    # else:
    #     out=sigmoid(s,array=0)
    #     return out*(1-out)

def forward(input=np.zeros(784), answer=-1):
    global w1, w2, b1, b2, x2, x3, e   
    x2=input.dot(w1)+b1
    x2=sigmoid(x2)
    x3=x2.dot(w2)+b2
    x3=sigmoid(x3)
    t=np.zeros(third_dim)
    if answer!=-1:
        t[answer]=1
        e= t-x3 # np.square(t-x5)
        cost= np.sum(np.square(t-x3))
        print('error: '+str(cost)) 

        #error=np.sum(t-x5)  
        #print(x5)  
        #return e

def backward():
    global w1, w2, b1, b2, x1, x2, x3, e    
    e2=e.dot(w2.T)
    for j in range(third_dim):
        for k in range(second_dim):            
            w2[k][j]+=step*x2[k]*sigmoid_der(x3[j])*e[j]
    for j in range(second_dim):
        for k in range(first_dim):
            w1[k][j]+=step*x1[k]*sigmoid_der(x2[j])*e2[j]
    
    

def learn():
    start = time.process_time()
    with open('10k_digits.json', 'r') as raw_data:
        data=json.load(raw_data)
        global x1
        load_values()
        for m in range(500):
            g=np.random.randint(len(data))
            h=np.random.randint(len(data[g]))
            ans=data[g][h][0]
            x1=np.array(data[g][h][1:])/255
            forward(input=x1, answer=ans)
            print(x3)
            backward()
            #forward(input=x1, answer=ans)
    save_values()
    print(time.process_time() - start)

# new_values()
# save_values()  
# learn()
