
# python_LRB_utils
Python code for pharsing xml and perform sequiencial downloads. 
The exposed code **requires a well-formed and sanitized xml file** to work, 
otherwise the functions might throw some exceptions.
- *Example of use:*
```python
#by adding lines at the end of the file and running

#this return a list of all the values for the given 'tag' in the xml file
#and will add the specified string to the start of each value.
l = phrase_file('file.xml','tag','string')

#this will create a new list containing only the values ​​that own the string '.pdf'
f = list_filteder(l, '.pdf')

#if these values ​​were urls, this function would return the filename
n = obtain_filename(f)

#then we create a dictionary in which the keys are the urls and the values ​​are the file names.
d = create_dict(f,n)

#finally we download all the files sequentially, using the dictionary.
download_dict(d)
```
