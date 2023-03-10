# ==========================User Class==================
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # Also include default attributes:
        self.is_rewards_member = False
        self.gold_card_points = 0

# Methods
    def display_info(self):
        print(f"{self.first_name}, {self.last_name}, {self.age},{self.is_rewards_member},{self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("Already a member")
        else:
            self.is_rewards_member = True

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

# =====================Create instances of User class====================


u1 = User("Alex", "Max", 39)
u1.gold_card_points = 100
u1.spend_points(50)
u1.enroll()
u1.enroll()
u1.display_info()

u2 = User("Tiger", "Martin", 27)
u2.enroll()
u2.gold_card_points = 200
u2.spend_points(80)
u2.display_info()

u3 = User("Tim", "Marta", 37)
# u3.enroll()

u3.display_info()
