init:
    image background field = "minigames/field.png"


label UnderSnail:

    #hide the menu
    call hide_buttons

    #set the background
    scene background field

    "The Snails will come out of the flower patches on the left."
    "Click and hold on them to capture them in your net!"
    "Miss three snails and its Game Over."
    "Catch ten to win!"
    "Good luck!"
    stop music
    python:
        us = UnderSnail()
        ui.add(us)
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
    $ renpy.transition(fade)
    $ renpy.show(world.get_room("Snail Hunting Room").bg)

    if winner == 'win':
        "Good job!"
        $ player.give_snails()
    else:
        "* Oh no..."
        "* All your snails got away."
    
    $ world.timezone_action_count += 10
    $ world.update_world()
    if world.current_timezone != "Night":
        play music "audio/ruins/the_ruins.mp3" fadein 5
        # if mission == "rocket":
        #     "You caught [us.rocket_snail_count] rocket snails."
        # if mission == "house":
        #     "You caught [us.house_snail_count] house snails."
        # if mission == "book":
        #     "You caught [us.book_snail_count] book snails."
        # if mission == "coffee":
        #     "You caught [us.coffee_snail_count] coffee snails."
        # if mission == "random":
        #     "You caught [us.rocket_snail_count] rocket snails, [us.house_snail_count] house snails, [us.book_snail_count] book snails, and [us.coffee_snail_count] coffee snails."
        # "Go, you!"
    return

