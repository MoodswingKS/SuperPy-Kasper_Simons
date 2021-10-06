## get ID as string or int

Through the use of a helper function called get_item_or_max, I've used the type() check to return either a string or integer.  
If it's a string, my function to create an ID instantly knows the product is in inventory.  
In the case of an integer, it knows the ID is created because the product or its expiration date has not been in inventory yet.

```python
def get_item_or_max(path, product_name, exp_date):
    """
    return id as a string or an int
    """
    exp_match = datetime.strftime(exp_date, '%d/%m/%Y')
    max_value = 0
    
    for item in path:
        if product_name == item[1] and exp_match == item[-1]:
            return item[0]
        elif product_name == item[1]:
            new_id = f'{item[0]}{exp_date}'
            new_id_string = new_id.replace('-', '')
            return new_id_string
        max_value = max(item[0])
    return int(max_value) 
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
