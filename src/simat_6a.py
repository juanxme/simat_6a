import numpy as np
import time

start_time = time.time()

fn_dane_inst_all = "data/dane_inst_all.csv"
array_dane_inst = np.genfromtxt(fn_dane_inst_all, delimiter=',', dtype=None)

fn_dane_6a = "data/dane_6a.csv"
array_6a = np.genfromtxt(fn_dane_6a, delimiter=',', dtype=None).astype('str')
a=array_6a

print "array_6a: " , array_6a[0]   
#print "array_dane_inst: " , array_dane_inst
w=0;
for i in array_dane_inst:
    for j in array_6a:
        #print j,i[0]
        if j == i[0]:
            j=i[1]
            print "entro"
            break
    break
    
print array_6a
 
t = time.time() - start_time
print("--- %s seconds ---" % t)
    
