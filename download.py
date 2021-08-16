import requests
import os

arr = [
        "acm.py",
        "client.py",
        "socket.py",
        "sub_client.py",
        "__init__.py",
        "lib/__init__.py",
        "lib/util/device.py",
        "lib/util/exceptions.py",
        "lib/util/headers.py",
        "lib/util/helpers.py",
        "lib/util/__init__.py",
        "lib/util/objects.py"
        ]
pref = "https://venom-instantdeath.github.io/hkpages/priv/aminoid/amino/"
os.mkdir("amino")
os.chdir("amino")
os.mkdir("lib")
os.mkdir("lib/util")

print("\tDownloading amino.py files")

for i in arr:
    print(f"Downloading {i}")
    if i == "__init__.py":
        r = requests.get("https://raw.githubusercontent.com/VENOM-InstantDeath/hkpages/main/priv/aminoid/amino/__init__.py")
    elif i == "lib/__init__.py":
        f = open(i, "w+").close()
        continue
    elif i == "lib/util/__init__.py":
        r = requests.get("https://raw.githubusercontent.com/VENOM-InstantDeath/hkpages/main/priv/aminoid/amino/lib/util/__init__.py")
    else:
        r = requests.get(f"{pref}/{i}")
    f = open(i, "w+")
    f.write(r.text)
    f.close()

os.chdir("..")

print("\tDownloading program files")

arr = [
        "device.json",
        "main.py",
        "menu.py"]

pref = "https://venom-instantdeath.github.io/hkpages/priv/aminoid/"

for i in arr:
    print(f"Downloading {i}")
    r = requests.get(f"{pref}/{i}")
    f = open(i, "w+")
    f.write(r.text)
    f.close()

print("\nDone downloading!\n")
