# People Facts Dictionary Program
import random


people_facts = {
    "Jeff": ["is afraid of Dogs", "loves pizza", "can juggle"],
    "David": ["Plays the piano", "is a great cook", "speaks 3 languages"],
    "Jason": ["Can fly an airplane", "enjoys hiking", "collects stamps"],
    "Jill": ["Can hula dance", "is a yoga instructor", "loves reading"]
}

def display_person_facts(name):
    """Display all facts for a specific person"""
    if name in people_facts:
        print(f"{name}: {people_facts[name][0]}.")
        for fact in people_facts[name][1:]:
            print(f"{name}: {fact}.")
    else:
        print(f"No facts found for {name}.")

def change_random_fact(name):
    """Change a random fact for a person"""
    if name in people_facts and len(people_facts[name]) > 0:
        fact_index = random.randint(0, len(people_facts[name]) - 1)
        old_fact = people_facts[name][fact_index]
        
        new_fact = input(f"Enter new fact to replace '{old_fact}': ")
        people_facts[name][fact_index] = new_fact
        print(f"Updated {name}'s fact!")
    else:
        print(f"Cannot change fact for {name}.")

def run_program():
    """Main program loop"""
    print("=== PEOPLE FACTS PROGRAM ===")
    print("Available people:", ", ".join(people_facts.keys()))
    
    while True:
        print("\n" + "-"*40)
        
        
        for person in people_facts:
            display_person_facts(person)
        
        print(f"\n{'-'*40}")
        
   
        person_to_change = input("Enter person's name to change a fact (or 'quit' to exit): ").strip()
        
        if person_to_change.lower() == 'quit':
            break
        elif person_to_change in people_facts:
            change_random_fact(person_to_change)
        else:
            print("Person not found! Available people:", ", ".join(people_facts.keys()))

if __name__ == "__main__":
    run_program()