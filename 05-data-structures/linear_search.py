names = ['ali','khan','afaq']
idx=0
x = 'khan'
for var in names:
    if var==x:
        print(f"{x} found at index {idx}")
        break
    idx+=1
