from salt_in_solution import SaltDilutionGauging

config = load_config("dil_config.ini")

csv_path = "./calibration.csv"
csv_trial = "./output/20250709_144014_790478.csv"

calibrate = SaltDilutionGauging.from_calibration_csv(csv_path)
discharge = SaltDilutionGauging.estimate_Q_from_csv(csv_trial, 13.0)

print("RC_sec:", calibrate.RC_sec)
print("k value:", calibrate.k)
print("RC values:", calibrate.RC_values)
print("EC values:", calibrate.EC_values)
print("Estimate of Q:", discharge)