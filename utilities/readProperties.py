import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common_info', 'baseurl')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common_info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def getAddress():
        address = config.get('common_info', 'address')
        return address

