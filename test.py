# coding: utf-8

import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("..")
from OpenPyHeat_2020.OpenPyHeat_Reader import allrun,allclean


## 1-
if False :
    # allclean('Example/triCouche0D')
    Ysol,Xt = allrun('Example/triCouche0D')


    Tsol = np.array([(Ysol[:,0]+Ysol[:,1])/2,
                    Ysol[:,2],
                    (Ysol[:,3]+Ysol[:,4])/2])

    plt.figure(1)
    [plt.plot(Xt,T) for T in Tsol]
    plt.legend(["Inox","Water","Verre"])
    plt.grid()
    plt.show()

## 1.1-
if False :
    # allclean('Example/triCouche0D_air')
    Ysol,Xt = allrun('Example/triCouche0D_air')


    Tsol = np.array([(Ysol[:,0]+Ysol[:,1])/2,
                    Ysol[:,2],
                    (Ysol[:,3]+Ysol[:,4])/2])

    plt.figure(2)
    [plt.plot(Xt,T) for T in Tsol]
    plt.legend(["Inox","Air","Verre"])
    plt.grid()
    plt.show()

## 2-
if False :
    # allclean('Example/monocouche_source_constante')
    Xsol,Xt = allrun('Example/monocouche_source_constante')
    x = np.linspace(0,1,len(Xsol[0]))

    Xana = np.loadtxt('Example/monocouche_source_constante/analytic_sol/analytic_solution')
    plt.figure(3)
    plt.plot(x,Xsol[-1],color='b',marker='s',
                                    markerfacecolor='orange',
                                    markeredgecolor='b',
                                    label="OpenPyHeat")
    plt.plot(Xana[:,0],Xana[:,1],'r',alpha=0.8,label="Analytic solution")
    plt.grid(True)
    plt.legend()
    plt.xlabel(r'$\bar X$')
    plt.ylabel('Temperature [K]')
    plt.show()


## 3-E
if False :
    #Xsol,Xt = allclean('Example/tri_couche')
    Xsol,Xt = allrun('Example/tri_couche')

    Xana = np.loadtxt('Example/tri_couche/analytic_sol/analytic_solution')
    plt.figure(4)
    plt.plot(Xsol[-1],color='b',marker='s',
                                    markerfacecolor='orange',
                                    markeredgecolor='b',
                                    label="OpenPyHeat")
    plt.plot(Xana,'r',alpha=0.8,label="Analytic solution")
    plt.grid(True)
    plt.legend()
    plt.xlabel(r'$\bar X$')
    plt.ylabel('Temperature [K]')
    plt.show()

## 4-
if True :
    # allclean('Example/tri_couche_steady')
    Xsol = allrun('Example/tri_couche_steady')
    xsol = np.linspace(0,1,len(Xsol))
    Xana = np.loadtxt('Example/tri_couche/analytic_sol/analytic_solution')
    xana = np.linspace(0,1,len(Xana))

    plt.figure(5)
    plt.plot(xsol,Xsol,color='b',marker='s',
                                    markerfacecolor='orange',
                                    markeredgecolor='b',
                                    label="OpenPyHeat")
    plt.plot(xana,Xana,'r',alpha=0.8,label="Analytic solution")
    plt.grid(True)
    plt.legend()
    plt.xlabel(r'$\bar X$')
    plt.ylabel('Temperature [K]')
    plt.show()


## 5-
if False :
    # allclean('Example/cylindric_1')
    Xsol = allrun('Example/cylindric_1')
    xsol = np.linspace(0,1,len(Xsol))
    Xana = np.loadtxt('Example/cylindric_1/analytic_sol/analytic_solution')
    xana = np.linspace(0,1,len(Xana))

    plt.figure(6)
    plt.plot(xsol,Xsol,color='b',marker='s',
                                    markerfacecolor='orange',
                                    markeredgecolor='b',
                                    label="OpenPyHeat")
    plt.plot(xana,Xana,'r',alpha=0.8,label="Analytic solution")
    plt.grid(True)
    plt.legend()
    plt.xlabel(r'$\bar X$')
    plt.ylabel('Temperature [K]')
    plt.show()

## 6-
if False :
    # allclean('Example/cylindric_2')
    Xsol = allrun('Example/cylindric_2')
    xsol = np.linspace(0,1,len(Xsol))
    Xana = np.loadtxt('Example/cylindric_2/analytic_sol/analytic_solution')
    xana = np.linspace(0,1,len(Xana))

    plt.figure(7)
    plt.plot(xsol,Xsol,color='b',marker='s',
                                    markerfacecolor='orange',
                                    markeredgecolor='b',
                                    label="OpenPyHeat")
    plt.plot(xana,Xana,'r',alpha=0.8,label="Analytic solution")
    plt.grid(True)
    plt.legend()
    plt.xlabel(r'$\bar X$')
    plt.ylabel('Temperature [K]')
    plt.show()

## 7-
if False :
    # allclean('Example/cylindric_3')
    Xsol = allrun('Example/cylindric_3')
    xsol = np.linspace(0,1,len(Xsol))
    Xana = np.loadtxt('Example/cylindric_3/analytic_sol/analytic_solution')
    xana = np.linspace(0,1,len(Xana))

    plt.figure(8)
    plt.plot(xsol,Xsol,color='b',marker='s',
                                    markerfacecolor='orange',
                                    markeredgecolor='b',
                                    label="OpenPyHeat")
    plt.plot(xana,Xana,'r',alpha=0.8,label="Analytic solution")
    plt.grid(True)
    plt.legend()
    plt.xlabel(r'$\bar X$')
    plt.ylabel('Temperature [K]')
    plt.show()


## 8-
if False :
    # allclean('Example/monocouche_transient')
    Xsol,Xt = allrun('Example/monocouche_transient')
    xsol = np.linspace(0,1,len(Xsol))
    Xopf = np.loadtxt('Example//monocouche_transient/analytic_sol/openfoam_solution')

    plt.figure(9)
    line1 = plt.plot(Xt,Xsol,color='b')
    line2 = plt.plot(Xopf[:,0],Xopf[:,1:],'r',alpha=0.8)
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Temperature [K]')
    plt.legend([line1[0],line2[0]],['OpenPyHeat',"Openfoam simu"])
    plt.show()

## 9-
if False :
    # allclean('Example/paraffinExchanger')
    Xsol,Xt = allrun('Example/paraffinExchanger')

    DATA = np.loadtxt('Example/paraffinExchanger/analytic_sol/ComsolResults.txt')
    t = DATA[:,0]
    fwComsol = DATA[:,1]
    fcComsol = DATA[:,2]
    TpcmComsol = DATA[:,3]
    TwaterComsol = DATA[:,4]

    plt.figure(10)
    line1 = plt.plot(Xt,Xsol[:,:-1],color='r')
    line2 = plt.plot(Xt,Xsol[:,-1],color='b')
    line3 = plt.plot(t,TpcmComsol,color='orange')
    line4 = plt.plot(t,TwaterComsol,color='c')
    plt.grid(True)
    plt.xlabel('t')
    plt.ylabel('Temperature [K]')
    plt.legend([line1[0],line2[0],line3[0],line4[0]],['paraffin',"water",'pcm COMSOL','water COMSOL'])
    plt.show()
