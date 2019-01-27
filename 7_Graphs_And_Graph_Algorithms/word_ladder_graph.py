from Graph_ADT import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')

    # Create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            # if the word is hello and i is 0
            # word is _ello
            # word is h_llo
            # word is he_lo
            # word is hel_o
            # word is hell_
            bucket = word[:i] + '_' + word[i+1:]

            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # Add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g
