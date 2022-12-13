from itertools import combinations
 
data_list = [1, 2, 3, 4, 5]
# kombinasi dari angka 1, 2, 3, 4, 5 =>  hasil kombinasi terdapat 10 kombinasi.
kombinasi = combinations(data_list, r=2)
# Cetak Hasil
for index, data in enumerate(list(kombinasi), 1):
    print(f'kombinasi ke: {index}. {data}')



    
#dibuat :septedy prasetya 25 oktober 2022