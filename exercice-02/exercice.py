temperature : float

temperature = float(input("Entrez la température : "))


if temperature < 0:
    print("%s°C : gel" % temperature)
elif temperature < 15:
    print("%s°C : froid" % temperature)
elif temperature < 25:
    print("%s°C : doux" % temperature)
else:
    print("%s°C : chaud" % temperature)

année : int

année = int(input("Entrez une année : "))

if année % 4 == 0 and (année % 100 != 0 or année % 400 == 0):
    print("%s : année bissextile" % année)