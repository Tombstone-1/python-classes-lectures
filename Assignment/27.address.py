# wap for enter address and validate.
address = input("Enter address = ")

alp_count = 0
lw_count = 0
upr_count = 0
dgt_count = 0
spc_count = 0
spl_count = 0

for ele in address:
    if ele.isalpha():
        alp_count += 1
        if ele.islower():
            lw_count += 1
        else:
            upr_count += 1
    elif ele.isdigit():
        dgt_count += 1
    elif ele.isspace():
        spc_count += 1
    else:
        spl_count += 1

print("No. of alphabets = ", alp_count)
print("No. of lower char = ", lw_count)
print("No. of upper char = ", upr_count)
print("No. of digit = ", dgt_count)
print("No. of space = ", spc_count)
print("No. of special char = ", spl_count)