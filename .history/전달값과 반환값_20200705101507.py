def open_account():
    print("새로운 계좌가 개설되었습니다.")


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money) # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)
