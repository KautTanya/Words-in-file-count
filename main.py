"""Words-in-file-count"""
file = open("example.txt")
content = file.read()

content_list = content.split()
count_word = len(content_list)
print(count_word)

file.close()
