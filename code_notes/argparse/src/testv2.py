import argparse
import pandas as pd

def arg_inputs():
    # initialize parser
    my_parser = argparse.ArgumentParser(description="A script that says hello.")
    # add arguments
    my_parser.add_argument("-n",
                        "--name",
                        type=str,
                        required=True,
                        help="The name to say hello.")
    my_parser.add_argument("-a",
                        "--age",
                        type=int,
                        required=True,
                        help="The age of the person.")
    # the list of arguments given
    args = my_parser.parse_args()
    # return list of arguments
    return args

def person_info(name:str, age:int) -> pd.DataFrame:
    df = pd.DataFrame([[name, age]], columns=["name", "age"])
    print(df)

def main():
    # get the command line arguments
    arguments = arg_inputs()
    # print the hello function
    person_info(arguments.name, arguments.age)

if __name__=="__main__":
    main()