from chemlib import Compound

#Formación de un compuesto
sulfato_sodio = Compound("Na2SO4")
print("Fórmula química:", sulfato_sodio.formula)

# Masa molar
masa_molar_Na2SO4 = sulfato_sodio.molar_mass()
print("Masa molar del sulfato de sodio (Na2SO4):", masa_molar_Na2SO4, "g/mol")

# Composición porcentual en masa
composicion_porcentual = sulfato_sodio.percent_composition()
print("Composición porcentual en masa del sulfato de sodio (Na2SO4):")
for elemento, porcentaje in composicion_porcentual.items():
    print(f" - {elemento}: {porcentaje:.2f}%")

# Estequiometría
# Ejemplo: Na + SO4 → Na2SO4
sodio = Compound("Na")
moles_Na = 2  # Suponemos que hay 2 moles de Na
razon_estequiometrica = sulfato_sodio.moles_product(moles_Na, "Na")
print(f"Con {moles_Na} moles de Na se producen {razon_estequiometrica:.2f} moles de Na2SO4")
