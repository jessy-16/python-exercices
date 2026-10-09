ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]

# CA par produit
for v in ventes:
    ca = v["prix"] * v["quantite"]
    print(f"{v['produit']} : {ca:.2f} €")

# CA total
ca_total = sum(v["prix"] * v["quantite"] for v in ventes)
print(f"CA total : {ca_total:.2f} €")

# Produit qui rapporte le plus
meilleur = max(ventes, key=lambda v: v["prix"] * v["quantite"])
print(f"Le produit qui rapporte le plus est : {meilleur['produit']}")