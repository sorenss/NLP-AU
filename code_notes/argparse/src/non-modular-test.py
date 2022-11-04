import argparse

#initialize parser
my_parser = argparse.ArgumentParser(description="A script that says hello.")
#add argument
my_parser.add_argument("-n",  #short name
                        "--name", #long name
                        type=str,
                        required=True, #if an argument is obligatory
                        help="The name to say hello to.")

#the list of arguments given, 
args = my_parser.parse_args()

def hello(name:str) -> str:
#    print(f"hi, my name is {my name}!!!") #we change away from this
    print(f"Hello, my name is {name}!!!")

hello(args.name)