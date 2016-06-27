def create_RestLinks():
    ### iterate through all pages of new yorker tables-for-two history                                                                            
    step = 1
    RestLinks = []
    while step < 80:
        page = 'http://www.newyorker.com/magazine/tables-for-two/page/' + str(step)
        #print(page)                                                                                                              
        r = urllib.request.urlopen(page).read()
        #r = open('sample_T4T_mainpage.html', 'r')  #can use this sample html page for debugging                                                                                            
        soup = BeautifulSoup(r, "lxml")
    
        #info = soup.findAll('span', {'itemprop':'headline'}) #this works to find the name of the restaurants
    
        #return a list of lists of restaurants from each page
        info = soup.findAll('a', {'itemprop':'name'})
    
        #extract only the link itself
        for link in info:
            #print(link.get('href'))
            # add links to RestLinks list:                                                                               
            RestLinks.append(link.get('href'))

        step +=1
    return(RestLinks)