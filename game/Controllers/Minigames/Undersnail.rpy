init:
    image background field = "minigames/field.png"
    $ mission = ''
label demo_undersnail:
    hide screen show_menu_button

    "Welcome to UnderSnail!!!"
    menu:
        "Need an explanation?"
        "yes":
            "The game is simple."
            "Click on a snail to capture it.  Some snails take longer than others.  Keep holding down the button!"
            "House snails are big and slow."
            "Book snails go all over the place."
            "Rocket snails are too fast."
            "Coffee snail don't know where to go."
            "Capture three snails to end the demo."
        "no":
            "Cool."
    "For the current demo, the game ends at three captures.  This is still a WIP.  Shoot me a message on skype with any bugs you find."
    jump UnderSnail

label UnderSnail:

    #hide the menu
    hide screen show_menu_button

    #set the background
    scene background field

    menu:
        "Test Mission"
        "Rocket":
            $ mission = "rocket"
        "House":
            $ mission = "house"
        "Book":
            $ mission = "book"
        "Coffee":
            $ mission = "coffee"
        "Random":
            $ mission = "random"

    stop music
    python:
        ui.add(UnderSnail())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    if winner == 'win':
        "good job"
        "you did it"

    menu:
        "Try again?"
        "yes":
            jump UnderSnail
        "nah":
            "bye!"
            return
