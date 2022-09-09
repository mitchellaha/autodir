import os
from pprint import pprint as pp

from directory_maker import create_lettered_folders, create_directory_if_not_exist
from url_maker import create_TCR_shortcut
from mongo import get_customers


ROOT_CUSTOMERS_FOLDER = r"C:\Users\mitch\Documents\Programming\Repositories\Plans-Directory-Structunator\TEST_ROOT_DRIVE\CUSTOMERS"
os.chdir(ROOT_CUSTOMERS_FOLDER)
CWD = os.getcwd()



voidListTest = ["Voided Customer"]
customerListTest = [
    {
        "CustomerName": "Barricade",
        "CustomerID": 6666666
    },
    {
        "CustomerName": "Cranes",
        "CustomerID": 7777777
    },
    {
        "CustomerName": "Scott",
        "CustomerID": 8888888
    },
    {
        "CustomerName": "Rail Services",
        "CustomerID": 9999999
    },
    {
        "CustomerName": "Voided Customer",
        "CustomerID": 0000000
    }
    ]


def customer_folder_creator(CustomerList):
    for customer in CustomerList:
        if customer["CustomerName"] not in voidListTest:
            startLetter = customer["CustomerName"][0].upper()
            if startLetter.isnumeric():
                startLetter = "#"

            # if "/" in customer["CustomerName"]:
            customer["CustomerName"].replace("/", "-")

            CUSTOMER_FOLDER_ROOT = os.path.join(CWD, startLetter, customer["CustomerName"])
            create_directory_if_not_exist(CUSTOMER_FOLDER_ROOT)
            foldersToCreate = ["2022", "2021", "Archive"]
            for folder in foldersToCreate:
                folderPath = os.path.join(CUSTOMER_FOLDER_ROOT, folder)
                create_directory_if_not_exist(folderPath)

            create_TCR_shortcut(customer["CustomerID"], customer["CustomerName"], CUSTOMER_FOLDER_ROOT)



def main():
    customerList = get_customers()
    create_lettered_folders()
    customer_folder_creator(customerList)

if __name__ == "__main__":
    main()



