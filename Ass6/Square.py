x = int(input("Voer een getal in "))    # (1, S.x) -> (PC + 1, S[x-> int(input(S.x + (3)))])
i = 0                                   # (2, S.i) -> (PC + 1, S[i-> (S.i + (0))])
while i < x:                            # (3, S) wVRB->(firstLine(B, S) when S[i] < x) | (PC,S) wVRB->(skipAfter(B, S) when S[i] !< x)
    text = ""                           # (4, S.text) -> (PC + 1, S[text -> ("")])
    i += 1                              # (5, S.i) -> (PC + 1, S[i -> (S.i + (1))])
    j = 0                               # (6, S.j) -> (PC + 1, S[j-> (S.j + (0))])
    while j < x:                        # (7, S) wVRB->(firstLine(B, S) when S[j] < x) | (PC,S) wVRB->(skipAfter(B, S) when S[j] !< x)
        text = text + "#"               # (8, S.text) -> (PC + 1, S[text -> (S.text + (""))])
        j += 1                          # (9, S.j) -> (PC + 1, S[j-> (S.j + (1))])
    print(text)                         # (10, S.text) -> (PC + 1, S[text -> print(S.text)])