TYPES = ['1 = VARCHAR2(50)', '2 = NUMBER(10, 2)', '3 = DATE', 
                    '4 = INTEGER(10)', '5 = DECIMAL(10)']


class EnumsType():
    def __init__(self):
        pass

    def type(self, type, varCharSize = 250, numberSizeTuple = (10, 2),
                     integer = 10, decimal = 10):
        match type:
            case 1: 
                return f'VARCHAR2({varCharSize})'
            case 2: 
                return f'NUMBER{numberSizeTuple}'
            case 3:
                return 'DATE'
            case 4:
                return f'INTEGER({integer})'
            case 5:
                return f'DECIMAL({decimal})'
            
    
    def getAllEnumsType(self):
        return TYPES