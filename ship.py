from log import Log

class Ship:
    # status
    Idle = 0
    Repairing = 1

    def __init__(self, game, id_, shipClass, lv, hp, maxHp, fuel, ammo):
        self.game = game
        self.id = id_
        self.shipClass = shipClass
        self.lv = lv
        self.hp = hp
        self.maxHp = maxHp
        self.fuel = fuel
        self.ammo = ammo
        self.status = Ship.Idle
        self.fleet = None

    def setProps(self, ship):
        self.lv = ship.lv
        self.hp = ship.hp
        self.maxHp = ship.maxHp
        self.fuel = ship.fuel
        self.ammo = ship.ammo

    def getName(self):
        return self.shipClass.name

    def getShipType(self):
        return self.shipClass.shipType

    def isIdle(self):
        if self.status != Ship.Idle:
            Log.i("Ship %s' status: %d" % (self.getName(), self.status))
            return False
        if self.fleet is not None and self.fleet.expedition is not None:
            Log.i('In fleet %d, expedition is %d' % (self.fleet.id, self.fleet.expedition.id))
            return False
        return True

    def isInjured(self):
        return self.hp < self.maxHp

    def isBroken(self):
        return self.hp * 2 < self.maxHp

    def isBadlyBroken(self):
        return self.hp * 4 < self.maxHp

    def isFilled(self):
        return self.fuel == self.shipClass.fuel and self.ammo == self.shipClass.ammo

    def setRepaired(self):
        self.hp = self.maxHp

    def setFilled(self):
        self.fuel = self.shipClass.fuel
        self.ammo = self.shipClass.ammo

    def instantRepair(self):
        if not self.isInjured():
            return False
        self.game.instantRepair(self)
        self.setRepaired()
        return True

    def dismantle(self, keepEquipt = False):
        self.game.dismantleShip(self, keepEquipt)
        self.game.removeShip(self)
