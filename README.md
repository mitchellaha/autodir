# auto-dir

> Directory Tree Creator for Windows

### Sample Blocks


#### Folder

```python
{
    "Name": "Folder_Name",
    "Type": "Folder",
    "Subfolders": [
    {
        "Name": "PDF",
        "Type": "Folder",
        "Subfolders": None
    }
    ]
}
```

#### Shortcut

```python
{
    "Name": "Shortcut_Name",
    "Type": "Shortcut",
    "Config": {
        "IconPath": "Z:\\assets\\github.ico",
        "Link": "https://github.com"
    }
}
```