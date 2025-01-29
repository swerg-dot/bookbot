def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)  
    words = file_contents.split()
    counter=0
    for word in words:
        counter+=1
    print(f'There are {counter} words in this text!')
main()
