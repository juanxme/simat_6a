#Author: Juan David Parra
#Feb 24 2015
import numpy as np
import time
import timeit

start_time = time.time() # --- time
print("--- Algoritmo iniciado ---")
    #inst
fn_inst = "data/inst.csv"
inst = np.genfromtxt(fn_inst, delimiter=',', dtype="|S200")

fn_inst_6a = "data/inst_6a.csv"
inst_6a = np.genfromtxt(fn_inst_6a, delimiter=',', dtype="|S200")

for i in inst:
    np.place(inst_6a, inst_6a == i[0], i[1])  
    
np.savetxt("data/data_inst.csv", inst_6a, delimiter=",", fmt="%s")

t = time.time() - start_time
print("--- %s seconds inst ---" % t)  
start_time2 = time.time() # --- time
#sedes
fn_sedes = "data/sedes.csv"
sedes = np.genfromtxt(fn_sedes, delimiter=',', dtype="|S200")

fn_sedes_6a = "data/sedes_6a.csv"
sedes_6a = np.genfromtxt(fn_sedes_6a, delimiter=',', dtype="|S200")

for j in sedes:
    np.place(sedes_6a, sedes_6a == j[0], j[1])  
    
np.savetxt("data/data_sedes.csv", sedes_6a, delimiter=",", fmt="%s")

t = time.time() - start_time2
print("--- %s seconds Sedes ---" % t)  
start_time3 = time.time()# --- time

    #mun
fn_mun = "data/mun.csv"
mun = np.genfromtxt(fn_mun, delimiter=',', dtype="|S200")

fn_mun_6a = "data/mun_6a.csv"
mun_6a = np.genfromtxt(fn_mun_6a, delimiter=',', dtype="|S200")

for j in mun:
    np.place(mun_6a, mun_6a == j[0], j[1])  
    
np.savetxt("data/data_mun.csv", mun_6a, delimiter=",", fmt="%s")

t = time.time() - start_time3
print("--- %s seconds mun ---" % t)  

t = time.time() - start_time
print("--- %s seconds total ---" % t)
