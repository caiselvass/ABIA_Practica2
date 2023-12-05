import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

while True:
    try:
        experiment = input('Quin experiment vols representar? [1, 2]: ')
        if experiment not in ['1', '2']:
            raise ValueError
    except ValueError:
        print("Error: Introdueix només un dels següents valors: 1, 2.")
        continue
    break

if experiment == '1':
    df = pd.read_csv('./experiments/data/experiment1.csv')

    while True:
        try:
            extensio: str = str(input('Quina extensió vols representar? [B, 1]: '))
            extensio = 'B' if extensio == 'b' else extensio
            if experiment not in ['B', '1']:
                raise ValueError
        except ValueError:
            print("Error: Introdueix només un dels següents valors: B, 1.")
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
    plt.savefig(f'./experiments/plots/experiment1_{extensio}.png')
    plt.show()
    print(f"\t* S\'ha guardat la gràfica 'experiment1_{extensio}.png' en el directori 'experiments/plots'.")

elif experiment == '2':
    data = pd.read_csv('./experiments/data/experiment2.csv')
    # Setting the aesthetic style of the plots
    sns.set(style="whitegrid")

    # Creating subplots for different variables
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Plotting the relationships
    sns.lineplot(ax=axes[0, 0], data=data, x="NÚMERO LLIBRES", y="STATES", hue="TIPUS")
    axes[0, 0].set_title('Number of Books vs States')
    print('States plot saved')

    sns.lineplot(ax=axes[0, 1], data=data, x="NÚMERO LLIBRES", y="MAXDEPTH", hue="TIPUS")
    axes[0, 1].set_title('Number of Books vs Max Depth')
    print('Max Depth plot saved')

    sns.lineplot(ax=axes[1, 0], data=data, x="NÚMERO LLIBRES", y="EASY", hue="TIPUS")
    axes[1, 0].set_title('Number of Books vs Easy Actions')

    sns.lineplot(ax=axes[1, 1], data=data, x="NÚMERO LLIBRES", y="HARD ACTION", hue="TIPUS")
    axes[1, 1].set_title('Number of Books vs Hard Actions')

    # Save the plot as Experimento2.png
    plt.savefig('./experiments/plots/experiment2.png')
    plt.show()
    print("\t* S\'ha guardat la gràfica 'experiment2.png' en el directori 'experiments/plots'.")

    # Create a plot to visualize the relationship between the time and the number of books
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="NÚMERO LLIBRES", y="TEMPS", hue="TIPUS")
    plt.title('Temps vs Número de Llibres')
    plt.xlabel('Número de Llibres')
    plt.ylabel('Temps (en segons)')

    # Save the plot as Experiment2_2.png
    plt.savefig('./experiments/plots/experiment2_2.png')
    print("\t* S\'ha guardat la gràfica 'experiment2_2.png' en el directori 'experiments/plots'.")