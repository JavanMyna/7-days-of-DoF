#🧱 PHASE 2 — Make it feel like a “real system”

#CODE:
# 6:19pm 7th June, 67 dayyyy
# 8 pm, I added functions to lessen the lags and also to soothe my confusion and headache
# 8:50pm I added more events
import random

time = {
    'timeblock' : 'Morning' or 'Afternoon' or 'Night', 
    'Day' : 0 }
time['timeblock'] = 'Morning'

stats = {
    "energy" : 100,
    "focus" : 100,
    "cs_knowledge" : 1,
    "math_knowledge" : 2,
    "phy_knowledge" : 2 }

#Separate functions
def study_math():
    stats['energy'] -= 20
    stats['math_knowledge'] += 1 
    stats['focus'] -= 10
    print(f"\nYou studied math the whole {(time['timeblock']).lower()}.")

def study_cs():
    stats['energy'] -= 20
    stats['cs_knowledge'] += 1 
    stats['focus'] -= 10
    print(f"\nYou studied coding the whole {(time['timeblock']).lower()}.")

def study_phy():
    stats['energy'] -= 20
    stats['phy_knowledge'] += 1 
    stats['focus'] -= 10
    print(f"\nYou studied physics the whole {(time['timeblock']).lower()}.")    

def study_tired():
    print("-"*50)
    print(f"You are too tired to study!")
    print("-"*50)

def choice_scroll():
    print(f"\nYou chose to scroll around the entire {(time['timeblock']).lower()}.")
    stats['energy'] -= 10
    stats['focus'] -= 20
    print("You felt bad...")


#EVENTS
def fatigue_event():
    event = random.randint(1, 10)
    if event == 1:
        print("Mom asked you to buy something outside (energy(-10), bond(+5))")
    elif event == 2:
        print("Brother asked you about math (energy(-10), bond(+5))")
    elif event == 3:
        print("You are in charge in cooking the meal for the family (cooking(+10), energy(-10))")
    elif event == 4:
        print("You noticed signs of burnout after pushing yourself too hard recently.")
    elif event == 5:
        print("You somehow spent an hour watching random videos instead of studying.")
    else:
        pass

def study_event():
    event = random.randint(1, 15)
    if event == 1:
        print("A motivational video inspired you to study harder today.")
    elif event == 2:
        print("Everything clicked during your study session, making learning feel effortless.")
    elif event == 3:
        print("Your lecturer explained a difficult concept in a way that finally made sense.")
    elif event == 4:
        print("A discussion with your study group helped clear up several confusing topics.")
    else:
        pass

def funny_event():
    event = random.randint(1, 10)
    if event == 1:
        print("You opened YouTube to watch one tutorial and somehow ended up watching videos about ancient Roman plumbing.")
    elif event == 2:
        print("You planned a quick 10-minute break; your brain interpreted that as a 2-hour break.")
    elif event == 3:
        print("A classmate shared a study trick that surprisingly worked.")
    elif event == 4:
        print("Your notes were so organized today that even future-you would be impressed.")
    elif event == 5:
        print("You spent more time choosing a study playlist than actually studying.")
    else:
        pass

def life_event():
    event = random.randint(1, 10)
    if event == 1:
        print("A family gathering took up part of your day but improved your mood.")
    elif event == 2:
        print("A friend invited you out, giving you a chance to relax and recharge.")
    elif event == 3:
        print("An unexpected errand interrupted your plans for the afternoon.")
    elif event == 4:
        print("One of your commitments was cancelled, leaving you with extra free time.")
    else:
        pass

def random_event():
    type_event = random.randint(1, 4)
    tp = type_event
    if tp == 1:
        study_event()
    elif tp == 2:
        life_event()
    elif tp == 3:
        funny_event
    elif tp == 4:
        fatigue_event()


#Defining 

