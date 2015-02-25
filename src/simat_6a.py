#Author: Juan David Parra (jdparrapimiento@gmail.com)
#Feb 24 2015
import numpy as np
import time

start_time = time.time()
 #inst
fn_inst = "data/inst.csv"
inst = np.genfromtxt(fn_inst, delimiter=',', dtype="|S200")

fn_inst_6a = "data/inst_6a.csv"
inst_6a = np.genfromtxt(fn_inst_6a, delimiter=',', dtype="|S200")

for i in inst:
    np.place(inst_6a,inst_6a==i[0], i[1])  
    
np.savetxt("data/data_inst.csv", inst_6a, delimiter=",",fmt="%s")

#sedes
fn_sedes = "data/sedes.csv"
sedes = np.genfromtxt(fn_sedes, delimiter=',', dtype="|S200")

fn_sedes_6a = "data/sedes_6a.csv"
sedes_6a = np.genfromtxt(fn_sedes_6a, delimiter=',', dtype="|S200")

for j in sedes:
    np.place(sedes_6a,sedes_6a==j[0], j[1])  
    
np.savetxt("data/data_sedes.csv", sedes_6a, delimiter=",",fmt="%s")
 
t = time.time() - start_time
print("--- %s seconds ---" % t)
    
