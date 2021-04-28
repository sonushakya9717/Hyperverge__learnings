#####  Tower of Hanoi Problem  #####

def tower(n,A,B,C):
    if n>0:
        tower(n-1,A,C,B)
        print("Move disk:- "+str(n)+" from " +A+ " to "+C)
        tower(n-1,B,A,C) 
tower(2,"source","Auxiliary","Destination")
