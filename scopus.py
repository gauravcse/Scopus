#   CREATED BY GAURAV MITRA
#   NOTE FROM GAURAV : THIS PIECE OF CODE IS NOT TESTED BECAUSE SCOPUS IS NOT OPEN SOURCE AND TO ACCESS THE DATABASE
#                      LICENSE IS REQUIRED. DUE TO ABSENCE OF LICENCE I COULD NOT TEST THE CODE AS I DO NOT HAVE AN
#                      API KEY. BUT THE CODE IS EXPECTED TO RUN AS PARTS OF IT ARE INDIVIDUALLY CHECKED AND HAVE
#                      PRODUCED ACCURATE RESULTS.

''' THIS IS A CODE THAT USES THE SCOPUS API TO PARSE AND RETURN PERSONAL DATA
    FROM SCOPUS DATBASE '''

#   WARNING : SCOPUS DOES NOT ALLOW US TO SCRAPE DATA WITHOUT THE API
#   THE API HAS TO BE INSTALLED USE THIS CODE

#   MAKE SURE YOU HAVE AN API KEY


try :
    import requests
    import json
    import textwrap
except ImportError:
    print '{}'.format("CHECK YOUR PYTHON DISTRIBUTION. SOME PACKAGES ARE NOT INSTALLED\n\n")

''' HELPER FUNCTION TO RETURN SCOPUS INFO '''

def get_scopus_info(SCOPUS_ID,MY_API_KEY):
    url = ("http://api.elsevier.com/content/abstract/scopus_id/"+ SCOPUS_ID + "?field=authors,title,publicationName,volume,issueIdentifier," + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
    resp = requests.get(url,headers={'Accept':'application/json','X-ELS-APIKey': MY_API_KEY})
    return json.loads(resp.text.encode('utf-8'))

''' ITERATES THROUGH THE SCOPUS IDS AND WRITES THE REFERNCE INFO INTO THE FILE '''

def print_scopus_info(scopus_ids,MY_API_KEY) :
    f = open("database.txt",'w')
    i = 0
    for sid in scopus_ids:
        try:
            results = get_scopus_info(sid[0],MY_API_KEY)
            if results['abstracts-retrieval-response']['coredata']['prism:aggregationType'] == 'Journal':
                i += 1
                fstring = '{authors}, {title}, {journal}, {volume}, {articlenum}, ({date}). <a href="http://dx.doi.org/{doi}">{doi}</a> (cited {cites} times)\n\n'
                s = fstring.format(authors=', '.join([au['ce:indexed-name'].encode('utf-8') for au in results['abstracts-retrieval-response']['authors']['author']]),title=results['abstracts-retrieval-response']['coredata']['dc:title'].encode('utf-8'),journal=results['abstracts-retrieval-response']['coredata']['prism:publicationName'].encode('utf-8'),volume=results['abstracts-retrieval-response']['coredata'].get('prism:volume', 'None').encode('utf-8'),articlenum=str((results['abstracts-retrieval-response']['coredata'].get('prism:pageRange') or results['abstracts-retrieval-response']['coredata'].get('article-number'))).encode('utf-8'),date=results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8'),doi='doi:' + results['abstracts-retrieval-response']['coredata']['prism:doi'].encode('utf-8'),cites=int(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8')))
            data =  '{0:3d}. {1}<br>'.format(i, s)
            f.write(data)
        except:
            print '{0:3d}. {1}'.format(i, sid)
    f.close()

''' SCOPUS IDS OF ALL THE DOCUMENTS IN THE DATABASE OF THE USER '''    

def get_scopus_ids(MY_API_KEY) :
    resp = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID(7004212771)&field=dc:identifier&count=100",headers={'Accept':'application/json','X-ELS-APIKey': MY_API_KEY})
    results = resp.json()
    scopus_ids = [[str(r['dc:identifier'])] for r in results['search-results']["entry"]]
    print_scopus_info(scopus_ids,MY_API_KEY)

if __name__ == "__main__" :
    print '{0}\n\t1. {1}\n\t2. {2}'.format("TO PROCEED WITH THIS PROGRAM  : ","YOU NEED TO BE A REGISTERED USER OF SCOPUS ","YOUR UNIVERSITY NEEDS TO HAVE THE RIGHT TO ACCESS SCOPUS")
    print '\n\n\t{}\n\t\t{}\n\t\t{}'.format("DO YOU WANT TO CONTINUE ? ","PRESS 1 TO CONTINUE","ANY OTHER NUMBER TO EXIT ")
    choice = int(input())
    if (choice == 1) :
        MY_API_KEY = raw_input("\tENTER YOUR API KEY : ")
        get_scopus_ids(MY_API_KEY)
    else :
        print '{}'.format("x-------x-------x-------x-------x-------x-------x-------x-------x-------x------x")
