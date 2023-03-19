from argparse import ArgumentParser, Namespace

def parser() -> Namespace: 
    """Argument ligne de commande

    Returns:
        Namespace: type argparse
    """
    
    arg = ArgumentParser()
    arg.add_argument('-e', '--element', type=str, help='Enter the lement to search')
    
    arg.add_argument('--file-type', type=str, help='Dork to filetype')
    arg.add_argument('--in-text', type=str, help='Dork to intext')
    arg.add_argument('--in-all-text', type=str, help='Dork to inallatext')
    arg.add_argument('--map', type=str, help='Dork to map')
    arg.add_argument('--film', type=str, help='Dork to film')
    arg.add_argument('--in-anchor', type=str, help='Dork to inanchor')
    arg.add_argument('--blog-url', type=str, help='Dork to blogurl')
    arg.add_argument('--loc', type=str, help='Dork to loc')
    arg.add_argument('--site', type=str, help='Dork to site')
    arg.add_argument('--extension', type=str, help='Dork to extension')
    
    arg.add_argument('-c', '--counter-page', type=int, default=1, help='Number page for requests')

    arg.add_argument('--google', action='store_true', help='Google search use')
    arg.add_argument('--bing', action='store_true', help='Bing search use')
    arg.add_argument('--duck-duck-go', action='store_true', help='Duckduckgo search use')


    return arg.parse_args()