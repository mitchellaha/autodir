import os


def create_shortcut(Link, Filename, IconPath, Directory = None):
    """Creates a Shortcut File"""
    fileName = f"{Filename}.url"
    filePath = os.path.join(Directory, fileName)

    with open(filePath, "w") as f:
        f.write(f"[InternetShortcut]\nURL={Link}\nIconIndex=0\nIconFile={IconPath}\n")
        f.close()