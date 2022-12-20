users = ["user1", "user2", "user3", "user4"]

print(users)
search = input("Get user position: ")

while True:

    position = -1
    for i in range(len(users)):
        if users[i] == search:
            position = i

    if position == 0:
        print(f"\nUser is in {position} position of the list.\n")
    else:
        print("\nUser does not exist.\n")

    print(users)
    search = input("Get user position: ")
