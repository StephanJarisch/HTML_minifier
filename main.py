import argparse, copy
import numpy as np

parser = argparse.ArgumentParser(description="Set html file name to process")
parser.add_argument("--file", metavar="file", type=str, help="pass the file you want to process")

args = parser.parse_args()


def get_rid_of_comments(line):
    new_line = copy.deepcopy(line)

    for i in range(1, len(line)):
        if new_line[i-1:i+1] == "//" and new_line[i-7:i-1] != "https:":
            new_line = new_line[:i-1]
            break
    
    if new_line == "":
        return ""
    else:
        return new_line

def get_rid_of_empty_lines(line):
    new_line = copy.deepcopy(line)

    if line == "" or line == "\n":
        return ""
    else:
        return line

def get_rid_of_whitespace(line):
    new_line = copy.deepcopy(line)

    new_line = new_line.replace(": ", ":")
    new_line = new_line.replace(" :", ":")

    new_line = new_line.replace("= ", "=")
    new_line = new_line.replace(" =", "=")

    new_line = new_line.replace(" {", "{")
    new_line = new_line.replace("{ ", "{")

    new_line = new_line.replace(", ", ",")
    new_line = new_line.replace(" ,", ",")

    new_line = new_line.replace("* ", "*")
    new_line = new_line.replace(" *", "*")

    new_line = new_line.replace("+ ", "+")
    new_line = new_line.replace(" +", "+")

    new_line = new_line.replace("- ", "-")
    new_line = new_line.replace(" -", "-")


    new_line = new_line.replace("; ", ";")
    new_line = new_line.replace(" ;", ";")

    new_line = new_line.replace("< ", "<")
    new_line = new_line.replace(" <", "<")


    new_line = new_line.replace("> ", ">")
    new_line = new_line.replace(" >", ">")


    new_line = new_line.replace("( ", "(")
    new_line = new_line.replace(" (", "(")


    new_line = new_line.replace(") ", ")")
    new_line = new_line.replace(" )", ")")

    new_line = new_line.replace("? ", "?")
    new_line = new_line.replace(" ?", "?")

    new_line = new_line.replace("! ", "!")
    new_line = new_line.replace(" !", "!")

    return new_line

def minify_html(file):
    with open(file, "r") as f:
        data = f.readlines()

    new_lines = []
    for idx, line in enumerate(data):
        
        line = get_rid_of_empty_lines(line.strip())
        line = get_rid_of_comments(line)
        line = get_rid_of_whitespace(line)

        if line != "":
            new_lines.append(line)

    text = "".join(new_lines)
    #print(text)

    with open(file.split(".")[0] + "_min.html", "w") as f:
        f.write(text)



            


if __name__ == "__main__":
    if isinstance(args.file, str):
        minify_html(args.file)


