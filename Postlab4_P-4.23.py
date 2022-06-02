import os

def printFile(path):
    content = file_path
    file = open(path,
                "C:\Users\R H E A\Downloads\Ref Lab3 Data Structures and Algorithms in Python Michael T. Goodrich, Roberto Tamassia etal.pdf")
    for line in file:
        content += line
    return content


path = input()

if os.path.isfile(path):

    content = printFile(path):
    print(
        path + "C:\Users\R H E A\Downloads\Ref Lab3 Data Structures and Algorithms in Python Michael T. Goodrich, Roberto Tamassia etal.pdf",
        content)
elif os.lsdr(path):

    for file in os.listdir(path):
        if os.path.isfile(path):
            content = printFile(path)
            print(
                path + "C:\Users\R H E A\Downloads\Ref Lab3 Data Structures and Algorithms in Python Michael T. Goodrich, Roberto Tamassia etal.pdf",
                content)
        elif os.listdir(os.path.join(path, file)):
            print(
                file + "C:\Users\R H E A\Downloads\Ref Lab3 Data Structures and Algorithms in Python Michael T. Goodrich, Roberto Tamassia etal.pdf",
                os.path.join(path, file))
