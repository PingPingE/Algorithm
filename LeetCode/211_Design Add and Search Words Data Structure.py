'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
'''
#sol: using Trie, deque(312 ms	29 MB)
class Node:
    def __init__(self,data,word=None):
        self.data = data
        self.next= {}#key: alphabet, value: Node
        self.word = word
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = Node(None) #root

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.words
        for w in word:
            if w in current.next:
                current = current.next[w]
            else:
                current.next[w] = Node(w)
                current = current.next[w]
        current.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        que = deque()
        que.append((self.words, 0)) #current's node, word's index
        while que:
            # print("que:",que,word)
            current, ind = que.popleft()
            if ind == len(word):
                # print(current.word, word)
                if current.word:
                    return True
                continue
            
            w = word[ind]
            if w == '.':
                # print(current.next)
                for v in current.next.values():
                    que.append((v,ind+1))
            elif w in current.next:
                que.append((current.next[w], ind+1))
        return False
    