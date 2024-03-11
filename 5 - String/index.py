def inverte_string(string):
    return string[::-1]


string_original = input("Digite uma string para inverter: ")

string_invertida = inverte_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
