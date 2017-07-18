#Use for, split(), and if to create a Statement that will print out words that start with 's':'

st = 'Print only the words that start with s in this sentence'
for line in st.split(" "):
    if line[0] == 's':
        print line