init python:
    import math
    import pygame
    renpy.music.register_channel("nerd",True,stop_on_mute=False)
    renpy.music.register_channel("coffee",True,stop_on_mute=False)
    renpy.music.register_channel("rocket",True,stop_on_mute=False)
    renpy.music.register_channel("house",True,stop_on_mute=False)
    
    class Flower_Patch(renpy.Displayable):
        def __init__(self,x,y):
            renpy.Displayable.__init__(self)
            self.sprite = Image("minigames/Flowers.png")
            self.w = 50
            self.h = 50
            self.x = x
            self.y = y

    class Capture_Text():
        def __init__(self,xpos,ypos):
            self.xpos = xpos
            self.ypos = ypos
            self.speed = 1
            self.timer = 30
            self.remove = False

        def update(self):
            self.ypos = self.ypos - self.speed
            self.timer -= 1

            if self.timer <= 0:
                self.remove = True

    class Flower(renpy.Displayable):
        def __init__(self,xpos,ypos):
            renpy.Displayable.__init__(self)
            self.sprite = Image("minigames/Flowers.png")
            self.w = 54
            self.h = 51
            self.x = xpos
            self.y = ypos

    class Snail(renpy.Displayable):
        def __init__(self,xpos,ypos,speed,dx,dy):
            renpy.Displayable.__init__(self)
            self.sprite = Image("minigames/snail.png")
            self.w = 42
            self.h = 27
            self.xpos = xpos
            self.ypos = ypos
            self.dx = dx
            self.dy = dy
            self.speed = renpy.random.randint(1,3)
            self.remove = False
            self.missed = False
            self.width = 50
            self.height = 50
            self.health = 10
        
        def update(self):
            self.ypos = self.ypos + self.speed * self.dy
            self.xpos = self.xpos + self.speed * self.dx
            self.check_remove()

        def check_remove(self):
            if self.health <= 0:
                self.remove = True
            #redundant, so sue me
            centerx = self.xpos + self.width /2
            centery = self.ypos + self.height /2
            if centerx < 0 or centerx > 800 or centery < 0 or centery > 800:
                self.missed = True
                self.remove = True

    class UnderSnail(renpy.Displayable):

        def __init__(self):
           
            renpy.Displayable.__init__(self)
            
            #setting synchro to true for testing
            #renpy.music.play("audio/music/snail_book.mp3","nerd",True,None,True)
            #renpy.music.play("audio/music/snail_coffee.mp3","coffee",True,None,True)
            #renpy.music.play("audio/music/snail_rocket.mp3","rocket",True,None,True)
            #renpy.music.play("audio/music/snail_house.mp3","house",True,None,True)
            #self.turn_off_music()
            renpy.music.play("audio/thundersnail.mp3","music",True,None,True)
            renpy.music.set_volume(.2,0,'music')
            #game variables
            self.title_phase = 1
            self.round_start_phase = 2
            self.game_phase = 3
            self.score_phase = 4
            self.start_timer = 100


            self.click_target = False
            self.over_target = False
            
            self.current_game_phase = 1
            self.oldst = 0
            self.flowercount = 1
            self.snailcount = 4
            self.snailtimer = 0
            self.snailrespawntime = 100

            #game width and height, probably need to figure out how to make this dynamic
            self.WIDTH = 1024
            self.HEIGHT = 640    

            #simple score
            self.score = 0
            self.scoretext = Text("Score : %d" % self.score)
            self.scoretext.xpos = 0.1
            self.scoretext.ypos = 0.1

            self.missed_snails = 0
            self.missed_snailstext = Text("Missed : %d" % self.missed_snails)
            self.missed_snailstext.xpos = 0.8
            self.missed_snailstext.ypos = 0.1

            self.rocket_snail_count = 0
            self.book_snail_count = 0
            self.house_snail_count = 0
            self.coffee_snail_count = 0

            #arrays of snails and flowers
            self.snails = []
            self.flowers = []
            self.capture_texts = []

            self.flowers.append(Flower(50,50))
            self.flowers.append(Flower(50,500))
            self.flowers.append(Flower(50,275))

            
        def interact(self):
            evt = ui.interact()
            rv = False


            if score > 10:
                self.turn_off_music()
                return 'win'

            return False
        def turn_off_music(self):
            renpy.music.set_volume(0,0,'nerd')
            renpy.music.set_volume(0,0,'coffee')
            renpy.music.set_volume(0,0,'rocket')
            renpy.music.set_volume(0,0,'house')
        def handle_music(self):
            
            self.turn_off_music()

            # for s in self.snails:
            #     if isinstance(s,House_Snail):
            #         renpy.music.set_volume(0.1,0,'house')
            #     if isinstance(s,Rocket_Snail):
            #         renpy.music.set_volume(0.1,0,'rocket')
            #     if isinstance(s,Book_Snail):
            #         renpy.music.set_volume(0.1,0,'nerd')
            #     if isinstance(s,Coffee_Snail):
            #         renpy.music.set_volume(0.1,0,'coffee')



        def spawn_snail(self,flower,dx=1,dy=0):
            self.snails.append(Snail(flower.x+flower.w/2,flower.y+flower.h/2,1,dx,dy))


        def spawn_handler(self):
            if len(self.snails) == 0:
                while len(self.snails) < self.snailcount:
                    self.spawn_snail(self.flowers[renpy.random.randint(0,len(self.flowers)-1)])

            elif len(self.snails) < self.snailcount:
                if self.snailtimer > self.snailrespawntime:
                    self.snailtimer = 0
                    #spawn at a random flowerbed
                    self.spawn_snail(self.flowers[renpy.random.randint(0,len(self.flowers)-1)])

        #not sure what this does but you have to put all children in here
        def visit(self):            
            sprites = self.flowers + self.snails         
            return sprites

        #handles all of the clicking
        def event(self, ev, x, y, st):

            if self.click_target:
                if not pygame.Rect(self.click_target.xpos,self.click_target.ypos,self.click_target.width,self.click_target.height).collidepoint(x,y):
                    self.over_target = False
                else:
                    self.over_target = True

            if ev.type == pygame.MOUSEBUTTONUP:
                self.click_target = False
            if ev.type == pygame.MOUSEBUTTONDOWN:

                if self.current_game_phase == self.title_phase:
                    self.current_game_phase = self.round_start_phase
                else:

                    #if the player clicks and it is on a snail, pick that snail
                    #if the player mouse moves off the snail, turn off target
                    #player must release mouse to reset target

                    for s in self.snails:
                        if pygame.Rect(s.xpos,s.ypos,s.width,s.height).collidepoint(x,y) and not self.click_target:
                            self.click_target = s

            cap = 10

            if self.score >= cap:
                self.turn_off_music()
                return "win"
            elif self.missed_snails >= 3:
                self.turn_off_music()
                return "lose"
            else:
                raise renpy.IgnoreEvent()

        def update(self):

            if self.click_target and self.over_target:
                self.click_target.health -=1

            for s in self.snails:
                s.update()
                if s.remove:
                    if s.missed:
                        self.missed_snails += 1
                    self.snails.remove(s)
                    #stupid check because they were making text by going offscreen
                    if s.health <= 0:
                        self.capture_texts.append(Capture_Text(s.xpos,s.ypos))
                        self.score += 1

            for c in self.capture_texts:
                c.update()
                if c.remove:
                    self.capture_texts.remove(c)

            self.snailtimer += 1
            self.spawn_handler()
            #self.handle_music()

        def interact(self):
            evt = ui.interact()
            rv = False

            if self.score > 5:
                return 'win'
            return False

        def render(self, width, height, st, at):
             
            #render object we will draw into
            r = renpy.Render(width, height)
            
            #figure out the time since last frame
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            #Show the Title Screen
            if self.current_game_phase == self.title_phase:
                r.blit(renpy.render(Text("{size=+40}UNDERSNAIL"),width,height,st,at),(width/2-200,height/2-50))
                r.blit(renpy.render(Text("click to begin"),width,height,st,at),(width/2,height/2 + 30))
            elif self.current_game_phase == self.round_start_phase:
                r.blit(renpy.render(Text("Are you ready?"),width,height,st,at),(width/2 - 100,height/2))
                r.blit(renpy.render(Text('%d' % (self.start_timer/10)),width,height,st,at),(width/2 - 5,height/2+30))
                self.start_timer-=.5

                if self.start_timer < 1:
                    self.current_game_phase = self.game_phase
                    rocket_snail_count = 0
                    book_snail_count = 0
                    house_snail_count = 0
                    coffee_snail_count = 0
            else:
                #call update loop
                self.update()

                #render the snails
                for s in self.snails:
                    snail_render = renpy.render(s.sprite, width, height, st, at)
                    text_render = renpy.render(Text('%d' % (s.health)),width,height,st,at)
                    r.blit(text_render,(s.xpos,s.ypos - 20))
                    r.blit(snail_render,(s.xpos,s.ypos))

                for c in self.capture_texts:
                    cap_render = renpy.render(Text('Caught!'),width,height,st,at)
                    r.blit(cap_render,(c.xpos,c.ypos))

                #render the flowers
                for f in self.flowers:
                    flower_render = renpy.render(f.sprite,width,height,st,at)
                    r.blit(flower_render,(f.x,f.y))

                #update and render score  
                self.scoretext = Text("Score : %d" % self.score)
                text_render = renpy.render(self.scoretext,width,height,st,at)
                r.blit(text_render,(25,0.1))

                self.missed_snailstext = Text("Missed : %d" % self.missed_snails)
                text_render2 = renpy.render(self.missed_snailstext,width,height,st,at)
                r.blit(text_render2,(width - 200,0.1))

            #redraw the frames    
            renpy.redraw(self, 0)
            #return the render
            return r