import re

class Search:

    def __init__(self, searchterms, regexterms):
        self.searchterms = searchterms
        self.regexterms = dict()
        for t in regexterms:
            self.regexterms[t] = re.compile(t)

    def add_searchterm(self, term):
        self.searchterms.append(term)

#    def del_searchterm(self, term):
        #if self.searchterms.contains(term):
        #@TODO

    def add_regexterm(self, term):
        self.regexterms[term] = re.compile(t)

#    def del_regexterm(self, term):
        #@TODO

    def clear_searchterms(self):
        self.searchterms = list()

    def clear_regexterms(self):
        self.regexterms = dict()

    def apply_terms(self, data):
        search_hits = self.apply_searchterms(data)
        regex_hits = self.apply_regexterms(data)
        return search_hits,regex_hits

    def apply_searchterms(self, data):
        hits = list()
        for t in searchterms:
            if t in data:
                hits.append(t)
        return hits

    def apply_regexterms(self, data):
        hits = list()
        for t,rec in regexterms.iteritems():
            if rec.match(data):
                hits.append(t)
        return hits
