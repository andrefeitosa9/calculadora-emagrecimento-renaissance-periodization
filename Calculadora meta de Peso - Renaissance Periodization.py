from time import sleep


peso_inicial = float(input(('Qual o seu peso atual? (Em kg)   ')))
while peso_inicial == 0:
    print("O seu peso atual deve ser maior que zero. Por favor, insira um valor válido.")
    peso_inicial = float(input('Qual a sua meta de peso? (Em kg)  '))
meta_peso = float(input('Qual a sua meta de peso? (Em kg)   '))
while meta_peso == 0:
    print("A meta de peso deve ser maior que zero. Por favor, insira um valor válido.")
    meta_peso = float(input('Qual a sua meta de peso? (Em kg)  '))

if meta_peso >= peso_inicial:
    print('A sua meta de peso deve ser menor que o seu peso inicial. Tente novamente.')
    peso_inicial = float(input(('Qual o seu peso atual? (Em kg)   ')))
    while peso_inicial == 0:
        print("O seu peso atual deve ser maior que zero. Por favor, insira um valor válido.")
        peso_inicial = float(input('Qual o seu peso atual? (Em kg)  '))
    meta_peso = float(input('Qual a sua meta de peso? (Em kg)   '))
    while meta_peso == 0:
        print("A meta de peso deve ser maior que zero. Por favor, insira um valor válido.")
        meta_peso = float(input('Qual a sua meta de peso? (Em kg)  '))

print()
print(f'O seu peso atual é de {peso_inicial}kg\nA sua meta de peso é de {meta_peso}kg.\nPerda total esperada: {(peso_inicial-meta_peso):.2f}kg')
print()
print('Calculando suas metas de emagrecimento por semana...')
sleep (2)

contador_semanas = 1
contador_ciclos = 1
peso_temporario = 0

while True:
    if contador_semanas == 13:
        contador_ciclos += 1
        print('\nVocê deve fazer um período de pelo menos 12 semanas de manutenção de peso para iniciar um próximo ciclo.')
        print('------ INÍCIO DO SEGUNDO CICLO ------\n')
    if contador_semanas == 25:
        print('\nVocê deve fazer um período de pelo menos 12 semanas de manutenção de peso para iniciar um próximo ciclo.')
        print('------ INÍCIO DO TERCEIRO CICLO ------\n')
        contador_ciclos += 1
    if contador_semanas == 37:
        print('\nVocê deve fazer um período de pelo menos 12 semanas de manutenção de peso para iniciar um próximo ciclo.')
        print('------ INÍCIO DO QUARTO CICLO ------\n')
        contador_ciclos += 1
    if contador_semanas == 1:
        peso_temporario = peso_inicial
    perda_semanal = (peso_temporario) - (peso_temporario*0.99)
    peso_temporario = peso_temporario*0.99
    print(f' O peso final na semana {contador_semanas} deve ser {peso_temporario:.2f} kg - Perda semanal de {perda_semanal:.2f}kg.')
    contador_semanas += 1
    if peso_temporario < (meta_peso*0.97):
        break
print(f'Você precisará de {contador_semanas-1} semanas em déficit para alcançar sua meta de peso, ou seja, {contador_ciclos} ciclo(s). ')

