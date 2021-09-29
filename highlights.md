## Classes

Through the use of classes, I've made a global path for each of the .csv paths. All of them can be used through the project, by simply accessing the class. 

```python
  def __init__(self):
        self.bought_path = os.path.join(data_paths, 'bought.csv')
```
Which can be used by simply writing:
```python
        super_bought.bought_path
```

## Advance Time

While creating the advance time feature, I've come across a weird bug which wouldn't let me use the a+ or w+ modes in the text file. Which made me unable to write the new time in my text file. I've used an unconventional method to get around this, and I'm proud of this one.

```python
        with open(time_file, mode='r+') as current_date:
            for line in current_date:
                text = line[-10:]
```

Instead of reading from a new line, the global_date will always return the last 10 characters from the text file.  
_Unless they want to use this for eons, this will always keep on working correctly._


## Parser Help Texts

I've created custom help paths for each of the subparsers in the code. They can be accessed by checking the parser_text.py in the project. 
With the Rich-module I've made them look green and made words bigger were a format was implied, to improve their readability for everyone who might use it. But most of all, to have them give this nostalgic vibe for everyone who has ever worked with CLT's before.   
I've even included a kind of easter egg in the form of credits to be seen with writing:

```python
$ python main.py credits super
```
