class Game(Player, Point):
    def __init__(self, player1, player2):
        Player.__init__(nome)
        Point.__init__(ponto)
        player1.set_nome("player1")
        player2.set_nome ("player2")
        player1.set_point(0)
        player2.set_point(0)

        point0 = "Love"
        point2 = "Fifteen"
        point3 = "Thirty"
        point4 = "forty"
        empate = "empate"
        
    
    def score(self):
        result = ""
        if (self.player1.get_point() == self.player2.get_point() and self.player1.get_point() < 3):
            if (self.player1.get_point()==0):
                result = point0
            if (self.player1.get_point()==1):
                result = point2
            if (self.player1.get_point()==2):
                result = point3
            result += "-All"
        if (self.player1.get_point()==self.player2.get_point() and self.player1.get_point()>2):
            result = empate
        
        P1res = ""
        P2res = ""
        if (self.player1.get_point() > 0 and self.player2.get_point()==0):
            if (self.player1.get_point()==1):
                P1res = point2
            if (self.player1.get_point()==2):
                P1res = point3
            if (self.player1.get_point()==3):
                P1res = point4
            
            P2res = point0
            result = P1res + "-" + P2res
        if (self.player2.get_point() > 0 and self.player1.get_point()==0):
            if (self.player2.get_point()==1):
                P2res = point2
            if (self.player2.get_point()==2):
                P2res = point3
            if (self.player2.get_point()==3):
                P2res = point4
            
            P1res = point0
            result = P1res + "-" + P2res
        
        
        if (self.player1.get_point()>self.player2.get_point() and self.player1.get_point() < 4):
            if (self.player1.get_point()==2):
                P1res=point3
            if (self.player1.get_point()==3):
                P1res=point4
            if (self.player2.get_point()==1):
                P2res=point2
            if (self.player2.get_point()==2):
                P2res=point3
            result = P1res + "-" + P2res
        if (self.player2.get_point()>self.player1.get_point() and self.player2.get_point() < 4):
            if (self.player2.get_point()==2):
                P2res=point3
            if (self.player2.get_point()==3):
                P2res=point4
            if (self.player1.get_point()==1):
                P1res=point2
            if (self.player1.get_point()==2):
                P1res=point3
            result = P1res + "-" + P2res
        
        if (self.player1.get_point() > self.player2.get_point() and self.player2.get_point() >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.player2.get_point() > self.player1.get_point() and self.player1.get_point() >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.player1.get_point()>=4 and self.player2.get_point()>=0 and (self.player1.get_point()-self.player2.get_point())>=2):
            result = "Win for " + self.player1Name
        if (self.player2.get_point()>=4 and self.player1.get_point()>=0 and (self.player2.get_point()-self.player1.get_point())>=2):
            result = "Win for " + self.player2Name
        return result

    
    def won_point(self, player):
        if player.get_nome = player1
            self.P1Score()
        else:
            self.P2Score()

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.player1.set_point
    
    
    def P2Score(self, point):
        self.player2.set_point()