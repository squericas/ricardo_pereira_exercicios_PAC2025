num1 = 52
num2 = 23
num3 = 11

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >=num3:
    maior = num2
else:
    maior = num3 

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"O maior número é o {maior} e o menor número é o {menor}")