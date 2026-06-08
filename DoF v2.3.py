#🧱 PHASE 2 — Make it feel like a “real system”

#CODE:
# Starting from 11:30am 8th June 2026

#MY INTENTIONS:
#- I wanna change my time-progression system by utlizing modulo.  

#What changed? :
#- I changed the time-progression to something I learned recently which was utilizing modular operation which is '%'.
#- I reduced repeated codes by defining them into a function 
#- I debugged the bug of unable to progress day, my else/if for night syntax wasn't fetched so I replaced it with the current_index 
#- I classed my player, event and time! Looking better now.

#Future updates:
#- Maybe I can make it folder style since it's kinda getting long now...
#- Better UX ofc, I kinda dont like theres always Random event log: empty space there like idk whats causing it

import random
#import time as t (just in case in the future i wanna have some fun with the dramatic pauses)
running = True
class Student:
    def __init__(self, name):
        self.name = name 
        self.energy = 100
        self.focus = 100
        self.cs_knowledge = 1
        self.math_knowledge = 1
        self.phy_knowledge = 1

    def say_study(self):
        print("")
        print("-"*50)
        print(f"You studied math the whole {time.time_states[time.current_index].lower()}.")

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
        print(f"\nYou chose to scroll around the entire {time.time_states[time.current_index].lower()}.")
        self.energy -= 10
        self.focus -= 20
        print("You felt bad...")

    def choice_rest(self):
        print("\n-"*50)
        print(f"You chose to rest and loiter around the entire {time.time_states[time.current_index].lower()}.")
        if player.energy + 10 >= 100:
            player.energy = 100
        else:
            player.energy += 10

    def view_stats(self):
        print(f"\nDay : {time.current_day}")
        print(f"-------- Personal stats --------\nEnergy : {player.energy}\nFocus : {player.focus}\nKnowledge : \n1. Mathematics : lvl {player.math_knowledge}\n2. Computer Science : lvl {player.cs_knowledge}\n3. Physics : lvl {player.phy_knowledge}")

    def night_sleep(self):
        print("\n-"*50)
        print("You went to sleep afterwards...")
        if player.energy + 50 > 100:
            player.energy = 100
        else:
            player.energy = player.energy + 50
        print("="*50)      
        print("")  
        time.next_day()
#I keep forgetting my "self" lololol
player = Student("Fred")

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
            event.funny_event
        elif tp == 4:
            event.intro_rand_event()
            event.fatigue_event()
        else:
            pass
event = Event()

class Time: 
    time_states = [
        "Morning",
        "Afternoon",
        "Night"
    ]
    current_index = 0
    current_day = 0
    #print(time_states[current_index])

    def day_progress(self):
        self.current_index = (time.current_index + 1) % len(time.time_states) #So that len sees how long is 2 huh because 0 1 2. Eh wait somethings wrong, wouldnt using len on an empty list return as 0, then if theres 1? eh wouldnt it actually mean 3 then?
        return self.current_index
        #hmmmm i dont get it. Maybe you could show me the progression how people used to do then see how they improve to optimize it, maybe there i can see
        
    def timeblock_progress(self):
        global running #(why did i global run this in 1st place) > its so that my running False work
        print(f"It is {time.time_states[time.current_index].lower()} right now...")
        chc = input("\nWhat do you want to do now?\n1. Study\n2. Rest\n3. Scroll\n4. View your stats\n(Write 'stop' to stop the simulation)\nSelect 1-4: ").lower()
        if chc == '1':
            if player.energy >= 20 and player.focus >= 20:
                subject = input("\nWhich subject do you want to study?\n1. Math\n2. Computer Science\n3. Physics\nEnter number 1-3: ")
                if subject == '1':
                    player.study_math()
                    time.day_progress()
                elif subject == '2':
                    player.study_cs()
                    time.day_progress()
                elif subject == '3':
                    player.study_phy()
                    time.day_progress()
            elif player.energy < 20:
                player.study_tired()
                return
            elif player.focus < 20:
                print("")
                print("-"*50)
                print("You tried to study but nothing sticked. You gave up.")

        elif chc == '2':
            player.choice_rest()
            time.day_progress()
        elif chc == '3':
            player.choice_scroll()
            time.day_progress()
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
        time.current_day += 1  
        return time.current_day
time = Time()

#1 day is 3 cycles right
while running:
    print("")
    if time.current_day >= 7:
        print("A week has passed...")
        running = False
    elif time.current_index == 2:
        time.timeblock_progress()
        player.night_sleep()
        #print("elif night called") Okay this was a good console.log() way
    else:
        time.timeblock_progress()

#if __name__ == "__main__":
#    main()
#Idk how to define it as a function tho, to run it. So I'll just leave to what works first
#1pm of 8th June 2026. Massive bug, I cannot add my days... > at library 3pm I fixed the big, in seemed that my elif ... = 'night' wasnt fetched so I replaced it with current_index

#SO BUGGY. stressin me out :(( but I think its my misunderstanding of global, maybe i gotta exercise whats global and whats not. 
#Ok lemme debug heheh 9:32pm 8th June 2026 > Yes! I successfully fixed it, I figured I didnt have to do global time repeatedly since doing "time." in front of it calls the class itself sooo yeah. 
#Im satisfied with how it is, it si 9:46pm now, I tried classing Subject but I think its an overkill and too much work. i wanna move on to phase 3
