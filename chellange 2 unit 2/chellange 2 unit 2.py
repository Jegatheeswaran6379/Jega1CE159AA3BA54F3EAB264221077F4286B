implement a class called player that represents a cricket player.the player class should have a method called play() which prints"the player is playing cricket".Derive two classes ,Batsman and Bowler,from the player class.Override the play() method in each derived class to print"the batsman is batting" and "the bowler is bowling",respectively.write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.'''                                                                                                                                                                                                                                                                                                                                                    class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
 def _init_(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount,
                                                     self.__account_balance))
    else:
      print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (account #{}): ₹{}".format(
        self._account_holder_name, self._account_number,
        self.__account_balance))