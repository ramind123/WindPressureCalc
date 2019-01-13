#Program to calculate wind pressure on 8" x 8" junction box.
def pressure_in_newtons(wind_speed):
    Fw = (1/2) * (1.3) * (pow(wind_speed, 2)) * (1)
    result = convert_n_to_kg(Fw)
    return result
def convert_n_to_kg(N):
    Kg = N / 10
    return Kg
#Program Interface:
wind = input("Enter wind velocity in m/s.")
wind = int(wind)
variable = pressure_in_newtons(wind)
print("Wind pressure force on the junction box is " + str(variable) + " Kgs.")
