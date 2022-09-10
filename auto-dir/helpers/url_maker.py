import os
from directory_maker import create_directory_if_not_exist


def create_URL_string(Link, Icon):
    returnString = f"[InternetShortcut]\nURL={Link}\nIconIndex=0\nIconFile={Icon}\n"
    return returnString


def create_TCR_shortcut(CustomerID, CustomerName, Directory = None):
    TCR_ICON = r"\\10.110.109.11\plans\assets\tcr-logotran.ico"
    tcrCustomerLink = f"http://apps.tcrsoftware.com/tcr_2/webforms/folder.aspx?Folder=CUSTOMER&CustomerID={CustomerID}"

    fileName = f"TCR - {CustomerName}.url"
    if Directory is not None:
        filePath = os.path.join(Directory, fileName)
    else:
        filePath = os.path.join(CustomerName, fileName)
    create_directory_if_not_exist(os.path.dirname(filePath))

    with open(filePath, "w") as f:
        f.write(create_URL_string(tcrCustomerLink, TCR_ICON))
        f.close()
