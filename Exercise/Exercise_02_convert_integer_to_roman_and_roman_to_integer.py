# Write a Python class to convert an integer to a roman numeral

class Roman:
    def __init__(self,integer):
        self.integer=integer

    def setValue(self):
        setRoman={
            1:"I",
            2:"II",
            3:"III",
            4:"IV",
            5:"V",
            6:"VI",
            7:"VII",
            8:"VIII",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            100:"C",
        }
        return setRoman.get(self.integer,"Null")

    def convertToRoman(self):
        pass




roman1=Roman(5)
roman1.convertToRoman()