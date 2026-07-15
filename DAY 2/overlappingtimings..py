time = ["9.00 - 10.00",
        "10.00 - 11.00",
        "9.30 - 10.30",
        "10.30 - 11.00",
        "11.30 - 12.00"]

for i in range(len(time)):
    s1, e1 = time[i].split("-")
    s1 = float(s1)
    e1 = float(e1)

    for j in range(i + 1, len(time)):
        s2, e2 = time[j].split("-")
        s2 = float(s2)
        e2 = float(e2)

        if s1 < e2 and s2 < e1:
            print(time[i], "overlaps with", time[j])