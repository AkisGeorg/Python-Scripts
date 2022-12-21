total_drivers = 0
attempts = 0

min_name = ""
min_time = 181

for i in range(36):
    name = input("Όνομα οδηγού: ")
    time = int(input("Χρόνος οδηγού σε δευτερόλεπτα: "))
    if time <= 180:
        print(f"\nO οδηγός {name} με χρόνο {time} δευτερόλεπτα, μπορεί να συμμετάσχει στον αγώνα.\n")
        total_drivers += 1
    elif time > 180:
        attempts += 1
        print("ΜΗ ΣΥΜΜΕΤΟΧΗ")
    else:
        print("ΜΗ ΣΥΜΜΕΤΟΧΗ")

    if time <= min_time:
        min_name = name
        min_time = time

print("=========================================")
print(f"Ο χαμηλότερος χρόνος είναι αυτός του {min_name} με χρόνο {min_time} δευτερόλεπτα, από το σύνολο των {total_drivers} οδηγών.")
print("=========================================")





