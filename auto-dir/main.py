import os
import re

from helpers.directory_maker import create_lettered_folders, create_directory_if_not_exist, create_directory_list, create_subdir_list
from helpers.url_maker import create_TCR_shortcut
from helpers.mongo import get_customers
from config import foldersToCreate, ROOT_FOLDER, IGNORED_CUSTOMERS


os.chdir(ROOT_FOLDER)
CWD = os.getcwd()


def customer_folder_creator(CustomerList):
    customerSubdirs = create_subdir_list(foldersToCreate)
    for customer in CustomerList:
        if customer["CustomerName"] not in IGNORED_CUSTOMERS:
            startLetter = customer["CustomerName"][0].upper()
            if startLetter.isnumeric():
                startLetter = "#"

            customer["CustomerName"] = re.sub(r'[\\/:"*?<>|]+', "-", customer["CustomerName"])

            CUSTOMER_FOLDER_ROOT = os.path.join(CWD, startLetter, customer["CustomerName"])
            create_directory_if_not_exist(CUSTOMER_FOLDER_ROOT)
            for folder in [str(CUSTOMER_FOLDER_ROOT + subDir) for subDir in customerSubdirs]:
                create_directory_if_not_exist(folder)

            create_TCR_shortcut(customer["CustomerID"], customer["CustomerName"], CUSTOMER_FOLDER_ROOT)


def main():
    customerList = get_customers()
    create_lettered_folders(CWD)
    customer_folder_creator(customerList)

if __name__ == "__main__":
    import time
    start_time = time.time()
    
    main() # BEAT --- 18.559240102767944 seconds --- > --- 17.997341632843018 seconds ---

    print("--- %s seconds ---" % (time.time() - start_time))



