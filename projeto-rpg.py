
#Escolha de classe

#começa a aventura # ENredo básico

#escolhas, e essas escolhas levam eles até outros lugares.
#DND comso base

nome = str(input('Olá aventureiro(a), como vai? Serei seu mestre nessa jogatina! Me diga como devo chama-lo: '))

print(f'Prazer em conhece-lo(a) {nome}, espero que esteja pronto para nossa aventura!')

print(f'{nome}, você precisará fazer a escolha da sua classe, isso irá impactar em sua jogatina!')

classes = ['Guerreiro, Arqueiro, Mago e Ladino']

print(f'A lista de classes é: {classes}')

escolha = str(input('Qual delas você escolhe?: '))

if escolha == classes[0]:
    print('Ah, então você preferiu brandir uma espada, muito bem!')
    concordancia = str(input('Quer continuar com esta classe? Sim ou Não: '))
    if concordancia != 'Sim':
        try:
            
    
    
elif escolha == classes[1]:
    print('Então você ')