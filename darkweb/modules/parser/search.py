import re

class search:
    searchterms = list()
    regexterms = dict()

    #@staticmethod
    def add_searchterm(self, term):
        self.searchterms.append(term)

#    def del_searchterm( term):
        #if searchterms.contains(term):
        #@TODO

    #@staticmethod
    def add_regexterm(self, term):
        self.regexterms[term] = re.compile(term)

#    def del_regexterm( term):
        #@TODO

    #@staticmethod
    def clear_searchterms():
        self.searchterms = list()

    #@staticmethod
    def clear_regexterms():
        self.regexterms = dict()

    #@staticmethod
    def apply_terms(self, data):
        print("Searching data for: " + str(self.searchterms))
        print("Applying Regex to data for: " + str(self.regexterms))
        search_hits = self.apply_searchterms(data)
        regex_hits = self.apply_regexterms(data)
        return search_hits,regex_hits

    #@staticmethod
    def apply_searchterms(self, data):
        hits = list()
        try:
            data = unicode(data, errors='ignore')
        except:
            pass
        for t in self.searchterms:
            if t in data:
                hits.append(t)
        return hits

    #@staticmethod
    def apply_regexterms(self, data):
        hits = list()
        try:
            data = unicode(data, errors='ignore')
        except:
            pass
        for t,rec in self.regexterms.iteritems():
            if rec.match(data):
                hits.append(t)
        return hits


