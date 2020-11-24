import os

files = os.listdir()
print(files)

# Using readlines()
#filename = input()
for file in files:
    if file.endswith('.csv'):
        print('Processing: '+file)
        input_file = open(file, 'r')
        Lines = input_file.readlines()

        updated_data=[]
        # Strips the newline character
        for line in Lines:
            #updated_data.append(line.replace('||', '|""|'))
            updated_line=[]
            modified = False
            inter_line = line.strip()
            if inter_line.startswith('|'):
                inter_line = inter_line.replace('|', '""|', 1)
                print("1) " + inter_line)
                modified = True
            if inter_line.find('||') != -1:
                # do twice to take care of repeated separators (|)
                inter_line = inter_line.replace('||', '|""|')
                inter_line = inter_line.replace('||', '|""|')
                print("2) " + inter_line)
                modified = True
            if inter_line.endswith('|'):
                inter_line = inter_line[0:len(inter_line)-1] + '|""'
                print("3) " + inter_line)
                modified = True

            updated_data.append(inter_line + '\n')
        updated_data[-1] = updated_data[-1].strip()
        print(updated_data)

        # writing to file
        output_file = open('output/'+file, 'w')
        output_file.writelines(updated_data)
        output_file.close()
