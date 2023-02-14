import numpy as np
import matplotlib.pyplot as plt
from math import pi

def one():
    plt.axes(projection='polar')

    num_points = 100

    angle = [i*pi/24 for i in range(1,num_points + 1)]
    radius = [i for i in range(1,num_points + 1)]

    print(angle, radius)

    plt.plot(angle, radius, color = 'green')

    plt.show()

def two():
    plt.axes(projection='polar')

    #these three lines remove the axes and labels
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    #lists to hold all the points being plotted
    angle = []
    radius = []

    #populate the angle list with a bunch of angles
    for i in range(-314, 314): #go from negative pi to pi
        angle.append(i/100)
    
    #for each angle, push a radius in to the other list
    radius = 1-np.sin(angle)

    plt.plot(angle, radius/4, color = 'pink')
    plt.plot(angle, radius/2, color ='red')
    plt.plot(angle, radius, color = 'pink')
    plt.plot(angle, radius*2, color ='red')
    plt.show()

def three(x):
    plt.axes(projection='polar')#make the graph polar

    #these three lines remove the axes and labels
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    #lists to hold all the points being plotted
    angle = []
    radius = []
    radius2 = []
    radius3 = []
    radius4 = []

    #populate the angle list with a bunch of angles
    for i in range(-628,628): #go from negative 2pi to 2pi
        angle.append(i/100)
    
    #for each angle, push a radius in to the other list
    for i in range(len(angle)):
        if x == "1":
            radius.append(8*np.cos(angle[i]*16)) #equation is 6*cos(12*angle)
        if x == "2":
            radius2.append(6*np.cos(angle[i]*12)) #equation is 4*cos(8*angle)
        if x == "3":
            radius3.append(4*np.cos(angle[i]*8))
        if x == "4":
            radius4.append(2*np.cos(angle[i]*4))

    if x == "1":
        plt.plot(angle, radius, color = "blue") #actually draw it
    if x == "2":
        plt.plot(angle, radius2, color = "purple") #actually draw it
    if x == "3":
        plt.plot(angle, radius3, color = "green")
    if x == "4":
        plt.plot(angle, radius4, color = "red")

    plt.show()

def four(x):
    plt.axes(projection='polar')

    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)


    angle = []
    radius = []
    radius2 = []
    radius3 = []
    radius4 = []
    radius5 = []
    radius6 = []

    for i in range(-628,628):
        angle.append(i/100)
    
    for i in range(len(angle)):
        if x == "1":
            radius.append(np.sin(angle[i]/2))
        if x == "2":
            radius2.append(np.sin(angle[i]/4))
        if x == "3":
            radius3.append(1/np.sin(3*angle[i]))
        if x == "4":
            radius4.append(angle[i]*np.sin(angle[i]))
        if x == "5":
            radius5.append(1+(4*np.cos(5*angle[i])))
        if x == "6": # good
            radius6.append(1/np.sqrt(angle[i]))

    if x == "1":
        plt.plot(angle, radius, color = "red")
    if x == "2":
        plt.plot(angle, radius2, color = "red")
    if x == "3":
        plt.plot(angle, radius3, color = "red")
    if x == "4":
        plt.plot(angle, radius4, color = "red")
    if x == "5":
        plt.plot(angle, radius5, color = "red")
    if x == "6":
        plt.plot(angle, radius6, color = "red")

    plt.show()
    pass

inp = input(" -- ")
if inp == "1":
    one()
elif inp == "2":
    two()
elif inp == "3":
    inp2 = input("1,2,3, or 4 -- ")
    three(inp2)
elif inp == "4":
    inp2 = input("1,2,3,4,5, or 6 -- ")
    four(inp2)