import sys


i,k =(5,5)

"""
In urma procesului de mapare vom obtine perechi de forma
(i,k)(M,j,M_ij) (pentru matricea M) si (i,k),(N,j,N_jk), unde:
    - i = nr de coloane din matricea M
    - j = nr de coloane din M(si implicit nr de linii din N)
    - k = nr de coloane din N
    - M_ij/N_jk elementul din matrice aflat la indexul dat

"""
for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "M":
		for index in range(0,k):
			key =  row + "," + str(index)
			print(key,matrix_index,col,value)
	else:
		for index in range(0,i):
			key = str(index) + "," + col
			print(key,matrix_index,row,value)
