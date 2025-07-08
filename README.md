# CSV-to-SQL
I was trying to import one of my big CSV files into a MySQL database, but the in Workbench, the import tool always generated some kind of error.
So I decided to make it manually, but as obvious, I didn't want to type the 10000 lines one-by-one into an insert.
That's why I made this little script. And also, it was a good practice.
Feel free to use it, and modify if you think it can be improved.

## Requirements and usage
- Source file must be in CSV format
- In default the delimiter is set to ; - if you want to change, you can find the variable in the beginning of the script (**delim**)
- You can also set the output directory and filename in the beginning in the **resfile** variable
- It needs two input after you started to run: first is the csv file you want to convert (full path needed)
- The second is the desired table name
- If you want to abort, in the file input, you can type 'exit'

The script first checks ALL the fields in the dataset. If all the fields in one column belongs to exactly one type of data, it will be assinged that type. If any field has different datatype than the others, it will be varchar(255)

You can reach me here if you want: rkoczur@gmail.com

Happy coding :)
