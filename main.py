num_1 = input("Vvedite pervoe chislo:")
num_2 = input("Vvedite vtoroe chislo:")
try:
    print(float(num_1)/float(num_2))
except ZeroDivisionError:
    print("Vtoroe chislo ne dolzhno bit 0")
except ValueError:
    print("Ne tot tip dannih, vvedite chisla")
except Exception:
    print("ischi oshibku")
