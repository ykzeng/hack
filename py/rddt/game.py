class Game:
    def __init__(self) -> None:
        self.a=self.b=0

    def score(self,player):
        if self.winner()=='ERROR':
            if player=='A':
                self.a+=1
            elif player=='B':
                self.b+=1
            if self.a>3 and self.a==self.b:
                self.a=self.b=3
            return 'SUCCESS'
        else:
            return 'ERROR'
    
    def current(self):
        print(f'A@{self.a}', f'B@{self.b}')
        return self.a,self.b
    
    def winner(self):
        if self.a>=5 and self.a-self.b>=2:
            return 'A'
        elif self.b>=5 and self.b-self.a>=2:
            return 'B'
        else:
            return 'ERROR'
class Match:
    def __init__(self) -> None:
        self.a=self.b=0
    
    def play(self,testcases):
        for arr in testcases:
            print('='*20)
            g=Game()
            for p in arr:
                print('#'*10)
                print(g.score(p))
                g.current()
                print(g.winner())
                if g.winner()!='ERROR':
                    if g.winner()=='A':
                        self.a+=1
                    elif g.winner()=='B':
                        self.b+=1
                    break
        
# class Match:
#     def __init__(self) -> None:
#         pass
g=Game()
testcases=[
    ['A','A','A','B','A','A'],
    ['A','B','A','B','A','A','B','B','B','B'],
    ['A','B','A','B','A','A','B','B','B','B'],
    ['B','A','B','B','B','B']
]
        

# print(g.score('A'))
# g.current()
# print(g.winner())