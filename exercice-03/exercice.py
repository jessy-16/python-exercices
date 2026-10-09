temperatures = [12.5,14,9.5,17,21,19.5,11]

moyenne = sum(temperatures) / len(temperatures)
print("La moyenne des températures est : %.2f" % moyenne)

minimum = min(temperatures)
print("La température minimale est : %.2f" % minimum)

maximum = max(temperatures)
print("La température maximale est : %.2f" % maximum)

#boucle
for i, temperature in enumerate(temperatures):
    print("Température %d : %.2f" % (i+1, temperature))

#en Fahrenheit
for i, temperature in enumerate(temperatures):
    fahrenheit = temperature * 9/5 + 32
    print(f"Température {i+1} en Fahrenheit : {fahrenheit:.2f}")

#afficher chaque jour
for i in range(len(temperatures)):
    print("Jour %d : %.2f" % (i+1, temperatures[i]))