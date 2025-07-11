for j in range(2,21):
    filename=f"table/table_{j}.txt"
    
    with open(filename,"w") as f:
        for i in range(1,11):
           f.write(f"{j} X {i} = {j*i}\n")

   