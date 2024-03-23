with open("my_file.txt", 'w') as f:
        f.write("First line\n")
        f.write("Second line\n")
        f.write("Third line\n")
         
       
with open("my_file.txt", 'r') as f:
        f.read()

with open("my_file.txt", 'a+') as f:    
        f.write("First line\n")
        f.write("fifth line\n")
        f.write("sixth line\n")    