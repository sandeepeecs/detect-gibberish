from keyboard import Keyboard
import math
class Gibirish:

    def __init__(self) -> None:
        self.keyboard = Keyboard().get_keyboard()

    def detect(self,word:str) -> list:
        return self.get_typing_distance(word)

    def get_distance_for_key_pair(self,keystring):
        first_char = keystring[0]
        second_char = keystring[1]
        x_distance = (self.keyboard[first_char]['x'] - self.keyboard[second_char]['x']) ** 2
        y_distance = (self.keyboard[first_char]['y'] - self.keyboard[second_char]['y']) ** 2
        euclid_distance = math.sqrt(x_distance + y_distance)
        return euclid_distance
    
    def get_stats_for_typing_pairs(self,pair_list):
        mean = sum(pair_list) / len(pair_list)
        var = sum((l-mean)**2 for l in pair_list) / len(pair_list)
        st_dev = math.sqrt(var)
        return sum(pair_list), mean, st_dev 

    def get_typing_distance(self,word):
        total_distance = 0
        ngram_char = ["".join(j) for j in zip(*[word[i:] for i in range(2)])]
        ngram_distance_list = []
        for bigram in ngram_char:
            bigram = [ch for ch in bigram]
            pair_distance = self.get_distance_for_key_pair(bigram)
            ngram_distance_list.append(pair_distance)
        pair_stats,mean,std_dev = self.get_stats_for_typing_pairs(ngram_distance_list)
        return pair_stats, mean,std_dev
    