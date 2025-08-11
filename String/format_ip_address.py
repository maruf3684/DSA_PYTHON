address = "255.100.50.0"

ans = []
for i in address:
    if i == ".":
        ans.append(f"[{i}]")
    else:
        ans.append(i)
print("".join(ans))