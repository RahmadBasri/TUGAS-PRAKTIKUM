nama ="RAHMAD BASRI"
print("NAMA :",(nama));
kelas ="TI.19.D1"
print("KELAS :",(kelas));
nim ="311910060"
print("NIM :",(nim));


print("===========================LATIHAN=================================");
R = [5,9,14,17,19,20]
print(R)

#Akses List
print("Akses List")
list1 = R[3]
print(list1)
list2 = R[2:4]
print(list2)
list3 = R[-1]
print(list3)
print("====================================================================");

#Ubah Elemen List
print("Ubah Elemen List")
print(R)
R[4]=90
print(R[4])
R[4:6]=[50-10]
print(R[4:6])
print('''====================================================================''');

#Tambah Elemen list
print('Tambah Elemen List')
print(R)
(A)= R
print((A))
(B)=(A)[2:4]
print(B)
B.append(4)
print(B)
B.extend([13,23,45])
print(B)

C = A+B
A.extend(B)
print(C)


