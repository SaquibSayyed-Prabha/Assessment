# Q10. Create Payment, CreditCardPayment, UPIPayment and NetBankingPayment classes. Override pay() method.
print("Q10. Create Payment, CreditCardPayment, UPIPayment and NetBankingPayment classes. Override pay() method.")
class Payment:
    def pay(self):
        print("Processing payment...")

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card.")

class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI.")

class NetBankingPayment(Payment):
    def pay(self):
        print("Paid using Net Banking.")

p = UPIPayment()
p.pay()