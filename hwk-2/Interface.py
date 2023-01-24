class WeaponBehavior:
    def useWeapon(self, weapon) -> None:
        print(weapon)


class Character:
    def __init__(self):
        self.weaponBehavior = None

    def setWeapon(self, weapon) -> None:
        self.weaponBehavior = weapon

    def getWeapon(self) -> WeaponBehavior:
        return self.weaponBehavior

    def fight(self) -> None:
        pass


class King(Character):
    def fight(self) -> None:
        print('The King is fighting')
        Character.getWeapon(self).useWeapon()


class Queen(Character):
    def fight(self) -> None:
        print('The Queen is fighting')
        Character.getWeapon(self).useWeapon()


class Knight(Character):
    def fight(self) -> None:
        print('The Knight is fighting')
        Character.getWeapon(self).useWeapon()


class Troll(Character):
    def fight(self) -> None:
        print('The Troll is fighting')
        Character.getWeapon(self).useWeapon()


class SwordBehavior(WeaponBehavior):
    def useWeapon(self) -> WeaponBehavior:
        return super().useWeapon('Swinging a sword')


class AxeBehavior(WeaponBehavior):
    def useWeapon(self) -> WeaponBehavior:
        return super().useWeapon('Chopping with an Axe')


class KnifeBehavior(WeaponBehavior):
    def useWeapon(self) -> WeaponBehavior:
        return super().useWeapon('Cutting with knife')


class BowAndArrowBehavior(WeaponBehavior):
    def useWeapon(self) -> WeaponBehavior:
        return super().useWeapon('Shooting with a bow and arrow')


king = King()
king.setWeapon(BowAndArrowBehavior())
king.fight()
print()  # newline

queen = Queen()
queen.setWeapon(KnifeBehavior())
queen.fight()
print()  # newline

knight = Knight()
knight.setWeapon(SwordBehavior())
knight.fight()
print()  # newline

troll = Troll()
troll.setWeapon(AxeBehavior())
troll.fight()
print()  # newline
