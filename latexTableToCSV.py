import re
def latexTableToCSV(inputfile='input.txt'):
    with open(inputfile,'r') as file:
        content = file.read()
        print("finish reading")
        content = content.split("\\\\")
        for index in range(len(content)):
            content[index] = re.sub(r" ",'',content[index] )
            content[index] = re.sub("\(",r'"(', content[index])
            content[index] = re.sub("\)",r'")', content[index])
            content[index] = re.sub("&",",", content[index])
            content[index] = re.sub("\\\\", "",content[index])
            content[index] = re.sub("hline", "",content[index])

            print("finish line",index+1)
        with open("output.txt","w") as output:
            output.writelines(content)
            output.close()
        file.close()
def latexTableCleanUp(inputfile='input.txt'):
    with open(inputfile,'r') as file:
        content = file.read()
        print("finish reading")
        content = content.split("\\\\")
        for index in range(len(content)):
            content[index] = re.sub(r" ",'',content[index] )
            print("finish line",index+1)
        with open("output.txt","w") as output:
            output.writelines(content)
            output.close()
        file.close()