class Order():
    total_orders = 0
    __price = 35  #Private class variable
    __number = 0
    
    def __init__(self, amount=1, spicy=False):
        self._amount = amount   #Protected instance variable
        self._spicy = spicy
        Order.total_orders += 1

    def check(self):
        sum = self._amount * Order.__price

        sauce = 'spicy' if self._spicy else 'not spicy'
        print(f'You have ordered {self._amount} burger(s) which are {sauce}. Total price is ${sum}.')

    @property  #Getter for private class variable
    def number(self):
        return self.__number

    @property
    def amount(self):
        return self._amount
    
    @amount.setter #Setter for protected instance variable
    def amount(self, n):
        if n > 0:
            self._amount = n
        else:
            print("Amount must be positive!")

    @staticmethod
    def quote():
        print(f"Burger is worth ${Order.__price} each!")

    def __str__(self): #String representation
        return f'Order(amount={self._amount}, spicy={self._spicy})'
    
    def __repr__(self): #Official string representation
        return f'Order(amount={self._amount}, spicy={self._spicy})'