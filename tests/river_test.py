import unittest

from src.river import River 
from src.fish import Fish 

class TestRiver(unittest.TestCase):
    
    def setUp(self):
      self.nemo = Fish("Nemo","small","Clown Fish") 
      self.dory = Fish("Dory","big","Blue Tang")
      self.fishes = [self.nemo,self.dory]
      self.river = River("nile",self.fishes)

    def test_river_has_name(self):
        
        self.assertEqual("Nile",self.river.name)

    # def test_fish_count(self):
          
    #       self.assertEqual(2,self.)