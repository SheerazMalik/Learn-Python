
class Player():

    def __init__(self,name):
        self.name = name
        self._lives = 5
        self.level = 2
        self.score = 20

#now we used getter setter. the benifit of getter and setter is its a layer b/w user and original busisness logic

    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives of Players can not be Zero")
            self._lives = 0  

    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return f"Name:{self.name}, Lives:{self.lives}, Level:{self.level}, Score:{self.score}"
    