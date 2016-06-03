#   CREATED BY GAURAV MITRA


''' REPRESENTS DOCUMENT AND ITS REFERENCES AS A GRAPH IN THE FORM OF AN ADJACENCY LIST '''
''' IT IS NON RECURSIVE AND ONLY FINDS THE EDGES WITH RESPECT TO ONE NODE (STAR GRAPH) '''
''' THIS USES THE CONCEPT OF INVERSE INDEX OR REVERSE WEB LINK '''
''' MAKE SURE THAT YOUR DATA FILE IS READY '''

''' THIS FUNCTION GENERATES THE GRAPH FROM A LIST OF NODES ALREADY GIVEN '''

def graph_generate(list_of_doi,main_node) :
    f = open("graph.txt",'a')
    data = ""
    for item in list_of_doi :
        data = data + item + "->"
    data = main_node + " -> " + data
    f.write(data+"\n")

''' FEEDS THE NODE TO THE graph_generate FUNCTION '''

def get_doi(filename,main_node) :
    f = open(filename,'r').read()
    list_of_doi = list()
    line = f.split("\n")
    for element in line :
        list_of_doi.append(element.split("\t")[0])
    graph_generate(list_of_doi,main_node)
    
if __name__ == "__main__" :
    print '{0}'.format("\t WELCOME TO THE GRAPH GENERATION PROCESS : ")
    print '{0}'.format("\t\tNOTE : THE GRAPH WILL BE GENERATED AND REPRESENTED IN THE FORM OF ADJACENCY LIST")
    filename = raw_input("\t ENTER THE FILENAME CONTAINING THE CORRECTLY PARSED CITATION DATA : " )
    main_node = raw_input("\t ENTER THE MAIN CITATION ARTICLE DOI : ")
    get_doi(filename,main_node)

