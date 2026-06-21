# 🧱 Phase 3 
# From 5:38pm of 11 June 2026

#MY INTENTIONS:
#- I wanna refactor the Event class > hmm i tried but im kinda tired

#What changed? :
#- Just small refactor and bug fix i think

#Thoughts :
#- I deleted some bit of my save function as it isnt working, maybe its beyond what I understand so maybe lets focus on other stuff.

#CODE:
import random
#import json
running = True
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
    
    def intro_rand_event(self):
        print("-"*50)
        print("Random event log : ")

    def random_event(self):
        type_event = random.randint(1, 4)
        tp = type_event
        if tp == 1:
            event.intro_rand_event()
            event.study_event()
        elif tp == 2:
            event.intro_rand_event()
            event.life_event()
        elif tp == 3:
            event.intro_rand_event()
            event.funny_event()
        elif tp == 4:
            event.intro_rand_event()
            event.fatigue_event()
        else:
            pass

class Time: 
    def __init__(self):
        self.current_index = 0 
        self.current_day = 0   
    time_states = [ "Morning", "Afternoon", "Night" ]     

    def day_progress(self):
        self.current_index = (self.current_index + 1) % len(self.time_states) 
        return self.current_index
        
    def timeblock_progress(self):
        global running 
        print(f"It is {self.time_states[self.current_index].lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n4. View your stats\n(Write 'stop' to stop the simulation)\nSelect 1-4: ").lower() #Option \n5. Settings is hidden as I skip this
        if chc == '1':
            if player.energy >= 20 and player.focus >= 20:
                subject = input("\nWhich subject do you want to study?\n1. Math\n2. Computer Science\n3. Physics\nEnter number 1-3: ")
                if subject == '1':
                    player.study_math()
                    self.day_progress()
                elif subject == '2':
                    player.study_cs()
                    self.day_progress()
                elif subject == '3':
                    player.study_phy()
                    self.day_progress()
            elif player.energy < 20:
                player.study_tired()
                return
            elif player.focus < 20:
                print("")
                print("-"*50)
                print("You tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            player.choice_rest()
            self.day_progress()
        elif chc == '3':
            player.choice_scroll()
            self.day_progress()
        elif chc == '4':        
            player.view_stats()

        elif chc == 'stop':
            print("\nStopping program\n")
            running = False
        else:
            print("\nInvalid choice!")
        print("")
        event.random_event()
        print("-"*50) 

    def next_day(self):
        self.current_day += 1  
        return self.current_day

class Student:
    def __init__(self, name, time):
        self.name = name 
        self.energy = 100
        self.focus = 100
        self.cs_knowledge = 1
        self.math_knowledge = 1
        self.phy_knowledge = 1
        self.time = time

  
    def say_study(self):
        print("")
        print("-"*50)
        print(f"You studied math the whole {my_time.time_states[my_time.current_index].lower()}.")

    def study_math(self):
        self.energy -= 20
        self.math_knowledge += 1 
        self.focus -= 10
        player.say_study()

    def study_cs(self):
        self.energy -= 20
        self.cs_knowledge += 1 
        self.focus -= 10
        player.say_study()

    def study_phy(self):
        self.energy -= 20
        self.phy_knowledge += 1 
        self.focus -= 10
        player.say_study()

    def study_tired(self):
        print("")
        print("-"*50)
        print(f"You are too tired to study!")
        

    def choice_scroll(self):
        print(f"\nYou chose to scroll around the entire {my_time.time_states[my_time.current_index].lower()}.")
        self.energy -= 10
        self.focus -= 20
        print("You felt bad...")

    def choice_rest(self):
        print("")
        print("-"*50)
        print(f"You chose to rest and loiter around the entire {my_time.time_states[my_time.current_index].lower()}.")
        if player.energy + 10 >= 100:
            player.energy = 100
        else:
            player.energy += 10

    def view_stats(self):
        print(f"\nDay : {my_time.current_day}")
        print(f"-------- Personal stats --------\nEnergy : {player.energy}\nFocus : {player.focus}\nKnowledge : \n1. Mathematics : lvl {player.math_knowledge}\n2. Computer Science : lvl {player.cs_knowledge}\n3. Physics : lvl {player.phy_knowledge}")

    def night_sleep(self):
        print("")
        print("-"*50)
        print("You went to sleep afterwards...")
        if player.energy + 50 > 100:
            player.energy = 100
        else:
            player.energy = player.energy + 50
        print("="*50)      
        print("")  
        my_time.next_day()
event = Event()
my_time = Time()
player = Student("Fred", my_time)


while running:
    print("")
    if my_time.current_day >= 7:
        print("A week has passed...")
        running = False
    elif my_time.current_index == 2:
        my_time.timeblock_progress()
        player.night_sleep()
    else:
        my_time.timeblock_progress()#Whats wrong with this now?

