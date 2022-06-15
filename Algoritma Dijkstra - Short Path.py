# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 07:03:59 2022

@author: LENOVO
"""
import timeit

start = timeit.default_timer()

class Dijkstra:
    def __init__(self, vertex, graf):
        self.vertex = vertex
        self.graf = graf
    def rute_terpendek(self, mulai, akhir):
        unvisited = {n: float("inf") for n in self.vertex}
        unvisited[mulai] = 0  # setel titik awal ke 0
        visited = {}  # daftar semua node yang dikunjungi
        parents = {}  # pendahulu
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # dapatkan jarak
                                                            # terkecil
            for tetangga, _ in self.graf.get(min_vertex, {}).items():
                if tetangga in visited:
                    continue
                new_distance = unvisited[min_vertex] 
                + self.graf[min_vertex].get(tetangga, float("inf"))
                if new_distance < unvisited[tetangga]:
                    unvisited[tetangga] = new_distance
                    parents[tetangga] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == akhir:
                break
        return parents, visited
    @staticmethod
    def generate_path(parents, mulai, akhir):
        jalur = [akhir]
        while True:
            key = parents[jalur[0]]
            jalur.insert(0, key)
            if key == mulai:
                break
        return jalur
    
input_vertex = ("Tuban", "Widang", "Babat", "Pucuk", "Ngimbang", "Lamongan", 
                "Kembangbahu", "Mantup", "Duduk Sampeyan", "Bendjing", 
                "Ambengambeng", "Kebomas", "Surabaya")
input_graf = {
    "Tuban": {"Widang": 20},
    "Widang": {"Tuban": 20, "Babat": 8},
    "Babat": {"Widang": 8, "Pucuk": 11, "Ngimbang": 23},
    "Pucuk": {"Babat": 11, "Lamongan": 17},
    "Ngimbang": {"Babat": 23, "Mantup": 22},
    "Lamongan": {"Pucuk": 17, "Kembangbahu": 13, "Duduk Sampeyan": 14},
    "Kembangbahu": {"Mantup": 12, "Lamongan": 13},
    "Mantup": {"Ngimbang": 22, "Kembangbahu": 12, "Bendjing": 17},
    "Duduk Sampeyan": {"Lamongan": 14, "Ambengambeng": 4},
    "Bendjing": {"Mantup": 17, "Surabaya": 31},
    "Ambengambeng": {"Duduk Sampeyan": 4, "Kebomas": 13},
    "Kebomas": {"Ambengambeng": 13, "Surabaya": 18},
    "Surabaya": {"Kebomas": 18, "Bendjing": 31}
}

mulai_vertex = "Tuban"
akhir_vertex = "Surabaya"
dijkstra = Dijkstra(input_vertex, input_graf)
p, v = dijkstra.rute_terpendek(mulai_vertex, akhir_vertex)
se = dijkstra.generate_path(p, mulai_vertex, akhir_vertex)
print("Jalur terpendek dari %s ke %s adalah, ['%s']" % (mulai_vertex,
akhir_vertex, "', '".join(se)))

stop = timeit.default_timer()
lama_eksekusi = stop - start
print("Lama eksekusi: ", lama_eksekusi, "detik")