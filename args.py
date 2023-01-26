from argparse import ArgumentParser

def parser(): 
    arg = ArgumentParser()
    arg.add_argument('-e', '--element', type=str, required=True, help='Enter the lement to search')
    arg.add_argument('-f', '--file-type', action='store_false', help='Dork to filetype')
    arg.add_argument('-t', '--in-text', action='store_false', help='Dork to intext')
    arg.add_argument('-a', '--in-all-text', action='store_false', help='Dork to inallatext')

    return arg.parse_args()