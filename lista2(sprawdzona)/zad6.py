def column(op):
    """
    Function:
    Funkcja tworząca działanie w słupku z wynikiem 

    Input:
    op(string) - działanie w postaci ciągu znakow

    Output:
    col_str(string) - słupek działania z wynikiem

    """
    op_sp = op.split("+")
    for i in range(len(op_sp)):
        op_ss = op_sp[i].split("-")
        op_sp[i] = op_ss
    result = 0
    col_list = []
    for i in range(len(op_sp)):
        if len(op_sp[i]) == 1:
            result += int(op_sp[i][0])
            col_list.append("+" + op_sp[i][0])
        else:
            result += int(op_sp[i][0])
            col_list.append("+" + op_sp[i][0])
            for j in range(1,len(op_sp[i])):
                result -= int(op_sp[i][j])
                col_list.append("-" + op_sp[i][j])
    col_list[0] = col_list[0].replace("+", "")
    col_str = ""
    lens = [len(str(result)), len(col_list[0])]
    for i in range(1, len(col_list)):
        lens.append(len(col_list[i]) - 1)
    lgst = max(lens)
    col_str += " " * (lgst - len(col_list[0]) + 1) + col_list[0]
    for i in range(1, len(col_list)):
        num = ""
        for j in range(1, len(col_list[i])):
            num += col_list[i][j]
        col_str += "\n" + col_list[i][0] + " " * (lgst - len(col_list[i])+ 1) + num
    col_str += "\n" + "-" * (lgst + 1)
    col_str += "\n" + " " * (lgst - lens[0]+1) + str(result) 

    return col_str
