hour_now = int(input("Add meg a mostani idő óráját: "))
alarm_time = int(input("Add meg hány órával később szólaljon meg az ébresztő: "))
result = alarm_time + hour_now

if result >= 24:
    print(f"Az ébresztés ideje: {result - 24} óra.")
else:
    print(f"Az ébresztés ideje: {result} óra.")
