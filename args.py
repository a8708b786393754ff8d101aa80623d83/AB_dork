from argparse import ArgumentParser

def parser(): 
    arg = ArgumentParser()
    arg.add_argument('-e', '--element', type=str, required=True, help='Enter the lement to search')
    arg.add_argument('-f', '--file-type', type=str, help='Dork to filetype')
    arg.add_argument('-t', '--in-text', type=str, help='Dork to intext')
    arg.add_argument('-a', '--in-all-text', type=str, help='Dork to inallatext')
    arg.add_argument('--google', type=bool, action='store_false', help='Google search use')
    arg.add_argument('--bing', type=bool, action='store_false', help='Bing search use')
    arg.add_argument('--duck-duck-go', type=bool, action='store_false', help='Duckduckgo search use')


    return arg.parse_args()