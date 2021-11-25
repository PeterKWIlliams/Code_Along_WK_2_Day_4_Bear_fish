class River:
    def __init__(self,name,fishes):
        
        self.name = name
        self.fishes =  fishes 

    
    def fishes_count(self):
        
        return len(self.fishes)
    
    def remove_fish(self,fish):
        
        self.fishes.remove(fish)

    def add_fish(self,fish):
        
        self.fishes.append(fish)














