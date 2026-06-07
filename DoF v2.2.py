#🧱 PHASE 2 — Make it feel like a “real system”

#CODE:
# Starting from 10:15pm 7th June 2026
# Yeyyyy it works! : 11:09pm 7th June 2026

#MY INTENTIONS:
#- Create class for student and define their choice (yippeee) 
#- Create class for event for convenience and compact
#- I intend to change focus into sanity later, sooo at some point at a low sanity, they will burn out (but not yet)

#What changed? :
#- I replaced the list of dictionary with just the class utilizing "player.stats_detail" instead of "player.stats['stats_detail']"
#- I created a class for student and event so i can click the >< thingy to make it compact. 
#- I still dont know how to make the day cycle, like rotate, mornign to afternoon to night then back to morning, it seems like I still depend on making it go to a specific daytime
import random

time = {
    'timeblock' : 'Morning' or 'Afternoon' or 'Night', 
    'Day' : 0 }
time['timeblock'] = 'Morning'

#stats = {
#    "energy" : 100,
#    "focus" : 100,
#    "cs_knowledge" : 1,
#    "math_knowledge" : 1,
#    "phy_knowledge" : 1 }

class Student:
    def __init__(self, name):
        self.name = name
        #I feel like this is better because its specifically for that person
        #For some reason i cant use student. or Student when picking it back up 
        self.energy = 100
        self.focus = 100
        self.cs_knowledge = 1
        self.math_knowledge = 1
        self.phy_knowledge = 1

    def study_math(self):
        self.energy -= 20
        self.math_knowledge += 1 
        self.focus -= 10
        print(f"\nYou studied math the whole {(time['timeblock']).lower()}.")

    def study_cs(self):
        self.energy -= 20
        self.cs_knowledge += 1 
        self.focus -= 10
        print(f"\nYou studied coding the whole {(time['timeblock']).lower()}.")

    def study_phy(self):
        self.energy -= 20
        self.phy_knowledge += 1 
        self.focus -= 10
        print(f"\nYou studied physics the whole {(time['timeblock']).lower()}.")    

    def study_tired(self):
        print("-"*50)
        print(f"You are too tired to study!")
        print("-"*50)

    def choice_scroll(self):
        print(f"\nYou chose to scroll around the entire {(time['timeblock']).lower()}.")
        self.energy -= 10
        self.focus -= 20
        print("You felt bad...")
player = Student("Fred")

#EVENTS
class Event:
    def fatigue_event(self):
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

    def study_event(self):
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

    def funny_event(self):
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

    def life_event(self):
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

    def random_event(self):
        type_event = random.randint(1, 4)
        tp = type_event
        if tp == 1:
            event.study_event()
        elif tp == 2:
            event.life_event()
        elif tp == 3:
            event.funny_event
        elif tp == 4:
            event.fatigue_event()
event = Event()

#Defining 

