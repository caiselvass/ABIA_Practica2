import pandas as pd
import matplotlib.pyplot as plt

while True:
    try:
        experiment = input('\nQuin experiment vols representar? [1/2/3]: ').replace(' ', '')
        if experiment not in ['1', '2', '3']:
            raise ValueError
    except ValueError:
        print("Error: Introdueix només un dels següents valors: 1, 2, 3.")
        continue
    break

if experiment == '1':
    df = pd.read_csv('./data/experiment1.csv')

    while True:
        try:
            extensio: str = input('\nQuina extensió vols representar? [B/1/2/3): ').replace(' ', '')
            extensio = 'B' if extensio == 'b' else extensio
            if experiment not in ['B', '1', '2', '3']:
                raise ValueError
        except ValueError:
            print("Error: Introdueix només un dels següents valors: B, 1, 2, 3.")
            continue
        break
        
    df = df[df['Extensió'] == extensio]

    # Convertir les comes a punts per a poder ser llegides com a números
    df['Temps'] = df['Temps'].str.replace(',', '.').astype(float)

    # Crear el gràfic
    plt.figure(figsize=(10, 6))
    plt.plot(df['N llibres'], df['Temps'], marker='o')  
    plt.xlabel('N Llibres')
    plt.ylabel('Temps')
    plt.title('Temps en funció del nombre de llibres')
    plt.grid(True)
    plt.savefig('./plots/experiment1_{}.png'.format(extensio))
    plt.show()

