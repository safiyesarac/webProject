# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:07:19 2021

@author: Lenovo-PC
"""
import math;
import tkinter as tk

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
      "eccentricity": 0.7, 
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
    print(state)
        
    
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
resetStateToInitialConditions();
def coord(x,y):
    
    return (x), (y)

    
    