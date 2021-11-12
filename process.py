# here, python is opening the file "um-server-01.txt" using the `open()` method and saving the data as a variable.
log_file = open("um-server-01.txt")

# def is used to define functions in python, we are creating a function here with the name `sales_reports` with an argument of `log_file`.
def sales_reports(log_file):
    # you need to indent inside of the file to access the function as part of python functionality. line 7 is a standard for loop, with `line` being declared as a variable for every item in `log_file`
    for line in log_file:
        #indent once more to be within the for loop, we are performing a strip method here to remove whitespace, `rstrip()` in particular removes whitespace only on the right side of character bodies.
        line = line.rstrip()
        #unique to python, if you access an array with a comma, you are performing an array slice. the variable saved will have data FROM the left Index up TO the data on the right Index.
        day = line[0:3]
        #standard if comparitor, == is used to see if both sides are of matching value.
        if day == "Tue":
            #prints data to terminal.
            print(line)

#just like in js, you invoke a function on its own with the argument you want to pass through it.
sales_reports(log_file)
