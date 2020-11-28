import Controllers.customer_controller as cc
import Controllers.car_model_controller as cmc
import Controllers.contact_person_controller as cpc
from UI.tools import int_input


def show_customer(chosen_customer):
    print("     KUNDBILD     ")
    print("------------------")
    print(f"Namn: {chosen_customer.name} ({str(chosen_customer.customer_type)})")

    if chosen_customer.contact_person:
        print(f"Kontaktperson: {chosen_customer.contact_person}")

    print(f"Address: {chosen_customer.street_address}")
    print(f"Postkod: {chosen_customer.zip_code}")
    print(f"Email: {chosen_customer.email}")
    print(f"Telefonnummer: {chosen_customer.phone}")

    if chosen_customer.orders:
        print("------------------")
        print("Ordrar:")
        for order in chosen_customer.orders:
            print(order)
        print("------------------")

    if chosen_customer.customer_cars:
        print("------------------")
        print("Bilar:")
        for car in chosen_customer.customer_cars:
            print(car)
        print("------------------")

    show_customer_menu(chosen_customer)


def find_customer_menu():
    while True:
        print("----------------------")
        print("SÖK UPP BEFINTLIG KUND")
        print("1. Sök efter namn")
        print("2. Sök efter id")
        print("3. Sök efter telefonnummer")
        print("4. Avbryt")

        choice = input("> ")

        if choice == "1":
            keyword = input("Ange namn: ")
            customers = cc.find_customer_by_name(keyword)
            if customers:
                choose_customer(customers)
                break
            else:
                print("Det finns ingen kund som uppfyller sökkraven")

        elif choice == "2":
            keyword = int_input("Ange id: ")
            customers = cc.find_customer_by_id(keyword)
            if customers:
                choose_customer(customers)
                break
            else:
                print("Det finns ingen kund som uppfyller sökkraven.")

        elif choice == "3":
            keyword = input("Ange telefonnumer: ")
            customers = cc.find_customer_by_phone(keyword)
            if customers:
                choose_customer(customers)
                break
            else:
                print("Det finns ingen kund som uppfyller sökkraven.")

        elif choice == "4":
            break

        else:
            print("Felaktig inmatning.")


def choose_customer(customers):
    if len(customers) == 1:
        customer = customers[0]
        print(customer)
        show_customer(customer)

    else:
        print("Matchande sökningar:")
        for i, customer in enumerate(customers):
            print(f"{i + 1}. {customer}")

        while True:
            print("Vilken kund vill du visa?")
            customer_choice = int_input("> ")
            if 1 <= customer_choice <= len(customers):
                customer = customers[customer_choice - 1]
                show_customer(customer)
                break
            else:
                print("Felaktig inmatning.")


def show_customer_menu(chosen_customer):
    while True:
        print("------------------")
        print(f"Vad vill du göra med {chosen_customer}")
        print("1. Redigera kunden")
        print("2. Lägg till bil")
        print("3. Ta bort bil")
        print("4. Lägg till order")
        print("5. Ta bort kunden")
        print("6. Avbryt")

        selected = input("> ")

        if selected == "1":
            edit_customer(chosen_customer)

        elif selected == "2":
            add_car(chosen_customer.id)

        elif selected == "3":
            remove_car_menu()
            pass

        elif selected == "4":
            place_order()

        elif selected == "5":
            remove_customer(chosen_customer)
            break

        elif selected == "6":
            break

        else:
            print("Felaktig inmatning")


def add_car(customer_id):
    print("-------------------")
    print("LÄGGA TILL BIL")
    print("Ange uppgifter på den bil du vill lägga till")

    regnr = input("Regnummer: ")

    while True:
        car_model_id = int_input("Bilmodel (id): ")
        if not cmc.find_car_model_by_id(car_model_id):
            print(f"Hittade ingen bilmodell med id {car_model_id}")
        else:
            break

    color = input("Bilfärg: ")
    c = (customer_id, regnr, car_model_id, color)
    added_string = cc.add_car(c)
    print(added_string)


def remove_car_menu():

    print("Ange regnummret på den bil du vill ta bort")

    while True:
        regnr = input("> ")
        found_car = cc.find_customer_car(regnr)
        print(found_car)

        if found_car:
            print(f"Är du säker på att du vill ta bort denna bil?")
            print(f"Modell: {found_car.car_model} | Regnummer: {found_car.regnr} | Ägare: {found_car.customer}")
            print("1. Ja")
            print("2. Nej")
            selected = int_input("> ")

            if selected == 1:
                cc.remove_customer_car(found_car)
                removed_string = cc.remove_customer_car(found_car)
                print(removed_string)
                break

            elif selected == 2:
                break

        else:
            print(f"Hittade ingen bil med id {regnr}")


def add_new_customer():
    pass


def remove_customer(chosen_customer):
    while True:
        print("----------------")
        print("TA BORT KUND")
        print(f"Är du säker på att du vill ta bort denna kunden?")
        print(f"{chosen_customer} ({chosen_customer.id})")
        print("1. Ja")
        print("2. Nej")

        selected = int_input("> ")
        if selected == 1:
            cc.remove_customer(chosen_customer)
            removed_string = cc.remove_customer(chosen_customer)
            print(removed_string)
            break

        elif selected == 2:
            break

        else:
            print("Felaktig inmatning")


def place_order():
    pass


def edit_customer(chosen_customer):
    while True:
        print("--------------")
        print(f"REDIGERA KUND")
        print(f"1. Namn: {chosen_customer.name}")
        print(f"2. Address: {chosen_customer.street_address}")
        print(f"3. Postkod: {chosen_customer.zip_code}")
        print(f"4. Email: {chosen_customer.email}")
        print(f"5. Telefonnummer: {chosen_customer.phone}")

        if chosen_customer.contact_person:
            print(f"6. Konkaktperson: {chosen_customer.contact_person}")
        print(f"7. Avbryt")
        print(f"Vilken rad vill du redigera?")
        selected = input("> ")

        if selected == "1":
            chosen_customer.name = input("Ange nytt namn: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "2":
            chosen_customer.name = input("Ange ny address): ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "3":
            chosen_customer.zip_code = input("Ange ny postkod: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "4":
            chosen_customer.email = input("Ange ny mail: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "5":
            chosen_customer.phone = input("Ange nytt telefonnummer: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "6":
            while True:
                cp_id = input("Ange id för den nya kontaktpersonen: ")

                if cpc.find_contact_person(cp_id):
                    chosen_customer.contact_id = cp_id
                    changed_string = cc.save_changes(chosen_customer)
                    print(changed_string)
                    break

                else:
                    print(f"Hittade ingen kontaktperson med id {cp_id}")

        elif selected == "7":
            break
        else:
            print("Felaktig inmatning")


def main():
    pass


if __name__ == "__main__":
    main()
