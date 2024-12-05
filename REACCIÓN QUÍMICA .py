from chemlib import Reaction

# Formación de una reacción
# Ejemplo: 2Na + SO4 → Na2SO4
reaccion = Reaction({"Na": 2, "SO4": 1}, {"Na2SO4": 1})

# Balanceo de la ecuación
print("Ecuación antes de balancear:", reaccion.unbalanced_equation)
print("Ecuación balanceada:", reaccion.formula)

# Información adicional de la reacción
print("¿Está balanceada la reacción?", reaccion.is_balanced())
