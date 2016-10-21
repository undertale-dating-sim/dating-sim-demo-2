
# This label is for the Name Select Screen
# I tried to duplicate the Undertale version of it.  Might need a little bit of polish.


label Name_Select:
    
    python:
        ui.add(Name_Select())
        name = ui.interact(suppress_overlay=True, suppress_underlay=True)
    if name != 'quit':
        $ player.name = name
    return

init python:
    import math
    import pygame

    class text_button():
        def __init__(self,text = Text('text'), x = 0, y = 0,size=25):
            self.text = Text(text,size=size)
            self.x = x
            self.y = y
            self.setBounds()

        def setBounds(self):
            self.rect = pygame.Rect(self.x,self.y,self.text.size()[0],self.text.size()[1])

        def setPos(self,x,y):
            self.x = x
            self.y = y
            self.setBounds()

        def isclicked(self,x,y):
            if self.rect.collidepoint(x,y):
                return True
            else:
                return False


    class click_letter():
        def __init__(self,let = 'a',x = 0,y = 0):
            self.let = let
            self.origx = x
            self.origy = y

            self.timer = 0

            self.x = x
            self.y = y
            self.text = Text(let,size=25,color='#FFFFFF')

        def set_pos(self,x,y):
            self.jigglex = (renpy.random.randint(0,2) - 1) + x
            self.jiggley = (renpy.random.randint(0,2) - 1) + y
            self.origx = x
            self.origy = y

        def update(self):
            self.jigglex = (renpy.random.randint(0,2) - 1) + self.x
            self.jiggley = (renpy.random.randint(0,2) - 1) + self.y

            self.timer += 1
            if self.timer <= 3:
                self.x = self.origx
                self.y = self.origy
            else:
                self.x = self.jigglex
                self.y = self.jiggley

            if self.timer > 5:
                self.timer = 0
                

    class Name_Select(renpy.Displayable):

        def __init__(self):
           
            renpy.Displayable.__init__(self)
            self.name = ""

            #are we done with the naming period
            self.done = False
            self.leave = False
            #show the confirm screen
            self.confirm = False
            #was the name rejected?

            self.oldst = 0

            self.quit= False

            #holds the y position of the name for drift effect
            self.namey = 0
            self.namesize = 30
            self.namejigglex = 1
            self.namejiggley = 1
            self.namejiggletimer = 0

            self.whitealpha = 0

            self.title = Text("Name the fallen human.",size = 25)

            self.quitbutton = text_button("Quit",x=50,y=50,size=30)
            self.backspacebutton = text_button("Backspace",size=30)
            self.donebutton = text_button("Done",size=30)
            self.pname = Text(self.name, size = 30)
            self.yesbutton = text_button("Yes", size = 30)
            self.nobutton = text_button("No", size = 30)
            self.backbutton = text_button("Go Back", size = 30)


            #game width and height, probably need to figure out how to make this dynamic
            self.WIDTH = 800
            self.HEIGHT = 600 

            self.build_letters()
        
        #Builds the upper and lower case letter list objects and places them on the xy grid
        def build_letters(self):
            self.lower_letters = [click_letter('a'),click_letter('b'),click_letter('c'),click_letter('d'),click_letter('e'),click_letter('f'),click_letter('g'),click_letter('h'),click_letter('i'),click_letter('j'),click_letter('k'),click_letter('l'),click_letter('m'),click_letter('n'),click_letter('o'),click_letter('p'),click_letter('q'),click_letter('r'),click_letter('s'),click_letter('t'),click_letter('u'),click_letter('v'),click_letter('w'),click_letter('x'),click_letter('y'),click_letter('z')]   
            self.upper_letters = [click_letter('A'),click_letter('B'),click_letter('C'),click_letter('D'),click_letter('E'),click_letter('F'),click_letter('G'),click_letter('H'),click_letter('I'),click_letter('J'),click_letter('K'),click_letter('L'),click_letter('M'),click_letter('N'),click_letter('O'),click_letter('P'),click_letter('Q'),click_letter('R'),click_letter('S'),click_letter('T'),click_letter('U'),click_letter('V'),click_letter('W'),click_letter('X'),click_letter('Y'),click_letter('Z')]

            row_count = 0

            #math!
            #there is a margin to the left and right, giving us a width of WIDTH - margin*2
            side_margin = 150
            top_margin = 200
            text_width = self.WIDTH - side_margin*2

            #there are 7 letters in a row, with the first being at margin, then the other 6 being spaced equally
            #so space is text_width / (row_count-1)
            text_space = text_width / (6)

            x = side_margin
            y = top_margin
            for l in self.upper_letters:
                l.set_pos(x,y)

                row_count+=1

                if row_count > 6:
                    row_count = 0
                    x = side_margin
                    y += 30
                else:
                    x += text_space

            x = side_margin
            y += 50
            row_count = 0
            for l in self.lower_letters:
                l.set_pos(x,y)

                row_count+=1

                if row_count > 6:
                    row_count = 0
                    x = side_margin
                    y += 30
                else:
                    x += text_space

            self.letters = self.lower_letters + self.upper_letters
        def interact(self):
            
            evt = ui.interact()
            rv = False

            if self.leave:
                return self.name
            elif self.quit:
                return 'quit'
            else:
                return False

        # #not sure what this does but you have to put all children in here
        # def visit(self):            
        #     return False
        def get_rejects(self,name):
            if name.lower() == 'sans':
                return "nope."
            else:
                return False

        def get_response(self,name):
            if name.lower() == 'papyrus':
                return "I'LL ALLOW IT!!!!"
            elif name.lower() == 'sempai' or name.lower() == 'senpai':
                return "NOTICE ME!"
            elif name.lower() == 'wilson':
                return "The best name of all."
            else:
                return False

        #handles all of the clicking
        def event(self, ev, x, y, st):

            if ev.type == pygame.MOUSEBUTTONDOWN:

                if not self.confirm:
                    for l in self.letters:
                        if pygame.Rect(l.x,l.y,Text(l.let).size()[0],Text(l.let).size()[1]).collidepoint(x,y):
                            if len(self.name) < 15:
                                self.name += l.let
                                renpy.sound.play("audio/sfx/click.wav")
                    if self.quitbutton.isclicked(x,y):
                        renpy.sound.play("audio/sfx/click.wav")
                        #quit
                        self.quit = True
                        return
                    if self.backspacebutton.isclicked(x,y):
                        renpy.sound.play("audio/sfx/click.wav")
                        #backspace
                        if len(self.name) > 0:
                            self.name = self.name[:-1]
                        return
                    if self.donebutton.isclicked(x,y):
                        if len(self.name) > 0:
                            renpy.sound.play("audio/sfx/click.wav")
                            #done
                            self.confirm = True
                        return
                else:
                    if self.yesbutton.isclicked(x,y):
                        renpy.sound.play("audio/sfx/click.wav")
                        self.done = True
                        return
                    if self.nobutton.isclicked(x,y) or self.backbutton.isclicked(x,y):
                        renpy.sound.play("audio/sfx/click.wav")
                        self.confirm = False

                
            # if self.score >= cap:
            #     self.turn_off_music()
            #     return "win"
            # else:
            if self.leave:
                return self.name
            elif self.quit:
                return 'quit'
            else:
                raise renpy.IgnoreEvent()

        def render(self, width, height, st, at):
             
            #render object we will draw into
            r = renpy.Render(width, height)
            
            #figure out the time since last frame
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            if not self.confirm:

                self.namey = 140
                self.namesize = 30
                self.namejiggletimer = 0
                self.namejigglex = 1
                self.namejiggley = 1

                for l in self.letters:
                    l.update()
                    r.blit(renpy.render(l.text,width,height,st,at),(l.x,l.y))
                
                #draw the player name
                self.pname = Text(self.name)
                r.blit(renpy.render(self.pname,width,height,st,at),(width/2 - self.pname.size()[0]/2,140))

                #draw the title
                r.blit(renpy.render(self.title,width,height,st,at),(width/2 - self.title.size()[0]/2,90))
                
                #draw the quit button
                self.quitbutton.setPos(width*.25 - self.quitbutton.text.size()[0]/2,height * .8)
                render = renpy.render(self.quitbutton.text,width,height,st,at)
                r.blit(render,(self.quitbutton.x,self.quitbutton.y))

                #draw the backspace button
                self.backspacebutton.setPos(width * .5 - self.backspacebutton.text.size()[0]/2,height * .8)
                r.blit(renpy.render(self.backspacebutton.text,width,height,st,at),(self.backspacebutton.x,self.backspacebutton.y))

                #draw the done button
                self.donebutton.setPos(width * .75 - self.donebutton.text.size()[0]/2,height * .8)
                r.blit(renpy.render(self.donebutton.text,width,height,st,at),(self.donebutton.x,self.donebutton.y))
            
            else:
                if self.namey <= height/2 - self.pname.size()[1]/2:
                    self.namey += 2
                    self.namesize += .5
                    self.pname = Text(self.name,size=self.namesize)
                r.blit(renpy.render(self.pname,width,height,st,at),(width/2 - self.pname.size()[0]/2 + renpy.random.randint(0,self.namejigglex),self.namey + renpy.random.randint(0,self.namejiggley)))

                self.namejiggletimer += 1

                if self.namejiggletimer > 30:
                    if self.namejigglex < 3:
                        self.namejigglex += 1
                        self.namejiggley += 1
                        self.namejiggletimer = 0
                if not self.get_rejects(self.name) and not self.done:

                    if self.get_response(self.name):
                        r.blit(renpy.render(Text(self.get_response(self.name),size=30),width,height,st,at),(width*.5 - Text(self.get_response(self.name)).size()[0]/2,100))


                    self.yesbutton.setPos(width*.66 - self.yesbutton.text.size()[0]/2,height*.66)
                    r.blit(renpy.render(self.yesbutton.text,width,height,st,at),(self.yesbutton.x,self.yesbutton.y))

                    self.nobutton.setPos(width*.33 - self.nobutton.text.size()[0]/2,height*.66)
                    r.blit(renpy.render(self.nobutton.text,width,height,st,at),(self.nobutton.x,self.nobutton.y))

                elif self.get_rejects(self.name):
                    r.blit(renpy.render(Text(self.get_rejects(self.name),size=30),width,height,st,at),(width*.5 - Text(self.get_rejects(self.name)).size()[0]/2,100))
                    self.backbutton.setPos(width*.33 - self.backbutton.text.size()[0]/2,height*.66)

                    r.blit(renpy.render(self.backbutton.text,width,height,st,at),(self.backbutton.x,self.backbutton.y))
                elif self.done:
                    r.canvas().rect((255,255,255,self.whitealpha),pygame.Rect(0,0,width,height))
                    if self.whitealpha < 255:
                        self.whitealpha += 5
                    else:
                        self.leave = True


            #redraw the frames    
            renpy.redraw(self, 0)
            #return the render
            return r