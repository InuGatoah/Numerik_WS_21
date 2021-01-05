#################################################
#Author: Susi Gentsch                           #
#Date: 2020-11-12                               #
#Description: Blatt 1, Aufgabe 2                #
#################################################
import numpy as np
import time

#a) Erstelle einen Kommentar

# Ein Kommentar wird mit # eingeleitet

print("a)")
print("#")

#b) Erstelle einen 1×4 Zeilenvektor

list_1 = [1, 2, 3, 4]
vector_1 = np.array(list_1)

print("\nb)")
print(vector_1)

#c) Erstelle einen 5×1 Spaltenvektor

list_2 = [[1], [2], [3], [4], [5]]
vector_2 = np.array(list_2)

print("\nc)")
print(vector_2)

#d) Erstelle eine Nullmatrix mit einer vorhandenen Funktion

zero = np.zeros((2,2))

print("\nd)")
print(zero) 

#e) Gebe die zweite Zeile einer 4×3 Matrix aus

matrix_1 = np.aragne(12)
matrix_1 = matrix_1.reshape((4,3))

print(matrix_1)
print(matrix_1[1])

#alternativ:
#result_e = [0] * 3
#list_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#matrix_1 = np.array(list_3)
#
#for iter_0 in range(3):
#    result_e[iter_0] = matrix_1 [1] [iter_0]
#
#print("\ne)")
#print(matrix_1)
#print(result_e)

#f)  Gebe die dritte Spalte einer 4×4 Matrix aus

matrix_2 = np.aragne(16)
matrix_2 = matrix_2.reshape((4,4))

print(matrix_2)
print(matrix_2[:,2])

#result_f = [0] * 4
#list_4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#matrix_2 = np.array(list_4)
#
#for iter_1 in range(4):
#    result_f[iter_1] = matrix_2 [2] [iter_1]
#
#print("\nf)")
#print(matrix_2)
#print(result_f)

#g)  Transponiere eine Matrix

result_g = np.zeros((4,4))

result_g = np.transpose(matrix_1)

print("\ng)") 
print(matrix_1)
print(result_g)

#h) Erzeuge zwei Matrizen gleicher Große (m×m).
#   Multipliziere die Matrizen einmal elementweiseund einmal als gewohnliche Matrixmultiplikation

result_h1 = np.zeros((2,2))
result_h2 = np.zeros((2,2))
list_5 = [[1, 2], [3, 4]]
list_6 = [[5, 6], [7, 8]]
matrix_3 = np.array(list_5)
matrix_4 = np.array(list_6)

result_h1 = np.multiply(matrix_3, matrix_4)
result_h2 = np.dot(matrix_3, matrix_4)


print("\nh)")
print(matrix_3)
print(matrix_4)
print("Elementweise: ", result_h1)
print("Matrixmulti: ", result_h2)

#i) Verknupfe zwei Matrizen jeweils unter Verwendung einer vorhandenen Funktion sowohl horizontalals auch vertikal

result_i1 = np.zeros((2,2))
result_i2 = np.zeros((2,2))

result_i1 = np.concatenate((matrix_3, matrix_4))
result_i2 = np.concatenate((matrix_3,matrix_4), axis = 1)

print("\ni)")
print(matrix_3)
print(matrix_4)
print("Vertikal: ", result_i1)
print("Horizontal: ", result_i2)

#j Gebe die Gr ̈oße bzw. Dimension einer Matrix aus

result_j = 0

result_j = np.shape(matrix_1)

print("\nj)")
print(matrix_1)
print(result_j)

#k) Verandere unter Verwendung einer vorhandenen Funktion die Struktur einer 8×7 Matrix,
#   so dass eine 14×4 Matrix entsteht

print("\nk)")

matrix_5 = np.zeros((8,7))
print(matrix_5)
matrix_5 = matrix_5.reshape((14,4))

print(result_k)

#l Vervielfache einen 3×1 Vektor, so dass eine 3×10000 Matrix entsteht

matrix_6 = np.ones((3,1))
print(matrix_6)
matrix_6 = np.repeat(matrix_6, 10000, axis = 1)

print("\nl)")
print(result_l)

#m) Setze alle negativen Elemente einer Matrix auf 0

list_7 = [[1, -3],[-4, 2]]
matrix_7 = np.array(list_7)

print("\nm)")
print(matrix_7)

matrix_7[np.where(matrix_7 < 0)] = 0

print(matrix_7)

#n Erzeuge einen Vektor mit den Zahlen von 1 - 100, wobei die Zahlen einen Abstand von 7 aufweisen