while True:
    #global stats #Does thsi even make a changeee?? why are they yellow underlining my stats adn how do I refer it as thennn
    print("")
    print(f"Day : {time['Day']}")
    print(f"\n---- Personal stats ----\nEnergy : {player.energy}\nFocus : {player.focus}\nKnowledge : \n1. Computer Science : lvl {player.cs_knowledge}\n2. Mathematics : lvl {player.math_knowledge}\n3. Physics : lvl {player.phy_knowledge}")
    if time['Day'] >= 7:
        print("A week has passed...")
        break
    if time['timeblock'] == 'Morning':
        print(f"It is {(time['timeblock']).lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n(Write 'stop' to stop the simulation)\nSelect 1-3: ").lower()
        if chc == '1':
            if player.energy >= 20 and player.focus >= 20:
                subject = input("Which subject do you want to study?\n1. Math\n2. Computer Science\n3. Physics\nEnter number 1-3: ")
                if subject == '1':
                    player.study_math()
                    time['timeblock'] = 'Afternoon'
                elif subject == '2':
                    player.study_cs()
                    time['timeblock'] = 'Afternoon'
                elif subject == '3':
                    player.study_phy()
                    time['timeblock'] = 'Afternoon'
            elif player.energy < 20:
                player.study_tired()
            elif player.focus < 20:
                print("\nYou tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            print(f"\nYou chose to rest and loiter around the entire {(time['timeblock']).lower()}.")
            if player.energy + 10 >= 100:
                player.energy = 100
            else:
                player.energy += 10

            time['timeblock'] = 'Afternoon'
        elif chc == '3':
            player.choice_scroll()
            time['timeblock'] = 'Afternoon'
        elif chc == 'stop':
            print("\nStopping program\n")
            break
        else:
            print("\nInvalid choice!")
        print(f"Current Energy : {player.energy}\nFocus : {player.focus}\nKnowledge : \n1. Computer Science : lvl {player.cs_knowledge}\n2. Mathematics : lvl {player.math_knowledge}\n3. Physics : lvl {player.phy_knowledge}")
        print("")
        event.random_event()
        print("")
        print("---------------------------------------") 
        print("")

    if time['timeblock'] == 'Afternoon':
        print(f"It is {(time['timeblock']).lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n(Write 'stop' to stop the simulation)\nSelect 1-3: ").lower()
        if chc == '1':
            if player.energy >= 20 and player.focus >= 20:
                subject = input("Which subject do you want to study?\n1. Math\n2. Computer Science\n3. Physics\nEnter number 1-3: ")
                if subject == '1':
                    player.study_math()
                    time['timeblock'] = 'Night'
                elif subject == '2':
                    player.study_cs()
                    time['timeblock'] = 'Night'
                elif subject == '3':
                    player.study_phy()
                    time['timeblock'] = 'Night'
            elif player.energy < 20:
                player.study_tired()
            elif player.focus < 20:
                print("\nYou tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            print(f"\nYou chose to rest and loiter around the entire {(time['timeblock']).lower()}.")
            if player.energy + 10 >= 100:
                player.energy = 100
            else:
                player.energy += 10

            time['timeblock'] = 'Night'
        elif chc == '3':
            player.choice_scroll()
            time['timeblock'] = 'Night'
        elif chc == 'stop':
            print("\nStopping program\n")
            break
        else:
            print("\nInvalid choice!")
        print(f"Current Energy : {player.energy}\nFocus : {player.focus}\nKnowledge : \n1. Computer Science : lvl {player.cs_knowledge}\n2. Mathematics : lvl {player.math_knowledge}\n3. Physics : lvl {player.phy_knowledge}")        
        print("")
        event.random_event()
        print("")
        print("---------------------------------------")         
        print("")


    if time['timeblock'] == 'Night':
        print(f"It is {(time['timeblock']).lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n(Write 'stop' to stop the simulation)\nSelect 1-3: ").lower()
        if chc == '1':
            if player.energy >= 20 and player.focus >= 20:
                subject = input("Which subject do you want to study?\n1. Math\n2. Computer Science\n3. Physics\nEnter number 1-3: ")
                if subject == '1':
                    player.study_math()
                    time['timeblock'] = 'Morning'
                elif subject == '2':
                    player.study_cs()
                    time['timeblock'] = 'Morning'
                elif subject == '3':
                    player.study_phy()
                    time['timeblock'] = 'Morning'
            elif player.energy < 20:
                player.study_tired()
            elif player.focus < 20:
                print("\nYou tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            print(f"\nYou chose to rest and loiter around the entire {(time['timeblock']).lower()}.")
            if player.energy + 10 >= 100:
                player.energy = 100
            else:
                player.energy += 10

            time['timeblock'] = 'Morning'
        elif chc == '3':
            player.choice_scroll()
            time['timeblock'] = 'Morning'
        elif chc == 'stop':
            print("\nStopping program\n")
            break
        else:
            print("\nInvalid choice!")
        print(f"Current Energy : {player.energy}\nFocus : {player.focus}\nKnowledge : \n1. Computer Science : lvl {player.cs_knowledge}\n2. Mathematics : lvl {player.math_knowledge}\n3. Physics : lvl {player.phy_knowledge}")  
        print("")
        event.random_event()
        print("You went to sleep afterwards...")
        if player.energy + 50 > 100:
            player.energy = 100
        else:
            player.energy = player.energy + 50
        
        print("="*50)      
        print("")  
        time['Day'] += 1        

