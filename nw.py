# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:07:19 2021

@author: Lenovo-PC
"""
import math;
import tkinter;
import matplotlib.pyplot as plt;
import matplotlib.animation as ani
from matplotlib.patches import Circle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def rungeKutta(h, u, derivative) :
    
     def calculate(h, u, derivative) : 
        a = [h/2, h/2, h, 0]
        b = [h/6, h/3, h/3, h/6]
        u0 = []
        ut = []
        dimension = len(u)

        for i in range(dimension) :
            u0.append(u[i])
            ut.append(0)
      

        for j in range(4) :
            du = derivative

            for i in range(dimension) :
                u[i] = u0[i] + a[j]*du[i]
                ut[i] = ut[i] + b[j]*du[i]
        
      

        for i in range(dimension) : 
            u[i] = u0[i] + ut[i]
      
    

     return calculate(h, u, derivative);
      

  

state = { "u": [0, 0, 0, 0],
      "masses": {
        "q": 0, 
        "m1": 1,
        "m2": 0,
        "m12": 0 
      },
      "eccentricity": 0, 
 
      "positions": [
        {
          "x": 0,
          "y": 0
        },
        {
         "x": 0,
          "y": 0
        }
      ],
      
    };

initialConditions = {
      "eccentricity": 0.07, 
      "q": 0.5, 
      "position": {
       "x": 1,
        "y": 0
      },
      "velocity": {
        "u": 0
      }
    };


   
    
def initialVelocity(q, eccentricity) :
    return math.sqrt( (1 + q) * (1 + eccentricity) );
    

   
def   updateParametersDependentOnUserInput() :
    state["masses"]["m2"] = state["masses"]["q"]
    state["masses"]["m12"] = state["masses"]["m1"] + state["masses"]["m2"]
    state["u"][3] = initialVelocity(state["masses"]["q"], state["eccentricity"])
    

def resetStateToInitialConditions() :
    state["masses"]["q"] = initialConditions["q"]
    state["eccentricity"] = initialConditions["eccentricity"]
    state["u"][0] = initialConditions["position"]["x"]
    state["u"][1] = initialConditions["position"]["y"]
    state["u"][2] = initialConditions["velocity"]["u"]
    
    updateParametersDependentOnUserInput()
    

def derivative() :
    du =  [None] * len(state["u"])
    r = state["u"][0:2]
    rr = math.sqrt( math.pow(r[0],2) + math.pow(r[1],2) )
    print(rr)
    for i in range(2):
        du[i] = state["u"][i + 2];
      
        du[i + 2] = -(1 + state["masses"]["q"]) * r[i] / (math.pow(rr,3))
          
    
    return du;
        


def  updatePosition() :
    timestep = 0.15
    rungeKutta(timestep, state["u"], derivative())
    calculateNewPosition()
    #print(state)
        
    
def calculateNewPosition() :
    r = 1
    a1 = (state["masses"]["m2"] / state["masses"]["m12"]) * r
    a2 = (state["masses"]["m1"] / state["masses"]["m12"]) * r
    
    state["positions"][0]["x"] = -a2 * state["u"][0]
    state["positions"][0]["y"] = -a2 * state["u"][1]
    
    state["positions"][1]["x"]  = a1 * state["u"][0]
    state["positions"][1]["y"] = a1 * state["u"][1]
        
    
        
def  separationBetweenObjects() :
    return initialConditions.position.x / (1 - state.eccentricity)
        
    
def  updateMassRatioFromUserInput(massRatio) :
    state.masses.q = massRatio
    updateParametersDependentOnUserInput()
        
    
def  updateEccentricityFromUserInput(eccentricity) :
    state.eccentricity = eccentricity
    updateParametersDependentOnUserInput()

"""
x_data=[]
y_data=[]

