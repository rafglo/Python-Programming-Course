def check_parantheses(text_path):
    """
    Function - check_parantheses
    Funckja sprawdzająca poprawność użytych w tekście nawiasów

    Input:
    text_path(string) - ścieżka do pliku z tekstem do sprawdzenia

    Output:
    True(boolean) - jeśli nawiasy zostały poprawnie użyte
    False(boolean) - jeśli nawiasy zostały niepoprawnie użyte
    
    """
    text = open(text_path, encoding="UTF-8").read()
    left = ["(", "[", "{", "<"]
    right = [")", "]", "}", ">"]
    parantheses = []
    for i in text:
        if i in left or i in right:
            parantheses.append(i)
    for i in range(len(right)):
        count_right = parantheses.count(right[i])
        count_left = parantheses.count(left[i])
        if count_right == count_left:
            continue
        else:
            return False
    for i in range(len(parantheses)-1):
        if parantheses[i] == parantheses[i+1]:
            return False
    ok = 1
    while ok:
        g = 0
        for i in range(len(parantheses)-1):
            try:
                if parantheses[i] in left:
                    if left.index(parantheses[i]) == right.index(parantheses[i+1]):
                        parantheses.pop(i)
                        parantheses.pop(i)
                        g += 1
            except:
                pass
        if g == 0:
            ok = 0
    if len(parantheses) != 0:
        return False
    else:
        return True


print(check_parantheses(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 3\tekst.txt"))
