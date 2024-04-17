import random
import time
import msvcrt
from phrases_data import phrases

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
