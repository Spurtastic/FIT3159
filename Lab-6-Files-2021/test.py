import os
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


# PARSING SED INSTRUCTION HIT RATIOS

for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' sed-{size}.txt |head -1 > output.txt")

    with open("instruction-sed.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("instruction-sed.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()


"""====================================================================="""
#PARSING SED DATA HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]

for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' sed-{size}.txt |tail -2|head -1 > output.txt")

    with open("data-sed.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("data-sed.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()


"""================================================================================================="""
#PARSING su2 DATA HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' su2-{size}.txt |tail -2|head -1 > output.txt")

    with open("data-su2.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("data-su2.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()
"""==============================================================================================="""
#PARSING su2 INSTRUCTION HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' su2-{size}.txt |head -1 > output.txt")

    with open("instruction-su2.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("instruction-su2.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()

"""================================================================================================="""
#PARSING swm DATA HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' swm-{size}.txt |tail -2|head -1 > output.txt")

    with open("data-swm.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("data-swm.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()
"""==============================================================================================="""
#PARSING swm INSTRUCTION HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' swm-{size}.txt |head -1 > output.txt")

    with open("instruction-swm.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("instruction-swm.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()



"""================================================================================================="""
#PARSING tex DATA HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' tex-{size}.txt |tail -2|head -1 > output.txt")

    with open("data-tex.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("data-tex.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()
"""==============================================================================================="""
#PARSING tex INSTRUCTION HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' tex-{size}.txt |head -1 > output.txt")

    with open("instruction-tex.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("instruction-tex.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()




"""================================================================================================="""
#PARSING wave DATA HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' wave-{size}.txt |tail -2|head -1 > output.txt")

    with open("data-wave.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("data-wave.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()
"""==============================================================================================="""
#PARSING wave INSTRUCTION HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' wave-{size}.txt |head -1 > output.txt")

    with open("instruction-wave.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("instruction-wave.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()





"""================================================================================================="""
#PARSING yacc DATA HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' yacc-{size}.txt |tail -2|head -1 > output.txt")

    with open("data-yacc.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("data-yacc.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()
"""==============================================================================================="""
#PARSING yacc INSTRUCTION HIT RATIOS
list = [1024, 2048, 4096, 8192, 16384, 32768, 65536]


for size in list:
    os.system(f"grep -A 1 -m 2 'Hit ratio' yacc-{size}.txt |head -1 > output.txt")

    with open("instruction-yacc.dat","r") as f:
        list = f.readlines()
    f.close()
    with open("output.txt", "r") as f:
        lst = f.readline().split(" ")
    f.close
    for n in lst:
        val = n.strip("\n")
    for i in range(len(list)):
        if str(size) in list[i] :
            list[i] = f"{list[i].split()[0]}\t{val}\n"
    print(list)
    print(size, "done\n")
    file = open("instruction-yacc.dat", "w")
    contents = "".join(list)
    file.write(contents)
    file.close()

