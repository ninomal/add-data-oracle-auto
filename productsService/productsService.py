import cx_Oracle
from models.conection import Conection
import pandas as pd


class ProductsService():
    def __init__(self):
        self.conectionRow = Conection()
        self.conection = self.conectionRow.getConection()
        self.cursor = self.conection.cursor()
        self.columnsName = ""
        self.dictData = {}

    def addDataOracle(self, dictData):
        try:
            insert_query = """
                INSERT INTO 
                    products(id_products, nome_products, marca, categoria, preco_unit, custo_unit)
                VALUES
                    (:id_products, :nome_products, :marca, :categoria, :preco_unit, :custo_unit)
                """
            
            self.cursor.execute(insert_query, dictData)

            # Commit the transaction
            self.conection.commit()  
            return ("Data added successfully!")

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)
        
    def addOracleDataAuto(self, columnsString, columnsStringValueTrigger, tableName, dictData):
        try:
            #self.getColumnsNames(tableName) old version
            #stringsInput = self.products.createColumnsAdd(self.columnsName) old version

            insert_query = f"""
                INSERT INTO {tableName}({columnsString})VALUES
                            ({columnsStringValueTrigger})
                """
            
            
            self.cursor.execute(insert_query, dictData)
            
            print(tableName)
            print(columnsString)
            print("inserquery\n")
            print(insert_query)
            print(dictData)

            print("\n\n")
            # Commit the transaction
            self.conection.commit()  
            print("Data added successfully!")
        
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)
        
    def getTableInfo(self, name):
        try:
            insert_query = f"""SELECT * FROM {name}"""
            select = self.cursor.execute(insert_query)
            selectFetch = select.fetchall()
            return selectFetch

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)

    def getColumnsNames(self, columns):
        try:
            insert_query = f"""SELECT * FROM {columns}
                                 WHERE ROWNUM = 1"""
            
            self.cursor.execute(insert_query)
            columnsDescription = [desc[0] for desc in self.cursor.description]
            self.columnsName = columnsDescription
            return ("Column Names:", columnsDescription)

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)
    
    def closed(self):
        self.cursor.close()
        self.conection.close()

    #Xlsx methods       
    def readXlsxRowSelect(self, path, columName):
        data = []
        try:
            df= pd.read_excel(path, engine='openpyxl')
            rowData = df[df[f'{columName}']== 12]
        
            #dict FILA
            data.append(rowData.to_dict(orient='records'))
            return data[0]
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
        except TypeError:
            return ("None type error")
        
    def readXlsxIloc(self, path, row):
        data = []
        try:
            df= pd.read_excel(path, engine='openpyxl')
            rowData = df.iloc[row]
        
            #dict FILA
            data.append(rowData.to_dict())
            return data[0]
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
        except TypeError:
            return ("None type error")
        
    def readXlsxIlocSheets(self, path, row, sheet):
        data = []
        try:
            df= pd.read_excel(path, engine='openpyxl', sheet_name= sheet)
            rowData = df.iloc[row]
        
            #dict FILA
            data.append(rowData.to_dict())
            return data[0]
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
 
    def getLenXlsx(self, path):
        try:
            df= pd.read_excel(path, engine='openpyxl')
            return (len(df)-1)
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
        
    def getLenXlsxSheets(self, path, sheet):
        try:
            df= pd.read_excel(path, engine='openpyxl', sheet_name= sheet)
            return len(df)
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
    
    def getXlsxCOlmunsName(self, path):
        try:
            df = pd.read_excel(path, header=0)
            return df.columns.tolist()

        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR ")
        except IndexError:
            return ("INDEX ERROR")
    
    def getXlsxCOlmunsNameSheets(self, path, sheet):
        try:
            df = pd.read_excel(path, header=0, sheet_name= sheet)
            return df.columns.tolist()

        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR ")
        except IndexError:
            return ("INDEX ERROR")

    def createTableAuto(self, nameTable, stringData):
        create_table_sql = f'''
            CREATE TABLE {nameTable} (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                {stringData}
            )
        '''
        print(create_table_sql)
        try:
            teste = self.cursor.execute(create_table_sql)
            print(f"Table '{nameTable}' created successfully.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Error code: {error.code}")
            print(f"Error message: {error.message}")

        # Commit the changes
        self.conection.commit()

    def readSheetsOfXlsx(self, path):    
        # Load the Excel file
        xls = pd.ExcelFile(path)

        # Step 2: Get the names of the sheets
        sheet_names = xls.sheet_names

        # Step 3: Print the sheet names
        print("Sheet names:", sheet_names)
        return sheet_names


    def checkTables(self, nameOfFile):
        tables = False
        insert_query = f""" SELECT * FROM DBA_TABLES WHERE TABLE_NAME = '{nameOfFile}' """
        
        try:
            self.cursor.execute(insert_query)
            tables = self.cursor.fetchall()
            if tables == []:
                return False
            else:
                return True
        except cx_Oracle.DatabaseError as e:
            print("errrorr")
            error, = e.args
            print(f"Error code: {error.code}")
            print(f"Error message: {error.message}")
            return True
 

          