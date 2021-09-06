class URL_Shotener:
    Url2Id = {}
    id = 1000000
    def shorten_url(self, original_url):
        if original_url in self.Url2Id:
            id = self.Url2Id[original_url]
            short_Url = self.encode(id)
        else:
            self.Url2Id[original_url] = self.id
            short_Url = self.encode(self.id)
            self.id += 1
        return "shortUrl.com/"+ str(short_Url)


    def encode(self,id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        
        return "".join(ret[::-1])

shortener = URL_Shotener()
print(shortener.shorten_url("gooooooooooogle.com"))

print(shortener.shorten_url("gooooooooooogle.com"))
print(shortener.shorten_url("yahoooooooo.com"))