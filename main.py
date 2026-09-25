def simular_fila(clientes):
    ordem = sorted(clientes, key=lambda x: x[1])
    fila1 = []
    fila2 = []
    for i in range(len(ordem)):
        if i % 2 == 0:
            fila1.append(ordem[i])
        else:
            fila2.append(ordem[i])
    
    espera1 = 0
    espera2 = 0
    tempo_atual1 = 0
    tempo_atual2 = 0
    
    for cliente in fila1:
        if cliente[1] > tempo_atual1:
            tempo_atual1 = cliente[1]
        espera1 += tempo_atual1 - cliente[1]
        tempo_atual1 += 5
        
    for cliente in fila2:
        if cliente[1] > tempo_atual2:
            tempo_atual2 = cliente[1]
        espera2 += tempo_atual2 - cliente[1]
        tempo_atual2 += 5
        
    return espera1 + espera2

clientes = [("Ana", 0), ("Beto", 5), ("Carla", 10), ("Davi", 12)]
resultado = simular_fila(clientes)
print("Tempo total de espera:", resultado, "minutos")