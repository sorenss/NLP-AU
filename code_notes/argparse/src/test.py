import argparse

def arg_inputs():
    #initialize parser
    my_parser = argparse.ArgumentParser(description="A script that says hello.")
    #add argument
    my_parser.add_argument("-n",  #short name
                            "--name", #long name
                            type=str,
                            required=True, #if an argument is obligatory
                            help="The name to say hello to.")

    #the list of arguments given 
    args = my_parser.parse_args()
    return args

def hello(name:str) -> str:
#    print(f"hi, my name is {my name}!!!") #we change away from this
    print(f"Hello, my name is {name}!!!")

def main():
    #get the command line args
    arguments = arg_inputs()
    hello(arguments.name)

if __name__=="__name__":      #boilerplatecode - det gør at det kun blir kørt når kaldt fra cmd; ikke hvis man importerer det, hvilket ville give fejl
    main()