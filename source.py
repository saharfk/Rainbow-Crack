import hashlib
import csv


def hash_password_hack(input_file_name, output_file_name):
    passWord = dict()
    s = list()
    for i in range(1000, 10000):
        passWord[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = str(i)

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            for grade in row[1:]:
                s.append(row[0] + ',' + passWord[grade])
    file_out = open(output_file_name, 'w')
    for l in s:
        file_out.write(l + '\n')
