from User import User

miriam = User("Miriam")
rosa = User("Rosa")
carolina = User("Carolina")

#User 1
miriam.make_a_deposit(120).make_a_deposit(180).make_a_deposit(150).withdraw_money(50).show_balance()

#User2
rosa.make_a_deposit(100).make_a_deposit(200).withdraw_money(100).show_balance()

#User3
carolina.make_a_deposit(600).withdraw_money(150).withdraw_money(250).withdraw_money(50).show_balance()

#Bonus
miriam.transfer_money(carolina,50).show_balance()
carolina.show_balance()