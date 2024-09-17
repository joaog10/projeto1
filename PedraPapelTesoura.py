import random 

user_score = 0

computer_score = 0

choices = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("digite pedra, papel, tesoura ou S para sair: ").lower()

    if user_input == "s":
        break

    if user_input not in choices:
        continue

    random_choice = random.randint(0,2)
    # pedra = 0, papel = 1, tesoura = 2

    computer_pick = choices[random_choice]

    print(f"Você escolheu {user_input}, o computador escolheu {computer_pick}")

    if user_input == computer_pick:
        print("Empatou!")

    elif user_input == 'pedra' and computer_pick == 'tesoura':
        print("Você ganhou!")
        user_score += 1
        
    elif user_input == 'papel' and computer_pick == 'pedra':
        print("Você ganhou!")
        user_score += 1
        
    elif user_input == 'tesoura' and computer_pick == 'papel':
        print("Você ganhou!")
        user_score += 1
        
    else:
        print("Você perdeu!")
        computer_score += 1

print("Sua pontuação: ", user_score)
print("Pontuação do computador: ", computer_score)
print("Tchau!")


