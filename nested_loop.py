data=""
while 1:
    data=raw_input("Command: ")
    if data in ("test", "experiment", "try"):
        data2=""
        while data2=="":
            data2=raw_input("Which test? ")
        if data2=="chemical":
            print("You chose a chemical test.")
        else:
            print("We don't have any " + data2 + " tests.")
    elif data=="quit":
        break
    else:
        pass