x1_data=[]
y1_data=[]
resetStateToInitialConditions();
fig, ax =plt.subplots()
ax.set_ylim(-10,10)
ax.set_xlim(-10,10)
#c=Circle((state["positions"][0]["x"],state["positions"][0]["y"]),radius=0.2,color="red")
#cc=Circle((state["positions"][1]["x"],state["positions"][1]["y"]),radius=0.2)
circ1,=  ax.plot(state["positions"][0]["x"],state["positions"][0]["y"])    #ax.add_patch(c)
circ2,= ax.plot(state["positions"][1]["x"],state["positions"][1]["y"])#ax.add_patch(cc)

def animate(i):



    

   
    
    updatePosition()
    x_data.append(state["positions"][0]["x"])
    y_data.append(state["positions"][0]["y"])
    
    circ1.set_xdata( x_data)
    circ1.set_ydata(y_data)
    #circ2.set_xdata(state["positions"][1]["x"])
    #circ2.set_ydata(state["positions"][1]["y"])
    return circ1,  #circ2,
   
def animatet(i):



    

   
    
    updatePosition()
    x1_data.append(state["positions"][1]["x"])
    y1_data.append(state["positions"][1]["y"])
    
    circ2.set_xdata( x1_data)
    circ2.set_ydata(y1_data)
    #circ2.set_xdata(state["positions"][1]["x"])
    #circ2.set_ydata(state["positions"][1]["y"])
    return circ2,  #circ2,


    

  
   
   
    
ani =ani.FuncAnimation(fig, func=animate,frames = 5000,interval = 20, blit = True) 
anit =ani.FuncAnimation(fig, func=animatet,frames = 5000,interval = 20, blit = True) 

plt.show()    
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
root = tkinter.Tk()

label = tkinter.Label(root,text="SHM Simulation").grid(column=0, row=0)

r = 2
def circle(phi, phi_off,offset_x, offset_y):
        return np.array([r*np.cos(phi+phi_off), r*np.sin(phi+phi_off)]) + np.array([offset_x, offset_y])

plt.rcParams["figure.figsize"] = 8,6

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)
def Pause():

     return ani.event_source.stop()

#unpause
def Play():
    return ani.event_source.start()
def Eccentricity(inputval):
    state["eccentricity"]=inputval
    return ;

a=tkinter.Button( root,text="Play", command=Play).grid(column=0,row=2)
b=tkinter.Button( root,text="Pause", command=Pause).grid(column=0,row=3)
def endProgam():
    raise SystemExit
    sys.exit()


B = tkinter.Button(root, text = "Exit", command = endProgam).grid(column=1,row=3)
ax.axis([-30,30,-30,30])
ax.set_aspect("equal")
resetStateToInitialConditions();
# create initial conditions
phi_offs = [ np.pi/2, np.pi] 
offset_xs = [state["positions"][0]["x"] ,state["positions"][1]["x"]]
offset_ys = [state["positions"][0]["y"] ,state["positions"][1]["y"]]
# amount of points
N = len(phi_offs)

# create a point in the axes
points = []
for i in range(N):
  x,y = circle(0, phi_offs[i], offset_xs[i], offset_ys[i])
  points.append(ax.plot(x, y, marker="o")[0])


def update(phi, phi_off, offset_x,offset_y):
        # set point coordinates
        updatePosition()
        for i in range(N):
          x, y = circle(phi,phi_off[i], offset_x[i], offset_y[i])
          points[i].set_data([state["positions"][i]["x"] ],[state["positions"][i]["y"] ])
        return points
"""
ani = animation.FuncAnimation(fig,update,
      fargs=(phi_offs, offset_xs, offset_ys), 
      interval = 2, 
      frames=np.linspace(0,2*np.pi,360, endpoint=False),
      blit=True)
"""
#plt.show()




ani = animation.FuncAnimation(fig,update,
      fargs=(phi_offs, offset_xs, offset_ys), 
      interval = 2, 
      frames=np.linspace(0,2*np.pi,360, endpoint=False),
      blit=True)





tkinter.mainloop()