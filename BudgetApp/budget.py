class Category:
    #set up function. Sets up list for categories
    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.current = 0

    #deposit function -  add to current
    def deposit(self, amount, descript = ''):
        self.ledger.append({"amount": amount, "description": descript})
        self.current += amount

    #withdraw function -  remove from current
    def withdraw(self, amount, descript = ''):
        if self.check_funds(amount):
            self.current -= amount
            self.ledger.append({"amount": -amount, "description": descript})
            return True
        else:
            return False

    #checks current balance
    def get_balance(self):
        return self.current

    #transfer function for withdraw -> deposit /// current change not needed
    def transfer(self,amount,cate_class):
        if self.withdraw(amount,"Transfer to "+cate_class.category):
          cate_class.deposit(amount,"Transfer from "+self.category)
          return True
        else:
          return False

    #checks current balance is large enough to process
    def check_funds(self, amount):
        if self.current >= amount:
            return True
        else:
            return False

    #print the final expenditure as table /// sectioned with comments
    # __str__ used for example provided
    def __str__(self):
      #adding **********'s and category
      form = "*"*((30-len(self.category))//2) + self.category
      form = form + "*"*(30-len(form)) + "\n"
      #set decript to left 23 chars /// set total to right 7 char
      for i in self.ledger:
        form += i["description"][:23].ljust(23)+str("{:.2f}".format(i["amount"]).rjust(7)) + "\n"
      form += "Total: "+str(self.current)
      return form

# used to round to nearest 10 //// used for chart function below
def rounder(x):
  if x<10:
    return 0
  return round(x/10.0)*10

def create_spend_chart(categories):
  chart_wd = []
  chart_max = 0
  #S will be what is returned for chart
  s = 0

  for i in categories:
    withdraw_amount=0
    for j in i.ledger:
      #adding chart_wd to string
      if j["amount"] < 0:
        withdraw_amount += -j["amount"]
        s += (-j["amount"])
    #max length of names
    if len(i.category) > chart_max:
      chart_max=len(i.category)
    chart_wd.append([i.category,withdraw_amount])

  #used to calculate the percentage of a certain category
  for i in chart_wd:
    i.append(rounder((i[1]/s)*100))
  s = ""
  s += "Percentage spent by category\n"

  #loop used for numbers and o's
  t = 100
  while t >= 0:
    # num + seperator left justified
    s += str(t).rjust(3) + "|" + " "
    #print o if applicable
    for i in range(len(chart_wd)):
      if chart_wd[i][2] >= t:
        s += "o" + "  "
      else:
        s += "   "
    t -= 10
    s += "\n"

  #adding ---------- to as seperator
  s += "    " + ("-"*10) + "\n"

  count=0
  #adds vertical letters/// each line is 1 letter added together
  for i in range(chart_max):
    s += "     "
    for j in range(len(chart_wd)):
      #used to add spacing to match longer categories
      if len(chart_wd[j][0]) - 1 < count:
        s += "   "
      #adds letter of category
      else:
        s += chart_wd[j][0][count]+"  "
    count += 1
    if i != chart_max-1:
      s += "\n"

  return s
