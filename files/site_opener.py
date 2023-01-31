
def opener(output):
    outputt = outputt.replace('for', '')
    outputt = outputt.split()
    search_index = outputt.index('open') + 1
    x = outputt[search_index]
    if x in sits_names:

        site = 'https://' + x + '.com'

        if 'search' in outputt:
            query = outputt.index('search') + 1
            query = outputt[query:]

            search = ''
            for word in query:
                search += word + '+'
            printWithSpeek(f'Opening {x} and searching...')
            for q in query_list:
                if check_code(site + q + search[0:-1]):
                    webbrowser.open(site + q + search[0:-1])


        else:
            printWithSpeek(f'Opening {x}')
            webbrowser.open(site)