fuel_level = int(input("Add meg mennyi üzemanyag van a tankodban: "))
fuel_consumption = int(input("Add meg az autód fogyasztását (l/100 km): "))
distance = (fuel_level/fuel_consumption)*100
print(f"Ennyi km-t tudsz megtenni az autóddal: {distance:.0f}")