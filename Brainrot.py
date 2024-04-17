import random
import time
import msvcrt

# Dictionary containing all the phrases and their corresponding probabilities
phrases = {
    'Common': [
        ('Beta', 5),
        ('Gen Alpha', 10),
        ('Griddy', 20)
    ],
    'Uncommon': [
        ('Sprite Cranberry', 25),
        ('Blue Smurf Cat', 35),
        ('Big Chungus', 50),
        ('Super Idol', 75)
    ],
    'Rare': [
        ('Lebron Sunshine', 100),
        ('Hood Irony', 150),
        ('Airpod Shotty', 200),
        ('Livvy Dunne', 250)
    ],
    'Ultra Rare': [
        ('Grimace Shake', 1000),
        ('Adin Ross', 2500),
        ('Mogwarts', 5000),
        ('IShowSpeed', 10000)
    ],
    'Legendary': [
        ('TikTok Rizz party', 10000),
        ('Giga Chad', 25000),
        ('Mewing', 50000),
        ('Rizz', 100000)
    ],
    'Exotic': [
        ('Ohio', 250000),
        ('Fanum Tax', 500000),
        ('Among Us', 1000000),
        ('Ice Spice', 1500000)
    ],
    'Mythical': [
        ('Sigma', 2000000),
        ('Quandale Dingle', 5000000),
        ('Duke Dennis', 10000000),
        ('Kai Cenat', 20000000)
    ],
    'Interstellar': [
        ('Skibidi Toilet', 50000000)
    ]
}

def select_phrase():
    # Flatten the list of phrases and their odds into a single list
    all_phrases = [(phrase, rarity, odds) for rarity, category in phrases.items() for phrase, odds in category]
    
    # Create a weighted choice based on the odds
    total = sum(1 / odds for _, _, odds in all_phrases)
    r = random.uniform(0, total)
    upto = 0
    for phrase, rarity, odds in all_phrases:
        if upto + 1 / odds >= r:
            return phrase, rarity
        upto += 1 / odds

def main():
    last_roll_time = 0
    cooldown = 3  # 3 seconds cooldown

    print("Hello! | Welcome to Brainrot RNG! | Press Enter to roll for a brainrot phrase!")
    
    while True:
        current_time = time.time()
        
        # Check if Enter key is pressed
        if msvcrt.kbhit() and msvcrt.getch() == b'\r':
            if current_time - last_roll_time < cooldown:
                wait_time = cooldown - (current_time - last_roll_time)
                print(f"Hold up there buddy! You need to wait {wait_time:.1f} seconds until you can roll again.")
            else:
                selected_phrase, rarity = select_phrase()
                odds = [odds for phrase, odds in phrases[rarity] if phrase == selected_phrase][0]
                print(f"You rolled: {selected_phrase} | Rarity: {rarity} | Odds: 1 in {odds}")
                last_roll_time = current_time
        
        time.sleep(0.1)  # Sleep briefly to avoid busy-waiting

if __name__ == "__main__":
    main()
