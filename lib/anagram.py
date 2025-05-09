class Anagram:
    def __init__(self,word):
        self.word=word

    def match(self,list):
        sorted_word=sorted(self.word)
        results=[]
        for _word in list:
            if sorted(_word.lower())==sorted_word and _word !=self.word:
                results.append(_word)

        return results

