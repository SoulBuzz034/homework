grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
b_Johnny = sum(grades[0]) / len(grades[0])
print(b_Johnny)
b_Bilbo = sum(grades[1]) / len(grades[1])
print(b_Bilbo)
b_Steve = sum(grades[2]) / len(grades[2])
print(b_Steve)
b_Khedrik = sum(grades[3]) / len(grades[3])
print(b_Khedrik)
b_Aarom = sum(grades[4]) / len(grades[3])
print(b_Aarom)

answer = {'Johnny': b_Johnny, 'Bilbo' : b_Bilbo, 'Steve': b_Steve, 'Khendrik': b_Khedrik, 'Aaron': b_Aarom}
print(answer)