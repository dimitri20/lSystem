
def intoList(str):
    return [ch for ch in str]

def intoString(ls):
    a = ''
    for i in ls:
        a += i
    return a

class lSystem:
    def __init__(self, axiom, rules):
        self.axiom = axiom          # string  
        self.rules = rules          # rules in dictyonary A -> AB is the same as {'A':'AB'}
        
        self.alphabet = [
            'F',    #draw a line forward
            'G',    #move forward without drawing
            '+',    #turn right
            '-',    #turn left
            '[',    #save state
            ']'     #restore saved state
        ]
        print('lSystem object has been created.')
    # use rules to generate next generation
    def nextGeneration(self, alphabet, rules):
        alphabet = intoList(alphabet)
        for ch in alphabet:
            for key in rules:
                if key == ch:
                    alphabet[alphabet.index(ch)] = rules[f'{key}']
        print(f'next generation --->>  {intoString(alphabet)}')
        return intoString(alphabet)

    # actions of turtle according to the command
    def turtleAction(self, turtleObject, command, distance=0, angle=0):
        
        for ch in command:
            print(f'{ch} command has been actiovated')
            #draw a line forward
            if ch == 'F':
                turtleObject.forward(distance)

            #move forward without drawing
            elif ch == 'G':
                turtleObject.penup()
                turtleObject.forward(distance)
                turtleObject.pendown()
            
            #turn right
            elif ch == '+':
                turtleObject.right(angle)
            
            #turn left
            elif ch == '-':
                turtleObject.left(angle)
            
            #save state
            elif ch == '[':
                print("current state has been saved")
                self.currentstate = turtleObject.pos()
            
            #restore saved state
            elif ch == ']':
                turtleObject.penup()
                turtleObject.setpos(self.currentstate)
                turtleObject.pendown()

    

class CantorSet(lSystem):
    def __init__(self, turtleObject):
        print(f'CantorSet object has been created')
        self.rules = {
            'F' : 'FGF',
            'G' : 'GGG'
        }
        super().__init__('F', self.rules)

        self.act(turtleObject, 'F', 200, 3)
        

    def act(self, turtleObject, command, distance, evolution):
        print(f"distance =====  {distance}")
        super().turtleAction(turtleObject, command, distance)
        if evolution < 0:
            return

        turtleObject.penup()
        
        turtleObject.right(180)
        turtleObject.forward(200)
        turtleObject.right(180)

        turtleObject.right(90)
        turtleObject.forward(20)
        turtleObject.left(90)
        turtleObject.pendown()

        command = super().nextGeneration(command, self.rules)
        self.act(turtleObject, command, 200/len(command), evolution-1)


if __name__ == '__main__':
    import turtle

    window = turtle.Screen()
    t = turtle.Turtle()

    cantor = CantorSet(t)