def check(num):
    match num:
        case 0:
            return("Zero")
        case 1:
            return("One")
        case _:
            return("Other")

if __name__ == "__main__":
    print(check(0))
   
               