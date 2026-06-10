# 🧱 Phase 3 — Portfolio-Grade Project Upgrade
# From 9:00pm of 10 June 2026

#MY INTENTIONS:
#- I upgraded my knowledge on save/load functions :) but somehow I still cant apply it wth
#- I wanna try to change abit, imma start from student class. Im gonna borrow some of my save function from my other mini-projects

#What changed? :
#- I added a save and load game function but it seemed to not work so far. I manage to only save the default data, but even if I save, it's as if it doesnt change...
#- I changed the instance in the Time class from time. to self. . I actually wanted to change to my_time but i realized for the Time class itself, we dont need to do that. 

#Thoughts :
#- Okay so far everything works even tho i organized and moved stuff to the init section of the time class. 
#- Hmmm everytime I test run using the simulation thingy, it gives error on the my_timme.timeblock_progress() at line 325. I dont see whats wrong..
#- i should ask ant manatau he sees something i dont see

#CODE:
import random
import json
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
        self.current_index = 0 #I moved it into my dunder init
        self.current_day = 0
        
    time_states = [ "Morning", "Afternoon", "Night" ] #I dont think this should be here but whatever
    
    @classmethod
    def from_dict(cls):
        return cls()
    #Idk if this would work as I default my current days to that. Would they change

    def to_dict(self): return {
            "Current index" : self.current_index,
            "Current day" : self.current_day }

    def day_progress(self):
        self.current_index = (self.current_index + 1) % len(self.time_states) 
        return self.current_index
        
    def timeblock_progress(self):
        global running 
        print(f"It is {self.time_states[self.current_index].lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n4. View your stats\n5. Settings\n(Write 'stop' to stop the simulation)\nSelect 1-4: ").lower()
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
        elif chc == '5':
            chc2 = input("1. Save game\n2. Load game\n3. Test save/load\nEnter 1-3: ")
            if chc2 == '1':
                pass
                #save_game()
            elif chc2 == '2':
                pass
                #load_game()
            elif chc2 == '3':
                print("--- BEFORE SAVE ---")
                player.view_stats()
                
                SaveManager.save(player, "DoFv31.json") #hmm whats wrong, Oh wowww, i dont have to instantiate them, like calling them savious
                #Since its already a @staticmethod, it now belongs to the class so we can just use SaveManager. instead. Thats very convenient honestly
                player.math_knowledge = 9
                my_time.current_index = 2

                print("--- AFTER CORRUPTION ---")
                player.view_stats()

                restored = SaveManager.load("DoFv31.json")

                print("--- AFTER LOAD ---")
                print(restored.math_knowledge) 
                print(restored.time.current_index)
            else:
                print("Invalid choice!")
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

    def to_dict(self): return {
        "name" : self.name,
        "energy" : self.energy,
        "focus" : self.focus,
        "cs_knowledge" : self.cs_knowledge,
        "math_knowledge" : self.math_knowledge,
        "phy_knowledge" : self.phy_knowledge,
        "time" : self.time.to_dict() }
    @classmethod
    def from_dict(cls, data):
        restored_time = Time.from_dict()
        return cls(data['name'], restored_time) #would this work?
        
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

############ I have a save load function but it seems to not work!!!
#game_state = {
#    "name" : player.name, #Im having trouble for this one, im still unsure heh :(
#    "energy" : player.energy,
#    "focus" : player.focus,
#    "cs_knowledge" : player.cs_knowledge,
#    "math_knowledge" : player.math_knowledge,
#    "phy_knowledge" : player.phy_knowledge, #THis seems to not work i wanna sleep and rest now 10:51pm
#    "current_period" : time.current_index,
#    "current_day" : time.current_day }

#def save_game():
#    with open("DoF_save_data.json", "w") as ourFile:
#        json.dump(game_state, ourFile) #mm its yellow > oh we gotta have the as some variable. grignard reagent
#        print("\nGame saved!")
        #Serious, i dont remember. I looked back at my past miniprojects, i wonder why we dont put anything in that bracket hmph
        #how do i make sure its in the same folder instead of the outermost folder though?

#def load_game():
#    with open("DoF_save_data.json", "r") as ourFile:
#        print("\nPrevious game loaded")
#        return json.load(ourFile)
############ I think kan. my brain is not like proficient in handling saveload functions yet, okay okay, lets do one more then...

my_dict = player.to_dict()
restored = Student.from_dict(my_dict) #from dih my dih

class SaveManager():
    @staticmethod
    def save(player, filename):
        with open(filename, "w") as f:
            dictionary = player.to_dict()
            print("Game saved!")
            json.dump(dictionary, f)
    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            print("Game loaded!")
            data = json.load(f)
            return Student.from_dict(data)

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