while True:
    print("")
    print(f"Day : {time['Day']}")
    print(f"\n---- Personal stats ----\nEnergy : {stats['energy']}\nFocus : {stats['focus']}\nKnowledge : \n1. Computer Science : lvl {stats['cs_knowledge']}\n2. Mathematics : lvl {stats['math_knowledge']}\n3. Physics : lvl {stats['phy_knowledge']}")
    if time['Day'] >= 7:
        print("A week has passed...")
        break
    if time['timeblock'] == 'Morning':
        print(f"It is {(time['timeblock']).lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n(Write 'stop' to stop the simulation)\nSelect 1-3: ").lower()
        if chc == '1':
            if stats['energy'] >= 20 and stats['focus'] >= 20:
                subject = input("Which subject do you want to study?\n1. Math\n2. Computer Science\n3. Physics\nEnter number 1-3: ")
                if subject == '1':
                    study_math()
                    time['timeblock'] = 'Afternoon'
                elif subject == '2':
                    study_cs()
                    time['timeblock'] = 'Afternoon'
                elif subject == '3':
                    study_phy()
                    time['timeblock'] = 'Afternoon'
            elif stats['energy'] < 20:
                study_tired()
            elif stats['focus'] < 20:
                print("\nYou tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            print(f"\nYou chose to rest and loiter around the entire {(time['timeblock']).lower()}.")
            if stats['energy'] + 10 >= 100:
                stats['energy'] = 100
            else:
                stats['energy'] += 10

            time['timeblock'] = 'Afternoon'
        elif chc == '3':
            choice_scroll()
            time['timeblock'] = 'Afternoon'
        elif chc == 'stop':
            print("\nStopping program\n")
            break
        else:
            print("\nInvalid choice!")
        print(f"Current Energy : {stats['energy']} \nCurrent Focus: {stats['focus']} \nCurrent Knowledge (Computer Science) : {stats['cs_knowledge']}")   
        print("")
        random_event()
        print("")
        print("---------------------------------------") 
        print("")

    if time['timeblock'] == 'Afternoon':
        print(f"It is {(time['timeblock']).lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n(Write 'stop' to stop the simulation)\nSelect 1-3: ").lower()
        if chc == '1':
            if stats['energy'] >= 20 and stats['focus'] >= 20:
                subject = input("Which subject do you want to study?\n1. Math\n2. Computer Science\nEnter number 1-2: ")
                if subject == '1':
                    study_math()
                    time['timeblock'] = 'Night'
                elif subject == '2':
                    study_cs()
                    time['timeblock'] = 'Night'
            elif stats['energy'] < 20:
                study_tired()
            elif stats['focus'] < 20:
                print("\nYou tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            print(f"\nYou chose to rest and loiter around the entire {(time['timeblock']).lower()}.")
            if stats['energy'] + 10 >= 100:
                stats['energy'] = 100
            else:
                stats['energy'] += 10
            time['timeblock'] = 'Night'
        elif chc == '3':
            choice_scroll()
            time['timeblock'] = 'Night'
        elif chc == 'stop':
            print("\nStopping program\n")
            break
        else:
            print("\nInvalid choice!")
        print(f"Current Energy : {stats['energy']} \nCurrent Focus: {stats['focus']} \nCurrent Knowledge (Computer Science) : {stats['cs_knowledge']}")   
        print("")
        random_event()
        print("")
        print("---------------------------------------")         
        print("")


    if time['timeblock'] == 'Night':
        print(f"It is {(time['timeblock']).lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n(Write 'stop' to stop the simulation)\nSelect 1-3: ").lower()
        if chc == '1':
            if stats['energy'] >= 20 and stats['focus'] >= 20:
                subject = input("Which subject do you want to study?\n1. Math\n2. Computer Science\nEnter number 1-2: ")
                if subject == '1':
                    study_math()
                    time['timeblock'] = 'Afternoon'
                elif subject == '2':
                    study_cs()
                    time['timeblock'] = 'Afternoon'
            elif stats['energy'] < 20:
                study_tired()
            elif stats['focus'] < 20:
                print("\nYou tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            print(f"\nYou chose to rest and loiter around the entire {(time['timeblock']).lower()}.")
            if stats['energy'] + 10 >= 100:
                stats['energy'] = 100
            else:
                stats['energy'] += 10
            time['timeblock'] = 'Morning'
        elif chc == '3':
            choice_scroll()
            time['timeblock'] = 'Morning'
        elif chc == 'stop':
            print("\nStopping program\n")
            break
        else:
            print("\nInvalid choice!")
        print(f"Current Energy : {stats['energy']} \nCurrent Focus: {stats['focus']} \nCurrent Knowledge (Computer Science) : {stats['cs_knowledge']}")   
        print("")
        random_event()
        print("You went to sleep afterwards...")
        if stats['energy'] + 50 > 100:
            stats['energy'] = 100
        else:
            stats['energy'] = stats['energy'] + 50
        
        print("="*50)      
        print("")  
        time['Day'] += 1        
