## Homework Submission # 2 
### TCSS590: Natural Language Processing 
### Winter 2018 
#### Chhaya Choudhary

# POS Tagging: Viterbi Decoding
Viterbi Decoding Matrix

# Description
For the above bigram HMM POS tagger, calculate the Viterbi Matrix for the sentence: "learning changes throughly" using the following emission probabilities:

P(learning|V) = 0.003

P(changes|V) = 0.004

P(throughly|Adv) = 0.002

P(learning|N) = 0.001

P(changes|N) = 0.003

Transition probabilities are as follows:
P(Noun|Start) = 0.2
P(Verb|Start) = 0.3
P(Noun|Noun) = 0.1
P(Verb|Verb) = 0.1
P(Adverb|Noun) = 0.1
P(Verb|Noun) = 0.3
P(Noun|Verb) = 0.4
P(Adverb|Verb) = 0.4
P(End|Adverb) = 0.1

Calculate the values for the sentence "learning changes throughly" along with the Output of the tagger.

Program can be run from command line as: 

__python <viterbi_matrix.py> 
  
where viterbi_matrix.py is the name of the python program. The output represents viterbi decoding matrix along with the output of the tagger.
