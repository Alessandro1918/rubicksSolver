"""
Rubik's Cube structure:
     ---
    | T |
 --- --- --- 
| L | F | R |
 --- --- --- 
    | D |
     ---
    | B |
     ---

Numeration pattern:
 --- --- ---
| 1 | 2 | 3 |
 --- --- ---
| 4 | 5 | 6 |
 --- --- ---
| 7 | 8 | 9 |
 --- --- ---

Up:     1 -  9
Front:  10 - 18
Left:   19 - 27
Right:  28 - 36
Down:   37 - 45
Back:   46 - 54

"""

class RubiksCube:
    
    # init a Rubicks Cube as a list of 54 ints
    def __init__(self):
        cube = []
        for i in range(55):
            cube.append(i)
        self.cube = cube
    

    # check if cube is finished
    def isFinished(self):
        for i in range(1, 55):
            if self.cube[i] != i:
                return False
        return True

    
    # count how many stickers are on the wrong side
    """def getErrorCount(self):
        errors = 0
        for i in range(1, 55):
            rightColor = (self.cube[i] - 1) // 9
            actualColor = (i - 1) // 9
            if rightColor != actualColor:
                errors += 1
        return errors"""

    
    # prints a text based representation of the cube
    def show(self):

        # IMPORTANT: By this color order, Up is White, and Front is Orange
        sideNames = ["Up", "Front", "Left", "Right", "Down", "Back"]

        for i in range(1, 55):

            # print sideName
            if (i - 1) % 9 == 0:
                sideName = sideNames[(i - 1) // 9]
                print(sideName + ":")
            
            # format sticker number if single digit
            if self.cube[i] < 10:
                digitsFormated = " " + str(self.cube[i]) + " "
            else:
                digitsFormated = str(self.cube[i]) + " "
            
            # print colored sticker (number or ▒▒)
            # V1 colors - check cubeV1.py
            # V2 colors
            import colored  #https://pypi.org/project/colored/
            colors = [15, 215, 4, 2, 11, 1]     # white, orange, blue, green, yellow, red
            color = colored.fg(colors[(self.cube[i] - 1) // 9])
            reset = colored.attr('reset')
            #print(color + digitsFormated + reset, end='')   #print digits
            print(color + "▒▒ " + reset, end='')           #print ▒▒
            
            #print end line or end side
            if i % 3 == 0:              # Next line
                print("")
            if i % 9 == 0:              # Next side
                print("--------")
    


    def rotate(self, move):

        # Workaround for not have to write "self.cube[42]" a thousand times: init a short named var
        c = []
        for cubie in self.cube:
            c.append(cubie)

        """ Clockwise moves: """
        if move == "U":
            c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9] = c[7], c[4], c[1], c[8], c[5], c[2], c[9], c[6], c[3]
            c[10], c[11], c[12], c[28], c[29], c[30], c[46], c[47], c[48], c[19], c[20], c[21] = c[28], c[29], c[30], c[46], c[47], c[48], c[19], c[20], c[21], c[10], c[11], c[12]
        
        if move == "F":
            c[10], c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[18] = c[16], c[13], c[10], c[17], c[14], c[11], c[18], c[15], c[12]
            c[7], c[8], c[9], c[28], c[31], c[34], c[39], c[38], c[37], c[27], c[24], c[21] = c[27], c[24], c[21], c[7], c[8], c[9], c[28], c[31], c[34], c[39], c[38], c[37]

        if move == "L":
            c[19], c[20], c[21], c[22], c[23], c[24], c[25], c[26], c[27] = c[25], c[22], c[19], c[26], c[23], c[20], c[27], c[24], c[21]
            c[1], c[4], c[7], c[10], c[13], c[16], c[37], c[40], c[43], c[54], c[51], c[48] = c[54], c[51], c[48], c[1], c[4], c[7], c[10], c[13], c[16], c[37], c[40], c[43]

        if move == "R":
            c[28], c[29], c[30], c[31], c[32], c[33], c[34], c[35], c[36] = c[34], c[31], c[28], c[35], c[32], c[29], c[36], c[33], c[30]
            c[9], c[6], c[3], c[46], c[49], c[52], c[45], c[42], c[39], c[18], c[15], c[12] = c[18], c[15], c[12], c[9], c[6], c[3], c[46], c[49], c[52], c[45], c[42], c[39]
        
        if move == "D":
            c[37], c[38], c[39], c[40], c[41], c[42], c[43], c[44], c[45] = c[43], c[40], c[37], c[44], c[41], c[38], c[45], c[42], c[39]
            c[16], c[17], c[18], c[34], c[35], c[36], c[52], c[53], c[54], c[25], c[26], c[27] = c[25], c[26], c[27], c[16], c[17], c[18], c[34], c[35], c[36], c[52], c[53], c[54]
        
        if move == "B":
            c[46], c[47], c[48], c[49], c[50], c[51], c[52], c[53], c[54] = c[52], c[49], c[46], c[53], c[50], c[47], c[54], c[51], c[48]
            c[3], c[2], c[1], c[19], c[22], c[25], c[43], c[44], c[45], c[36], c[33], c[30] = c[36], c[33], c[30], c[3], c[2], c[1], c[19], c[22], c[25], c[43], c[44], c[45]
        
        """ Counter clockwise moves: """
        if move == "Ui":
            for _ in range(3):
                c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9] = c[7], c[4], c[1], c[8], c[5], c[2], c[9], c[6], c[3]
                c[10], c[11], c[12], c[28], c[29], c[30], c[46], c[47], c[48], c[19], c[20], c[21] = c[28], c[29], c[30], c[46], c[47], c[48], c[19], c[20], c[21], c[10], c[11], c[12]
        
        if move == "Fi":
            for _ in range(3):
                c[10], c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[18] = c[16], c[13], c[10], c[17], c[14], c[11], c[18], c[15], c[12]
                c[7], c[8], c[9], c[28], c[31], c[34], c[39], c[38], c[37], c[27], c[24], c[21] = c[27], c[24], c[21], c[7], c[8], c[9], c[28], c[31], c[34], c[39], c[38], c[37]

        if move == "Li":
            for _ in range(3):
                c[19], c[20], c[21], c[22], c[23], c[24], c[25], c[26], c[27] = c[25], c[22], c[19], c[26], c[23], c[20], c[27], c[24], c[21]
                c[1], c[4], c[7], c[10], c[13], c[16], c[37], c[40], c[43], c[54], c[51], c[48] = c[54], c[51], c[48], c[1], c[4], c[7], c[10], c[13], c[16], c[37], c[40], c[43]

        if move == "Ri":
            for _ in range(3):
                c[28], c[29], c[30], c[31], c[32], c[33], c[34], c[35], c[36] = c[34], c[31], c[28], c[35], c[32], c[29], c[36], c[33], c[30]
                c[9], c[6], c[3], c[46], c[49], c[52], c[45], c[42], c[39], c[18], c[15], c[12] = c[18], c[15], c[12], c[9], c[6], c[3], c[46], c[49], c[52], c[45], c[42], c[39]
        
        if move == "Di":
            for _ in range(3):
                c[37], c[38], c[39], c[40], c[41], c[42], c[43], c[44], c[45] = c[43], c[40], c[37], c[44], c[41], c[38], c[45], c[42], c[39]
                c[16], c[17], c[18], c[34], c[35], c[36], c[52], c[53], c[54], c[25], c[26], c[27] = c[25], c[26], c[27], c[16], c[17], c[18], c[34], c[35], c[36], c[52], c[53], c[54]
        
        if move == "Bi":
            for _ in range(3):
                c[46], c[47], c[48], c[49], c[50], c[51], c[52], c[53], c[54] = c[52], c[49], c[46], c[53], c[50], c[47], c[54], c[51], c[48]
                c[3], c[2], c[1], c[19], c[22], c[25], c[43], c[44], c[45], c[36], c[33], c[30] = c[36], c[33], c[30], c[3], c[2], c[1], c[19], c[22], c[25], c[43], c[44], c[45]
                        
        self.cube = c