init python:
    import math
    import pygame
    renpy.music.register_channel("nerd",True,stop_on_mute=False)
    renpy.music.register_channel("coffee",True,stop_on_mute=False)
    renpy.music.register_channel("rocket",True,stop_on_mute=False)
    renpy.music.register_channel("house",True,stop_on_mute=False)

    rocket_snail_count = 0
    book_snail_count = 0
    house_snail_count = 0
    coffe_snail_count = 0
    class Flower(renpy.Displayable):
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

    class Snail(renpy.Displayable):
        def __init__(self,xpos,ypos,speed,dx,dy):
            renpy.Displayable.__init__(self)
            self.sprite = Image("minigames/Snail.png")
            self.w = 42
            self.h = 27
            self.xpos = xpos
            self.ypos = ypos
            self.dx = dx
            self.dy = dy
            self.speed = 1
            self.remove = False
            self.width = 50
            self.height = 50
            self.health = 50
        
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
                self.remove = True

    class Book_Snail(Snail):
        def __init__(self,xpos,ypos,speed,dx,dy):
            Snail.__init__(self,xpos,ypos,speed,dx,dy)
            self.sprite = Image("minigames/ReaderSnail.png")
            self.speed = .5
            self.timer = 200
            self.width = 50
            self.height = 28
            self.health = 100
            self.port_count = 0
            self.port_max = 5

        def update(self):

            self.timer -= 1
            if self.timer <= 0:
                self.xpos = renpy.random.randint(100,700)
                self.ypos = renpy.random.randint(100,500)
                self.timer = renpy.random.randint(50,200)
                directions = [(1,0),(1,1),(0,1),(-1,0),(-1,1),(0,-1),(-1,-1),(1,-1)]
                dir_rand = directions[renpy.random.randint(0,7)]
                self.dx = dir_rand[0]
                self.dy = dir_rand[1]
                self.port_count += 1
                if self.port_count > self.port_max:
                    self.remove = True

            Snail.update(self)

    class Rocket_Snail(Snail):
        def __init__(self,xpos,ypos,speed,dx,dy):
            Snail.__init__(self,xpos,ypos,speed,dx,dy)
            self.sprite = Image("minigames/RocketSnail.png")
            self.width = 100
            self.height = 56

            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            dir_rand = directions[renpy.random.randint(0,3)]
            self.dx = dir_rand[0]
            self.dy = dir_rand[1]

            self.speed = 4
            self.health = 20

        def update(self):
            Snail.update(self)


    class House_Snail(Snail):
        def __init__(self,xpos,ypos,speed,dx,dy):
            Snail.__init__(self,xpos,ypos,speed,dx,dy)
            self.sprite = Image("minigames/HouseSnail.png")
            self.speed = .25
            
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            dir_rand = directions[renpy.random.randint(0,3)]
            self.dx = dir_rand[0]
            self.dy = dir_rand[1]

            self.width = 98
            self.height = 70

            self.health = 150

        def update(self):
            Snail.update(self)

    class Coffee_Snail(Snail):
        def __init__(self,xpos,ypos,speed,dx,dy):
            Snail.__init__(self,xpos,ypos,speed,dx,dy)
            self.sprite = Image("minigames/CoffeeSnail.png")
            self.speed = 2
            self.dir_timer = 0
            self.change_now = renpy.random.randint(25,50)
            self.width = 70
            self.height = 44

        def update(self):

            #we need the coffee snail to change directions randomly
            self.dir_timer += 1

            if self.dir_timer == self.change_now:
                directions = [(1,0),(1,1),(0,1),(-1,0),(-1,1),(0,-1),(-1,-1),(1,-1)]
                dir_rand = directions[renpy.random.randint(0,7)]
                self.dy = dir_rand[0]
                self.dx = dir_rand[1]
                self.dir_timer = 0
                self.change_now = renpy.random.randint(25,50)

            Snail.update(self)

    class UnderSnail(renpy.Displayable):

        def __init__(self):
           
            renpy.Displayable.__init__(self)
            
            #setting synchro to true for testing
            renpy.music.play("audio/music/snail_book.mp3","nerd",True,None,True)
            renpy.music.play("audio/music/snail_coffee.mp3","coffee",True,None,True)
            renpy.music.play("audio/music/snail_rocket.mp3","rocket",True,None,True)
            renpy.music.play("audio/music/snail_house.mp3","house",True,None,True)

            
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

            #arrays of snails and flowers
            self.snails = []
            self.flowers = []
            self.capture_texts = []

            for i in range(0, self.flowercount):
                self.flowers.append(Flower(375,275))
            
        def interact(self):
            
            evt = ui.interact()
            rv = False


            if score > 3:
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

            for s in self.snails:
                if isinstance(s,House_Snail):
                    renpy.music.set_volume(1,0,'house')
                if isinstance(s,Rocket_Snail):
                    renpy.music.set_volume(1,0,'coffee')
                if isinstance(s,Book_Snail):
                    renpy.music.set_volume(1,0,'nerd')
                if isinstance(s,Coffee_Snail):
                    renpy.music.set_volume(1,0,'rocket')



        def spawn_snail(self,flower,dx=0,dy=1):
            self.snails.append(Snail(flower.x,flower.y,1,dx,dy))

        def spawn_rocket_snail(self,flower,dx=0,dy=1):
            self.snails.append(Rocket_Snail(flower.x,flower.y,1,dx,dy))

        def spawn_coffee_snail(self,flower,dx=0,dy=1):
            self.snails.append(Coffee_Snail(flower.x,flower.y,1,dx,dy))

        def spawn_book_snail(self,flower,dx=0,dy=1):
            self.snails.append(Book_Snail(flower.x,flower.y,1,dx,dy))

        def spawn_house_snail(self,flower,dx=0,dy=1):
            self.snails.append(House_Snail(flower.x,flower.y,1,dx,dy))

        def spawn_random_snail(self,flower):
            pick = renpy.random.randint(0,3)

            directions = [(1,0),(1,1),(0,1),(-1,0),(-1,1),(0,-1),(-1,-1),(1,-1)]

            dir_rand = directions[renpy.random.randint(0,7)]

            dirx = dir_rand[0]
            diry = dir_rand[1]

            if mission == 'house':
                self.spawn_house_snail(flower,dx=dirx,dy=diry)
            elif mission == "coffee":
                self.spawn_coffee_snail(flower,dx=dirx,dy=diry)
            elif mission == "book":
                self.spawn_book_snail(flower,dx=dirx,dy=diry)
            elif mission == "rocket":
                self.spawn_rocket_snail(flower,dx=dirx,dy=diry)
            elif mission == "random":
                self.spawn_rocket_snail(flower,dx=dirx,dy=diry)
                self.spawn_house_snail(flower,dx=dirx,dy=diry)
                self.spawn_coffee_snail(flower,dx=dirx,dy=diry)
                self.spawn_book_snail(flower,dx=dirx,dy=diry)

        def spawn_handler(self):
            if len(self.snails) == 0:
                while len(self.snails) < self.snailcount:
                    self.spawn_random_snail(self.flowers[renpy.random.randint(0,len(self.flowers)-1)])

            elif len(self.snails) < self.snailcount:
                if self.snailtimer > self.snailrespawntime:
                    self.snailtimer = 0
                    #spawn at a random flowerbed
                    self.spawn_random_snail(self.flowers[renpy.random.randint(0,len(self.flowers)-1)])

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

            cap = 3

            if self.score >= cap:
                self.turn_off_music()
                return "win"
            else:
                raise renpy.IgnoreEvent()

        def update(self):

            if self.click_target and self.over_target:
                self.click_target.health -=1

            for s in self.snails:
                s.update()
                if s.remove:
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
            self.handle_music()

        def interact(self):
            evt = ui.interact()
            rv = False

            if self.score > 1:
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
                r.blit(text_render,(0.1,0.1))

            #redraw the frames    
            renpy.redraw(self, 0)
            #return the render
            return r