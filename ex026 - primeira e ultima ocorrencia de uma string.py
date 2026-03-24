#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).strip().upper()
print(f"Você escreveu: {frase}")
print(f"A letra 'A' aparece na frase {frase.count('A')} vezes.\n"
      f"Ela aparece a primeira vez na posição {frase.find('A')+1} e\n"
      f"aparece pela última vez na posição {frase.rfind('A')+1}.")
