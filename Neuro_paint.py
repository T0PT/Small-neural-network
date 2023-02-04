from tkinter import *
from turtle import color
from PIL import ImageTk, Image
import csv

wind= Tk()
wind.title('PAINt')
wind.config(bg='white')
cn=Canvas(width=781,height=781,bg='white')
field= [[0]*28]*28#[[0 for i in range(28)] for i in range(28)]
lastfield=[[0]*28]*28# [vertical y][horizontal x], 28x28 from left to right, top to bottom   
field_to_feed=[[0]*28]*28

for i in range(27):
    cn.create_line(i*28+27,0,i*28+27,839)
    cn.create_line(0,i*28+27,839,i*28+27)

def update_cn(event=0):
    global field
    global lastfield
    for y in range(0,28):
        for x in range(0,28):
            if field[y][x]!=lastfield[y][x]:
                col=field[y][x]
                cn.create_rectangle(x*28,y*28,x*28+26,y*28+26, fill=f'#{255-col:02x}{255-col:02x}{255-col:02x}', outline=f'#{255-col:02x}{255-col:02x}{255-col:02x}')                            
    print('update')
    lastfield=field

def clear():     
    global field 
    field=[[0]*28]*28       

def draw(event):    
    global field
    if event.x<784 and event.y<784:
        cn.create_rectangle(event.x//28*28,event.y//28*28,event.x//28*28+26,event.y//28*28+26, fill='black')
        #print('x'+str(event.x//28)+' y'+str(event.y//28))
        field[0][0]=30 # from left to right and up to down, y is vertical, x is horizontal        
        # try:
        #     field[event.y//28-1][event.x//28]+=15
        #     if field[event.y//28-1][event.x//28]>255: field[event.y//28-1][event.x//28]=255
        # except:
        #     pass
        # try:
        #     field[event.y//28][event.x//28+1]+=15 
        #     if field[event.y//28][event.x//28+1]>255: field[event.y//28][event.x//28+1]=255           
        # except:
        #     pass
        # try:
        #     field[event.y//28+1][event.x//28]+=15     
        #     if field[event.y//28+1][event.x//28]>255: field[event.y//28+1][event.x//28]=255      
        # except:
        #     pass
        # try:
        #     field[event.y//28][event.x//28-1]+=15 
        #     if field[event.y//28][event.x//28-1]>255: field[event.y//28][event.x//28-1]=255          
        # except:
        #     pass    
    for i in range(28):print(field[i])       

def undraw(event):
    if event.x<838 and event.y<838:
        cn.create_rectangle(event.x//28*28,event.y//28*28,event.x//28*28+26,event.y//28*28+26, fill='white', outline='white')        
        field[(event.y//28)*28+event.x//28]=0 # from left to right and up to down, y is vertical, x is horizontal        
        
delbutt=Button(text='DELETE\nALL',command=clear,height=5,width=10)
updbutt=Button(text='Update',command=update_cn,height=5,width=10)
ans=Label(text='Answer: \n',width=10,height=5,bg='white',fg='black')
cn.bind('<Button-1>',draw)
cn.bind('<B1-Motion>',draw)
cn.bind('<ButtonRelease-1>',update_cn)
cn.bind('<Button-3>',undraw)
cn.bind('<B3-Motion>',undraw)
cn.bind('<ButtonRelease-3>',update_cn)
ans.grid(column=0,row=0)
delbutt.grid(column=1,row=0)
updbutt.grid(column=2,row=0)
cn.grid(column=0,row=1,columnspan=3)
wind.mainloop()