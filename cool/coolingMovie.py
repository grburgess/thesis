import matplotlib.pyplot as plt
from numpy import *
import os



def edistS(x,gc):

    gmin = 900.


     

     

    if x>gc:

        return x**(-3.2)

    else:
        
        return gc**(-1)*x**(-2.2)

    #else:
        
    #    return x**(-2.)
        

def edistC(x,gc):


    gmin = 900
     
    if x > gmin:

        return x**(-3.2)

    else:
        
        return gmin**(-1.2)*x**(-2.)







gcGrid = logspace(log10(1e5), log10(10), 30)


names= ["0","1","2","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
i=0
for g,name in zip(gcGrid,names):

    fig = plt.figure(i)
    ax = fig.add_subplot(111)

    n = []

    if g>900.:
    
        gGrid = logspace(log10(900.), log10(1e5))
    else:
        gGrid = logspace(log10(g), log10(1e5))   


    
    for x in gGrid:

        if g>900.:
            n.append(edistS(x, g))
        else:
            n.append(edistC(x, g))

    ax.loglog(gGrid, n, color="purple", lw=2)
    ax.set_xlabel(r"$\gamma$",fontsize=18)
    ax.set_ylabel(r"n$_e$",fontsize=18)

    ax.vlines(g,1e-12,g**-3,linestyles="--")
    #print g**-2
    ax.set_ylim(bottom=1e-15,top=1e-1)
    ax.set_xlim(1,1e5)
    print "hey"

    fig.savefig("cool_"+name+".png",bbox_inches='tight')



    i=i+1

fps=3

command = ('mencoder',
			   'mf://*.png',
			   '-mf',
			   'type=png:w=800:h=600:fps='+str(fps),
			   '-ovc',
			   'lavc',
			   '-lavcopts',
			   'vcodec=mpeg4',
			   '-oac',
			   'copy',
			   '-o',
			   '/Users/jburgess/cooling.avi')

print "Starting to encode video...."
os.spawnvp(os.P_WAIT, 'mencoder', command)
print "DONE!!!"

        

        
