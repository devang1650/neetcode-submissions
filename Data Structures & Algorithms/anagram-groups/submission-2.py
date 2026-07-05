class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output=[]
        # for i in range(len(strs)):
        #     for j in range(i+1,len(strs)):
        #         if sorted(strs[i])==sorted(strs[j]):
        #             output.append([strs[i],strs[j]])
        #         if sorted(strs[i]) not in output:
        #             output.append([strs[i]])
        # return output
        anagram_map = defaultdict(list)
    
        for word in strs:
            # Sorting the word creates a universal key for all its anagrams
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())
                