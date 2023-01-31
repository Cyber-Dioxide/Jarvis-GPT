import webbrowser


def youtube(output):
    url = 'https://youtube.com/'
    query = '/results?search_query='
    splited_output = output.split()

    if 'search' in splited_output:
        output = output.replace('for', '', 1)
        output = output.replace('search', '', 1)
        output = output.replace(' ', '+')

        webbrowser.open(url + query + output)
    else:
        webbrowser.open(url)
