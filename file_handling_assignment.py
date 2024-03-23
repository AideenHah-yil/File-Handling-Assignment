with open("my_file.txt", 'w') as f:
        f.write("First line\n")
        f.write("Second line\n")
        f.write("Third line\n")
         
       
with open("my_file.txt", 'r') as f:
        file_content = f.read()
        print(file_content)

with open("my_file.txt", 'a') as f:    
        f.write("Fourth line\n")
        f.write("fifth line\n")
        f.write("sixth line\n")    