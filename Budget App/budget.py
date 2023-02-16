
class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item ['description'][0:23]:23}" + f"{item ['amount']:>7.2f}" + '\n'
      total += item['amount']

    printed_statment = title + items + "Total: " + str(total)
    return printed_statment

  def deposit(self, amount, description=""):
    """
        A deposit method that accepts an amount and description. 
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list in the form of 
        {"amount": amount, "description": description}.
        """
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    '''
        A withdraw method that is similar to the deposit method, 
        but the amount passed in should be stored in the ledger as a negative number. 
        If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise.
        '''

    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def check_funds(self, amount, description=""):
    '''
        A check_funds method that accepts an amount as an argument. 
        It returns False if the amount is greater than the balance of 
        the budget category and returns True otherwise. 
        This method should be used by both the withdraw method and transfer method.
        '''
    if (self.get_balance() >= amount):
      return True
    return False

  def get_balance(self):
    '''
        A get_balance method that returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred.
        '''
    total = 0
    for item in self.ledger:
      total += item["amount"]

    return total

  def transfer(self, amount, catagory):
    '''
        A transfer method that accepts an amount and another budget category as arguments. 
        The method should add a withdrawal with the amount and the description 
        "Transfer to [Destination Budget Category]". 
        The method should then add a deposit to the other budget category with the amount 
        and the description "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. 
        This method should return True if the transfer took place, and False otherwise.
        '''
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + catagory.name)
      catagory.deposit(amount, "Transfer from " + self.name)
      return True
    return False

def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

    

  return(graph)
  # def chart_calc(self):
  #   total = 0
  #   for item in self.ledger:
  #     if item["amount"] < 0:
  #       total += item["item"]
  #   return total