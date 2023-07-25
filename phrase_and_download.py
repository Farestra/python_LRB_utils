#!/usr/bin/env python3

#Imports
from xml.etree import ElementTree as ET
import requests
import os
from time import sleep
import random

#Functions
def clear_stdout():
    """Clear stdout based on OS name
    """
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        
def verify_exists(f: str) -> bool:
    """Check if file exists in the current directory.

    Args:
        f (str): file path

    Returns:
        bool: True if exists, False if not.
    """
    try:
        r = os.path.exists(os.getcwd()+os.sep+str(f))
        return r
    except Exception as e:
        print(e)

def pharse_file(f: str, k: str, p: str = None) -> list:
    """Return a list of all values for a specific key of a given xml file.
    This function requires a sanitized xml file.

    Args:
        f (str): Path for the xml file
        k (str): Key in the given xml file to search values
        p (str, optional): String to concatenate with values. Defaults to None.

    Returns:
        list: list of all values for a key in the given xml file
    """
    u = list()
    try:
        tree = ET.parse(f)
        for i in tree.findall(".//"+str(k)):
            if p:
                j = p+i.text.strip() 
                u.append(j)
            else:
                j = i.text.strip() 
                u.append(j)
        return u
    except Exception as e:
        print(e)

def list_filtered(l: list, filter: str) -> list:
    """Return a new list containing only elements of the given list 
    that match filter string
    
    Args:
        l (list): Given list of strings to apply filter string
        filter (str): Filter string

    Returns:
        list: Returned new list containing only filtered elements
    """
    u = list()
    try:
        n = [x for x in l if filter in x]
        return n
    except Exception as e:
        print(e)

def obtain_filename(l: list) -> list:
    """Return a list of filenames from a list of urls
    
    Args:
        l (list): Given List of url's

    Returns:
        list: Returned list of filenames
    """
    n = list()
    try:
        for i in l:
            p = i.rfind("/") + 1
            s = i[p:]
            n.append(s)
        return n
    except Exception as e:
        print(e)

def create_dict(l1:list, l2:list) -> dict:
    """Takes two list of the same lenght and returns a dictionary with the first
    list elements as keys, and the second list elements as values.

    Args:
        l1 (list): List for keys
        l2 (list): List for values

    Returns:
        dict: Dictionary with elements of the first list as keys and 
        the second list elements as values
    """
    u = dict()
    try:
        u = {l1[i]: l2[i] for i in range(len(l1))}
        return u
    except Exception as e:
        print(e)

def download_file(url: str, fname: str) -> bool:
    """Donwload a file from given url and save it in the current working directory with the given name.
    Args:
        url (str): ULR to download
        fname (str): File name to save
    Returns:
        bool: True if the file was written. False if not.
    """
    try:
        if verify_exists(fname):
            return False
        else:
            r = requests.get(url, stream=True)
            if r.status_code == requests.codes.ok:
                with open(fname, "wb") as f:
                    for data in r:
                        f.write(data)
            return True
    except Exception as e:
        print(e)
        return False
    
def download_dict(d:dict, w: int = 1) -> None:
    """Sequentially download files from a dictionary where the keys are the url 
    and the values are the name of the file. Wait at least one second between downloads

    Args:
        d (dict): Dictionary where keys are urls and values are filenames
        w (int, optional): Time to wait between downloads. Defaults to 1.
    """
    try:
        for k, v in d.items():
            r = download_file(k,v)
            if r:
                print(str(v)+" OK")
            else:
                print(str(v)+" File already exists")
            t=random.randint(0,w)
            sleep(t)
            clear_stdout()
    except Exception as e:
        print(e)
