# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random


def wow_mount_contest():
    # List of rare WoW dungeon/raid mounts
    mounts = [
        "Rivendare's Deathcharger (Stratholme)",
        "Midnight (Return to Karazhan)",
        "Ashes of Al'ar (The Eye)",
        "Invincible (Icecrown Citadel)",
        "Mimiron's Head (Ulduar)",
        "Flame Talon of Alysrazor (Firelands)",
        "Pureblood Fire Hawk (Firelands)",
        "Life-Binder's Handmaiden (Dragon Soul)",
        "Blazing Drake (Dragon Soul)",
        "Experiment 12-B (Dragon Soul)",
        "Astral Cloud Serpent (Mogu'shan Vaults)",
        "Heavenly Onyx Cloud Serpent (Siege of Orgrimmar)",
        "Felsteel Annihilator (Hellfire Citadel)",
        "Antoran Charhound (Antorus)",
        "Spawn of Galakras (Siege of Orgrimmar)"
    ]

    player_score = 0
    computer_score = 0

    print("=== World of Warcraft Mount Drop Contest! ===")
    print(f"We'll be rolling for {len(mounts)} rare mounts!\n")

    for mount in mounts:
        input(f"Press Enter to roll for {mount}...")

        player_roll = random.randint(1, 100)
        computer_roll = random.randint(1, 100)

        print(f"\nYou rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")

        if player_roll > computer_roll:
            player_score += 1
            print(f"You won the {mount}!")
        elif computer_roll > player_roll:
            computer_score += 1
            print(f"Computer won the {mount}!")
        else:
            print(f"Tie! No one gets the {mount}.")

        print(f"Current score - You: {player_score} | Computer: {computer_score}\n")

    print("\n=== Final Results ===")
    print(f"You collected {player_score} mounts")
    print(f"Computer collected {computer_score} mounts")

    if player_score > computer_score:
        print("Congratulations! You won the mount contest!")
    elif computer_score > player_score:
        print("The computer wins this time. Better luck next time!")
    else:
        print("It's a tie! You and the computer are equally lucky!")


# Run the game
if __name__ == "__main__":
    wow_mount_contest()
