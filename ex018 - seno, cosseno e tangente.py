#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


from math import cos, sin, tan, radians

angulo = float(input("Digite um ângulo: "))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f"O angulo de {angulo} tem o seno {seno:.2f}, o cosseno {cosseno:.2f} e a tangente {tangente:.2f}")