"""Game entities."""

from .core.entity import Entity
from .movable import Movable


class Ship(Entity):
    def __init__(self, owner):
        super(Ship, self).__init__(owner)
        self._currentWeapon = None

        @property
        def currentWeapon(self):
            return self._currentWeapon

        @currentWeapon.setter
        def currentWeapon(self, weapon):
            self._currentWeapon = weapon


class PlayerShip(Ship):
    def __init__(self, owner, startX, startY):
        super(PlayerShip, self).__init__(owner)
        self._x = startX
        self._y = startY
        self.baseType = "PlayerShip"

    def updateState(self):
        self.updatePosition()

    def updatePosition(self):
        pass


class EnemyShip(Ship):
    def __init__(self, owner, startX, startY):
        super(EnemyShip, self).__init__(owner)
        self.baseType = "EnemyShip"


class Weapon(Entity):
    def __init__(self, owner):
        super(Weapon, self).__init__(owner)
        self.shell = None

    def fire(self):
        print("bang!")


class WeaponShell(Movable):
    def __init__(self, owner):
        super(WeaponShell, self).__init__(owner)

    def updateState(self):
        super(WeaponShell, self).updateState()

    def handleEvents(self):
        pass


class BasicLaser(WeaponShell):
    def __init__(self, owner):
        super(BasicLaser, self).__init__(owner)
        self.leap(0, 0)
        self.rotateUntilStop(0, 0, 0, 0, 0)


class WBasicLaser(Weapon):
    def __init__(self, owner):
        super(WBasicLaser, self).__init__(owner)
        self.shell = BasicLaser

        def fire(self):
            print(self.shell())


class Asteroid(Movable):
    def __init__(self, owner):
        super(Asteroid, self).__init__(owner)

    def updateState(self):
        super(Asteroid, self).updateState()

    def handleEvents(self):
        pass