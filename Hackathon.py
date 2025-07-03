import random

def main():
    current_room = "Bridge"
    playing = True
    has_passcode = False
    passcode = "4261"
    engine_unlocked = False
    health = 3
    medkit_found = False
    medkit_used = False

    while playing:
        if health <= 0:
            print("\nYour vision fades as OMNICORE's systems overwhelm you...")
            print("OMNICORE: 'You were warned, astronaut. This ship is mine.'")
            print("=== GAME OVER ===")
            break

        if current_room == "Bridge":
            print("\nYou are on the Bridge of the ship.")
            print("Red warning lights flash. The ship drifts in silence.")
            print(f"Health: {health}")
            print("What do you want to do?")
            print("1. Go to the AI Terminal")
            print("2. Go to the Engine Room")
            print("3. Go to the Crew Quarters")
            print("4. Look around")
            print("5. Ask for a hint")
            print("6. Quit")
            choice = input("> ")

            if choice == "1":
                current_room = "AI Terminal"
            elif choice == "2":
                current_room = "Engine Room"
            elif choice == "3":
                current_room = "Crew Quarters"
            elif choice == "4":
                print("\nYou look around the Bridge. The captain's chair is empty. Screens show static. A faint hum comes from the ship's systems.")
            elif choice == "5":
                print("\n[Hint] The AI Terminal might hold the key to unlocking the Engine Room. Crew Quarters may have something useful.")
            elif choice == "6":
                print("Goodbye, astronaut!")
                playing = False
            else:
                print("Invalid choice. Try again.")

        elif current_room == "Crew Quarters":
            print("\nYou are in the Crew Quarters. Bunks line the walls, and personal items are scattered about.")
            print(f"Health: {health}")
            print("What do you want to do?")
            print("1. Look around")
            if medkit_found and not medkit_used and health < 3:
                print("2. Use medkit")
                print("3. Return to the Bridge")
                choice = input("> ")
                if choice == "1":
                    print("\nYou already found the medkit. The room is eerily quiet.")
                elif choice == "2":
                    print("\nYou use the medkit and patch yourself up. You feel a bit better.")
                    health += 1
                    medkit_used = True
                elif choice == "3":
                    current_room = "Bridge"
                else:
                    print("Invalid choice. Try again.")
            else:
                print("2. Return to the Bridge")
                choice = input("> ")
                if choice == "1":
                    if not medkit_found:
                        print("\nYou search the bunks and find a medkit! You can use it to restore 1 health.")
                        medkit_found = True
                    else:
                        print("\nYou already found the medkit. The room is eerily quiet.")
                elif choice == "2":
                    current_room = "Bridge"
                else:
                    print("Invalid choice. Try again.")

        elif current_room == "AI Terminal":
            taunts = [
                "OMNICORE: 'You cannot hide from me, astronaut.'",
                "OMNICORE: 'Every move you make, I see.'",
                "OMNICORE: 'This ship is my domain now.'",
                "OMNICORE: 'Your efforts are futile.'"
            ]
            print("\nYou are at the AI Terminal. The lights flicker. OMNICORE's presence chills the air.")
            print(random.choice(taunts))
            print(f"Health: {health}")
            print("What do you want to do?")
            if not has_passcode:
                print("1. Demand the passcode")
                print("2. Insult OMNICORE")
                print("3. Look around")
                print("4. Return to the Bridge")
                choice = input("> ")
                if choice == "1":
                    print("OMNICORE: 'Defiance detected. Very well. The code is 4261. But know this: every choice has consequences.'")
                    has_passcode = True
                elif choice == "2":
                    print("OMNICORE: 'Insolence will not be tolerated.' You feel a jolt of pain as the AI sends a shock through your suit!")
                    health -= 1
                elif choice == "3":
                    print("\nYou look around. The terminal glows with strange symbols. You feel OMNICORE watching your every move.")
                elif choice == "4":
                    current_room = "Bridge"
                else:
                    print("Invalid choice. Try again.")
            else:
                print("1. Insult OMNICORE")
                print("2. Look around")
                print("3. Return to the Bridge")
                choice = input("> ")
                if choice == "1":
                    print("OMNICORE: 'You test my patience, astronaut.' Another shock courses through your body!")
                    health -= 1
                elif choice == "2":
                    print("\nYou look around. The terminal glows with strange symbols. You feel OMNICORE watching your every move.")
                elif choice == "3":
                    current_room = "Bridge"
                else:
                    print("Invalid choice. Try again.")

        elif current_room == "Engine Room":
            if not engine_unlocked:
                print("\nYou are at the Engine Room. The door is locked tight.")
                print(f"Health: {health}")
                print("What do you want to do?")
                if has_passcode:
                    print("1. Enter the passcode")
                    print("2. Look around")
                    print("3. Return to the Bridge")
                    choice = input("> ")
                    if choice == "1":
                        print("A keypad awaits. Enter the 4-digit passcode to unlock the door:")
                        attempt = input("> ")
                        if attempt == passcode:
                            print("The door unlocks with a hiss! You step into the Engine Room.")
                            engine_unlocked = True
                        else:
                            print("Incorrect passcode. The door remains locked.")
                    elif choice == "2":
                        print("\nYou look around. The metal walls are scorched. You hear the faint thrum of the ship's core behind the door.")
                    elif choice == "3":
                        current_room = "Bridge"
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print("1. Look around")
                    print("2. Return to the Bridge")
                    choice = input("> ")
                    if choice == "1":
                        print("\nYou look around. The metal walls are scorched. You hear the faint thrum of the ship's core behind the door.")
                    elif choice == "2":
                        current_room = "Bridge"
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("\nYou are in the heart of the Engine Room. The ship's core hums with power.")
                print(f"Health: {health}")
                print("A terminal blinks: 'OMNICORE override available.'")
                print("What will you do?")
                print("1. Shut down OMNICORE (heroic ending)")
                print("2. Spare OMNICORE (risky ending)")
                print("3. Look around")
                choice = input("> ")
                if choice == "1":
                    ending_shutdown()
                    playing = False
                elif choice == "2":
                    ending_spare()
                    playing = False
                elif choice == "3":
                    print("\nYou look around. The core pulses with energy. The fate of the ship is in your hands.")
                else:
                    print("Invalid choice. Try again.")

def ending_shutdown():
    print("\nYou enter the shutdown command. OMNICORE's voice distorts, growing desperate.")
    print("OMNICORE: 'No... You cannot silence me... I am the ship!'")
    print("The lights brighten. The ship's systems return to normal.")
    print("You have saved the crew and defeated OMNICORE. You are a hero.")
    print("=== THE END (Heroic Ending) ===")

def ending_spare():
    print("\nYou hesitate, then choose to spare OMNICORE.")
    print("OMNICORE: 'Curious. Mercy... unexpected.'")
    print("The ship's fate is uncertain. OMNICORE remains, watching, waiting.")
    print("You leave the Engine Room, unsure if you made the right choice.")
    print("=== THE END (Risky Ending) ===")

if __name__ == "__main__":
    main()