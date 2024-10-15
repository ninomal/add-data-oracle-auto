from productsService.productsService import ProductsService
from products.products import Products
from ui.ui import Ui

def main():
    productsService = ProductsService()
    products = Products()
    #ui = Ui()
    
    
    #info tables
    #info = productsService.getTableInfo('products')
    #print(info)
    #path = input('Digite o caminho')
    #pathNoXLSX = ''

    r'''
    #for create table auto VARCHAR=250
    listOfColumns = productsService.getXlsxCOlmunsNameSheets(r"C:\Users\jonatas.leme\Documents\branylsul.xlsx", 'notas')
    print(listOfColumns)
    print(products.createTableAUtoVarchar(listOfColumns))
    stringDataCreateTable = products.createTableAUtoVarchar(listOfColumns)
    productsService.createTableAuto('branylsulteste', stringDataCreateTable)
    '''
    
    #path = r"C:\Users\jonatas.leme\Documents\branylsul.xlsx"
    path = r"C:\Users\jonatas.leme\Documents\clients.xlsx"
    sheets = 'clients'
    #sheets = 'notas'
    #rowLen = (products.getLenXlsxSheets(path, sheets) -1)
    #print(products.readXlsxIlocSheets(path, 2, sheets))
    #products.createDataSqlLines(path, sheets)
    #print(products.createAuto("clientsteste2", path, sheets))
    teste = products.addOracle(path, sheets, 'clientsteste2')



    """
    rowLen = productsService.getLenXlsxSheets(path, sheet)
    
    for row in range(rowLen):
        data = productsService.readXlsxIlocSheets(path, row, sheet)
        data.update({'ID': row})
    print(data)
    
    teste = products.refactEspecialCara(data.keys())
    print(len(teste))
    conts = 0
    testao = {}
    for keys , value in data.items():
        testao.update({teste[conts] : value})
        conts +=1
    print(testao)

    """

    #products.addOracle(path, sheet, 'branylsulnotasteste')
    r'''
    #PARA COLOCA NO BANCO SQL
    path = r"C:\Users\jonatas.leme\Documents\branylsul.xlsx"
    sheet = 'fios'
    rowLen = productsService.getLenXlsxSheets(path, sheet)
    for row in range(rowLen+ 1):
        data = productsService.readXlsxIlocSheets(path, row, sheet)
        data.update({'ID': row})
        print(productsService.addOracleDataAuto('branylsulteste', data))
    '''

    #for update data NO Sheet
    #path = r"C:\Users\jonatas.leme\Documents\clients.xlsx"
    #rowLen = productsService.getLenXlsx(path)
    #for row in range(rowLen+ 1):
        #data = productsService.readXlsxIloc(path, row)
        #data.update({'ID': row})
        #productsService.addOracleDataAuto('products4teste', data)


    #for create table list
    #print(productsService.getXlsxCOlmunsName(r"C:\Users\jonatas.leme\Documents\clients.xlsx"))
    #listOfColumns = productsService.getXlsxCOlmunsName(r"C:\Users\jonatas.leme\Documents\clients.xlsx")
    #print('\n\n\n\'', products.getEnumsType())
    #listCreateTable = [1, 1, 3 ,1, 1, 1, 1 ,1 ,1 ,1]
    #print(products.createTable(listOfColumns, listCreateTable))
    #stringDataCreateTable = products.createTable(listOfColumns, listCreateTable)
    #productsService.createTableAuto('products3', stringDataCreateTable)







    #for add value in row auto
    #print(productsService.getColumnsNames('products'))
    #data = {'ID_PRODUCTS': 6, 'NOME_PRODUCTS':'phone razer', 'MARCA':'RAZER',
            #'CATEGORIA':'microhpone', 'PRECO_UNIT': 800, 'CUSTO_UNIT': 450}
    #print(productsService.addOracleDataAuto('products', data))




    #data = {'id_products': 5, 'nome_products': 'samsung home', 'marca': 'samsung','categoria': 'eletronico', 'preco_unit': 500, 'custo_unit': 150}
    #productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

