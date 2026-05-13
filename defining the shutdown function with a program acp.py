def shutdown(command) :
    if command == "yes":
        return "Shutting Down"
    elif command == "no":
        return "Shutdown aborted"
    else :
        return "Sorry"
    

#Example calls
print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("abc"))