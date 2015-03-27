'''index page of applequest.fallenofftheedge.com'''
if __name__ == '__main__':
    import library as lib
else:
    import webapp.library as lib

import os
os.environ["REQUEST_METHOD"] = "GET"
os.environ["QUERY_STRING"] = "redirect=game"


def html_p():
    '''docstring'''
    html = lib.get_html(lib.HTML_DIR + 'index.html')
    print(html)


def main():
    '''docstring'''
    form = lib.get_cgi_data()
    redirect = form.getfirst('redirect')
    
    lib.print_header()
    if redirect == None:
        html_p()
    elif type(redirect) == str:
        try:
            lib.print_me(lib.REDIRECT_DIR + 'to_' +
                         redirect.lower() + '.html')
        except FileNotFoundError:
            lib.print_me(lib.HTML_DIR + 'index.html')
    else:
        html_p()

if __name__ == '__main__':
    main()