list_8 = [0] * 100

print("\nn)")
print(list_8)

for iter_0 in range(100):
    list_8[iter_0] = iter_0 * 7

print(list_8)

#o Erzeuge einen Vektor mit 100 Eintr ̈agen. Setze anschließend jedes zweite Element des Vektors aufnull

list_9 = [2] * 100

print("\no)")
print(list_9)

for iter_0 in range(100):
    if (iter_0 % 2) != 0:
        list_9[iter_0] = 0

print(list_9)

#p Erzeuge einen Vektor mit 100 Eintr ̈agen. Losche anschließend jedes zweite Element des Vektors

list_10 = [0] * 100
ele = 0

print("\np)")
print(list_10)

list_10 = list_10[1::2]

print(list_10)

#q Erzeuge zwei Matrizen mit der Dimension 100×3, welche mit Zufallszahlen gefullt sind. Dabeik ̈onnen  die  Zeilen  einer  solchen  Matrix  als  1×3  Vektoren  interpretiert  werden.
#   Berechne  das Skalarprodukt fur alle Paare dieser Vektoren unter Verwendung von Schleifen.
#   Dazu muss ̈uber die Zeilen der 1000×3 Matrizen iteriert werden und das Skalarprodukt fur die Vektoren, welche durch die aktuellen Matrixzeilen gegeben sind, berechnet werden. 
#   Berechne weiterhin diese Skalarprodukte ohne die Verwendung von Schleifen. Vergleiche die Laufzeiten der beiden Varianten.(Hinweis: Zum Zeitmessen k ̈onnen in Matlab die Funktionentic,tocund in Python das Modultimeverwendet werden). Was fallt dir auf, wenn du die Laufzeiten miteinander vergleichst?

print("q)")
m_1 = np.random.random((1000,3))
m_1 = np.random.random((1000,3))

dots = np.zeros((1000,1000))

loop_start = time.time()

for i in range(0,1000):
    for j in range(0,1000):
        dots[i,j] = m_1[i]@m_2[j]

loop_end = time.time()

print(dots)

np_start = time.time()

np_dots = m_1@m_2.T

np_end = time.time()

print(np_dots)

print("Error: ", np.linalg.norm(dots-np_dots))

print("Zeit mit Schleife: ", loop_end-loop_start, "s")
print("Zeit ohne Schleife: ", np_end-np_start, "s")


#r) In dieser Aufgabe ist folgendes Szenario gegeben. Wir wollen 1000 2×2 Matrizen invertieren.
#   Die 2×2 Matrizen sind jeweils als Zeile repr ̈asentiert (vgl. Abbildung 1). 
#   Die tiefgestellten Zahlenan den Matrixeintragen stellen die Position des Eintrages in der 2×2 Matrix dar. 
#   Die hochgestellteZahl gibt den Index der aktuellen Matrix an (n= 1000). 
#   Erzeuge eine 1000×4 Matrix mit zuf ̈alligenEintr ̈agen, wobei jede Zeile wie in Abbildung 1 gezeigt, nun einer 2×2 Matrix entspricht. 
#   ZurBerechnung der Inversen der Matrizen soll das gegebene Speicherlayout der 2×2 Matrizennichtver ̈andert  werden  (d.h.  eine  Zeile  des  gegebenen  Speicherlayouts  sollnichtin  ein  2×2  Arrayumgewandelt werden, womit dann die Inverse ̈uber vorhandene Funktionen berechnet wird).
#   MitHilfe der Cramer’schen Regel fur 2×2 Matrizen kann jede der 1000 Matrizen nun invertiert werden.
#   Berechne nun die Inversen fur die erzeugten 2×2 Matrizen ohne daf ̈ur Schleifen zu verwenden.

a = np.random.random((1000,4))  #(a11 a12 a21 a22)

#det(A) = a11*a22 - a12*a21
#Berechne die Determinatnte jeder Matrix
det = a[:,0]*a[:,3] - a[:,1]*a[:,2]

#Entferne Zeilen, bei denen Determinante zu nah an 0 liegt
result = a[np.abs(det) > 0.00001]

#Tausche a0 und a3
result[:,[0,1,2,3]] = result[:,[3,1,2,0]]

#Aendere das Vorzeichen von a1 und a2
result[:,1] *= -1
result[:,2] *= -1

#Teile durch Dertereminante
result/= np.repeat(det.reshape((1000,1)), 4, axis = 1)

print("r)")
print(a)
print(result)
