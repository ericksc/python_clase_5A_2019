
frutas = [
    [1, 'melon', 400],
    [4,'sandia', 500],
    [2,'banano', 10],
    [3,'papaya', 600]
]
#pregunta: precio la preferida
#resultado = [fruta[2] for fruta in frutas if fruta[0] == 1]

#fruta cuyo precio es menor a 500
#resultado = [fruta[1] for fruta in frutas if fruta[2] < 500]

# Cual es la fruta mas barata
# primero vamos a obtener los precios
precios = [fruta[2] for fruta in frutas]
#resultado = [fruta[1] for fruta in frutas if fruta[2] == min(precios)]

# cual es la fruta mas barata o la favorita
resultado = [[fruta[1], fruta[0]] for fruta in frutas if (fruta[2] == min(precios)) | (fruta[0] == 1)]
print(resultado)