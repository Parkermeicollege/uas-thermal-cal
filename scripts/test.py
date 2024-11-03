from src import planck_exitance

planck_calculator = planck_exitance.Planck()
exitance = planck_calculator.exitance(8, 200)
print(exitance)