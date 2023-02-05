#method vs classmethod vs staticmethod
#method - self método de instância
#@Classmethod - cls, método de classe
#@staticmethod - método estático (Xself, Xcls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): #set_nomedosetter
        #setter
        self.user = user

    def set_password(self, password):
        self.password = password
        #toda vez que precisa usar self, user_self, esse método é um método de instância

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print(msg)

    def connection_log(msg):
        print('LOG:', msg)


print(Connection.log('Essa é a mensagem de log'))
c1 = Connection.create_with_auth('Carol', '1234')
c1 = Connection()

c1.set_user('carol')
c1.set_password('123')
print(c1.user)
print(c1.password)