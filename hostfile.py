ips_in_file = set()
with open("hosts", "r") as file:
    # for line in file:
    #     print(line)
    for line in file:
        line = line.strip()
        if line.startswith("172.16"):
            print(line)
            tb = line.find("\t")
            print(tb)

# ips_in_file = set()
# with open("hosts", "r") as file:
#     for line in file:
#         line = line.strip()
#         if line.startswith("172.16"):
#             tb = line.find('\t')
#             if tb != -1:
#                 ip = line[:tb]
#             else:
#                 ip = line
#             ips_in_file.add(ip)



# for i in range (10,12):
#     #print (i)
#     for j in range (1,21):
#         si = str (i)
#         sj = str (j)
#         ipvalue = "172.16." + si + "." + sj
#         print(ipvalue)

