"""
File name: question6.py
Author: Mathew Bub
Date: 2018-05-13
Description: Simulates a spaceship battle.
"""

import numpy as np

# Classes

class Ship:
    """ 
    A class representing a spaceship.
    
    name - The name of the Ship
    shield - The shield strength of the Ship
    hull - The hull strength of the Ship
    lasers - The power of the Ship's lasers
    """
    name: str
    shield: float
    hull: float
    lasers: float
    
    def __init__(self, name: str, shield: float, hull: float, 
                 lasers: float) -> None:
        """ 
        Initialize a Ship with a name, shield strength, 
        hull strength, and laser strength.
        """
        self.name = name
        self.hull = hull
        self.shield = shield
        self.lasers = lasers
        
    def isDestroyed(self) -> bool:
        """ Check whether the Ship is destroyed. """
        return self.hull <= 0

    def hit(self, damage: float) -> str:
        """ Hit this Ship with a certain amount of damage. """
        self.shield -= damage
        
        # If the shields are depleted, take hull damage at 50% shot strength   
        if self.shield < 0:
            self.hull += self.shield / 2.
            self.shield = 0
        
        # Return a string detailing the result of the damage.
        result_str = "{} was hit for {} damage. ".format(self.name, damage)
        if self.isDestroyed():
            self.hull = 0
            result_str += "{} was destroyed!".format(self.name)
        else:
            result = (self.shield, self.hull)
            result_str += "It now has {} shields and {} hull.".format(*result)
        return result_str
    
    def shoot(self, other: Ship) -> str:
        """ Have this Ship shoot at another Ship. """
        shot_str = "{} shot at {}.\n".format(self.name, other.name)
        hit_str = other.hit(self.lasers)
        return shot_str + hit_str
    
    def chooseTarget(self, others: list) -> Ship:
        """ Choose a valid target to attack from a list of Ships. """
        mask = [not (other is self or other.isDestroyed()) for other in others]
        valid_targets = np.array(others)[mask]
        return np.random.choice(valid_targets)
