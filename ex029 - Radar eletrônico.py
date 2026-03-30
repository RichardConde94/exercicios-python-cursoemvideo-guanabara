#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


velocidade = int(input("Qual a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você está acima da velocidade e vai ser multado. O valor da sua multa será de R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade")