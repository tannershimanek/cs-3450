namespace weapon_behavior {
    public interface WeaponBehavior {
        void useWeapon();
    }

    public class KnifeBehavior : WeaponBehavior
    {
        public void useWeapon() {
            Console.WriteLine("Cutting with knife");
        }
    }

    public class BowAndArrowBehavior:WeaponBehavior {
        public void useWeapon() {
            Console.WriteLine("shooting with an arrow and a bow");
        }
    }

    public class AxeBehavior:WeaponBehavior {
        public void useWeapon() {
            Console.WriteLine("Chopping with an axe.");
        }
    }

    public class SwordBehavior:WeaponBehavior {
        public void useWeapon() {
            Console.WriteLine("swinging a sword");
        }
    }

    public abstract class Character {
        protected WeaponBehavior weapon;

        public void setWeapon(WeaponBehavior w) {
            this.weapon = w;
        }

        public WeaponBehavior getWeapon() {
            return weapon;
        }

        public abstract void fight();
    }

    public class Knight :Character {
        public override void fight() {
            Console.WriteLine("Knight is fighting");
        }
    }

    public class King:Character {
        public override void fight() {
            Console.WriteLine("King is fighting");
        }
    }

    public class Queen : Character {
        public override void fight() {
            Console.WriteLine("Queen is fighting");
        }
    }

    public class Troll : Character {
        public override void fight() {
            Console.WriteLine("Troll is fighting");
        }
    }

    public class Program {
        public static void Main(string[] args) {
            Character queen = new Queen();
            queen.setWeapon(new BowAndArrowBehavior());
            queen.getWeapon().useWeapon();
            queen.fight();

            Character king = new King();
            king.setWeapon(new SwordBehavior());
            king.getWeapon().useWeapon();
            king.fight();

            Character troll = new Troll();
            troll.setWeapon(new AxeBehavior());
            troll.getWeapon().useWeapon();
            troll.fight();

            Character knight = new Knight();
            knight.setWeapon(new KnifeBehavior());
            knight.getWeapon().useWeapon();
            knight.fight();
            //pause
            Console.ReadLine();
        }
    }
}