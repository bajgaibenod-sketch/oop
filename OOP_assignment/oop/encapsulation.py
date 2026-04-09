class Password:
    def __init__(self,password):
        self.__password=password
    def check_password(self,guess):
        if guess==self.__password:
            return True
        return False
guess=Password('password123')
print(guess.check_password('password123'))