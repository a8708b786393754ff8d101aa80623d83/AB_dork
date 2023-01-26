from argparse import ArgumentParser

def parser(): 
    arg = ArgumentParser()
    arg.add_argument('-e', '--element', type=str, help='Enter the lement to search')
    arg.add_argument('-f', '--file-type', type=str, help='Dork to filetype')
    arg.add_argument('-t', '--in-text', type=str, help='Dork to intext')
    arg.add_argument('-a', '--in-all-text', type=str, help='Dork to inallatext')
    arg.add_argument('--google', action='store_true', help='Google search use')
    arg.add_argument('--bing', action='store_true', help='Bing search use')
    arg.add_argument('--duck-duck-go', action='store_true', help='Duckduckgo search use')


    return arg.parse_args()