def show_menu():
    print("\n--- Mashin Hesab Sade ---")
    print("1. Jam")
    print("2. Tafrigh")
    print("3. Zarb")
    print("4. Taghsim")
    print("0. Khorooj")

def get_numbers():
    try:
        num1 = float(input("Adade aval: "))
        num2 = float(input("Adade dovom: "))
        return num1, num2
    except ValueError:
        print("Lotfan faghat adad vared kon!")
        return get_numbers()

def calculator():
    while True:
        show_menu()
        choice = input("Entekhab kon (0 ta 4): ")

        if choice == '0':
            print("Khorooj az mashin hesab. Khodahafez!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Gozineye namotabar! Dobare talash kon.")
            continue

        num1, num2 = get_numbers()

        if choice == '1':
            result = num1 + num2
            print(f"Nateije: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Nateije: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Nateije: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Khatta: Taghsim bar sefr emkan pazir nist!")
            else:
                result = num1 / num2
                print(f"Nateije: {num1} / {num2} = {result}")

calculator()
