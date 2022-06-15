# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 07:03:59 2022

@author: LENOVO
"""

import timeit

start = timeit.default_timer()

def rute_terpendek(graf, mulai, akhir): 
    result = [] # node dengan jarak terpendek simpan ke dalam list
    result.append(mulai) # inisialisasi node pertama dengan nilai asal
    while akhir not in result: # telusuri graf sampai tujuan ditemukan
        node_sekarang = result[-1]
        jarak_terpendek = min(graf[node_sekarang].values())
        for node, jarak in graf[node_sekarang].items(): # iterasi mencari
                                                        # node selanjutnya
            if jarak == jarak_terpendek:
                result.append(node)
    return result

input_graf = {
    "Tuban": {"Widang": 20},
    "Widang": {"Babat": 8},
    "Babat": {"Pucuk": 11, "Ngimbang": 23},
    "Pucuk": {"Lamongan(1)": 17},
    "Ngimbang": {"Mantup(1)": 22},
    "Lamongan(1)": {"Kembangbahu(1)": 13, "Duduk Sampeyan": 14},
    "Lamongan(2)": {"Duduk Sampeyan": 14},
    "Kembangbahu(1)": {"Mantup(1)": 13},
    "Kembangbahu(2)": {"Lamongan(2)": 13},
    "Mantup(1)": {"Bendjing": 17},
    "Mantup(2)": {"Kembangbahu(2)": 13, "Bendjing": 17},
    "Duduk Sampeyan": {"Ambengambeng": 4},
    "Bendjing": {"Surabaya": 31},
    "Ambengambeng": {"Kebomas": 13},
    "Kebomas": {"Surabaya": 18},
}

mulai_vertex = "Tuban"
akhir_vertex = "Surabaya"
Greedy = rute_terpendek(input_graf, mulai_vertex, akhir_vertex)
print ("Jalur Dari Tuban ke Surabaya adalah, ", Greedy)

stop = timeit.default_timer()
lama_eksekusi = stop - start

print("Lama eksekusi: ", lama_eksekusi, "detik")