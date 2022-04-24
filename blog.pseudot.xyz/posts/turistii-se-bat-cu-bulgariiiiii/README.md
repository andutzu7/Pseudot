# Lab 2 - Tehnici Big Data
##### @autor: Vavilov Andrei
##### @grupa: SDTW 1B
----------------------------------

## Sarcina 1:
*Proiectati si implementati o solutie MapReduce pentru a contoriza numarul de aparitii ale cuvintelor intr-un fisier text.*
###### Soluție propusă:
- Dat fiind un text de intrare, primul pas este despărțirea componentelor sale(cuvinte) în token-uri.
- În faza de mapare creez tuplele de forma *(token,1)*, unde token este un cuvânt din text iar 1 este numârul
de apariții a acestuia.
- Fiecare cuvânt va avea inițial valoarea atribuită 1, indiferent dacă acesta a mai fost întâlnit în text sau nu.
- Etapa de combinare presupune sortarea split-ului de tuple în ordine lexicografică.
- Etapa de reducere presupune sumarea valorilor de frecvență a itemilor cu aceeași cheie (token).

###### Utilizare:
```
	python word_count.py
```
###### Exemplu rezultat:

![WC_OUTPUT](./WordCountMR/exemplu_output.png)

## Sarcina 2:
_Proiectati si implementati o solutie MapReduce pentru a înmulti doua matrice(patratice)._

###### Soluție propusă:
- Fișierul de intrare conține pe fiecare rând informații ce descriu un rând al unei matrici
  (ex. M,0,0,63)
- În faza de mapare procesam fisierul de intrare pentru a obtine perechi de forma
**(i,k)(M,j,M_ij)** (pentru matricea M) si **(i,k),(N,j,N_jk)** (pentru matricea N), unde:
    - i = nr de coloane din matricea M
    - j = nr de coloane din M(si implicit nr de linii din N)
    - k = nr de coloane din N
    - M_ij/N_jk elementul din matrice aflat la indexul dat
- Etapa de combinare este executata cu ajutorul functiei sort din linux și in urma acesteia
tuplele generate in etapa de mapare pot fi procesate in functie de indecsii i,k.
- Etapa de reducere constă in următorii pasi:
    - Salvarea intr-o lista a tuturor valorilor din ambele matrici care au aceiasi cheie, sub forma de tuple
    care contin indexul si valoarea care se gaseste la o anumita cheie
    - Calcularea sumei produselor elementelor cu aceiasi cheie(partea efectiva de calcul a produsului matricii)
    - Pentru fiecare index din matricea reuzultat, returnarea cheii și valorii de interes.

###### Utilizare:
Pentru simplificarea procesului de rulare, este suficientă execuția unui script bash. Aceasta se poate realiza
apelând următoarea comandă:
```
	sh run.sh
```
###### Exemplu rezultat:


![MATRIX_MUL_OUTPUT](./MatrixMulPy/matrix_mul_output.png)

###### Bibliografie problema 2:
https://github.com/amberm291/MatrixMultiplyMR
