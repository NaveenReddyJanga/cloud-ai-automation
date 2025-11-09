import os

source = 'data/sample.txt'
destination = 'outputs/reversed_sample.txt'

# read the content of the source file

with open(source,'r',encoding = 'utf-8') as f:
    content = f.read()
# reverse the content
reversed_content = content[::-1]

# write the reversed content to the destination file
with open(destination , 'w',encoding = "utf-8") as f:
    f.write(reversed_content)

print(f"Reversed content written to {destination}")


# # works fine for basic text files
# with open("data/sample.txt", "r") as f:
#     content = f.read()
# with open("output/reversed.txt", "w") as f:
#     f.write(content[::-1])
# print("File content reversed and saved to output/reversed.txt")