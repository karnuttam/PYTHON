class Account:
    def __init__(self, acc_bal, acc_pass):
        self.acc_bal = acc_bal;
        self.__acc_pass = acc_pass; #conceptually Private access specifier
    def get_pass(self):
        print(self.__acc_pass);
    

A = Account(4512, 235);
print(A.acc_bal);
A.get_pass();
#print(A.__acc_pass);
