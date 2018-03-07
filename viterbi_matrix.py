# calculate the Viterbi Matrix for the sentence: "learning changes throughly" 

from pandas import DataFrame

# This function creates viterbi decoding matrix given an input sentence
def create_matrix(input_sentence, emission_probability, transition_probability):

    # split input sentence into tokens
    tokens = input_sentence.split()

    # Insert Start and Stop 
    tokens.insert(0, "<start>")
    tokens.append("<stop>")

    # Create a list of all part of speech tags given in question
    pos_tags = list(transition_probability.keys())

    # Initialize viterbi matrix with (0,0) except position 0,0 as (1,0) as we always start from start point
    viterbi_matrix = [[(0, 0) for x in range(len(tokens))] for y in range(len(pos_tags))]
    viterbi_matrix[0][0] = 1, 0

    # calculates the probabilities for input tokens (learning, changes, thoroughly) tagged as 
    # different states(noun, verb, adverb) for each cell in the matrix
    for index in range(1, len(tokens)):
        token = tokens[index]
        prev_col_index = index - 1
        for index_from, pos_from in enumerate(pos_tags):
            prev_probability, prev_pointer = viterbi_matrix[index_from][prev_col_index]
            for index_to, pos_to in enumerate(pos_tags):
                word_emission_probability = emission_probability.get(token).get(pos_to, 0)
                word_transition_probability = transition_probability.get(pos_from).get(pos_to, 0)
                new_pointer = (index_from, prev_col_index)
                new_probability = prev_probability * word_emission_probability * word_transition_probability
                curr_probability, curr_pointer = viterbi_matrix[index_to][index]
                if curr_probability < new_probability:
                    viterbi_matrix[index_to][index] = new_probability, new_pointer

    viterbi_result = DataFrame(viterbi_matrix, index=pos_tags, columns=tokens)
    return viterbi_result


def backtrace_viterbi_result(viterbi_result):
    """Return the POS tagger for the given sentence from the matrix"""
    output_prediction = ["<stop>"]
    probability, pointer = viterbi_result["<stop>"]["<stop>"]
    while pointer:
        pos_tag = viterbi_result.index[pointer[0]]
        output_prediction.insert(0, pos_tag)
        probability, pointer = viterbi_result.iloc[pointer[0]].iloc[pointer[1]]
    return output_prediction


def main():

        # emission_probability contains probability values of each word for being in different states
    emission_probability = {
        "learning": {
            "verb": 0.003,
            "noun": 0.001
        },
        "throughly": {
            "adverb": 0.002
        },
        "changes": {
            "verb": 0.004,
            "noun": 0.003
        },
        "<start>": {
            "<start>": 1
        },
        "<stop>": {
            "<stop>": 1
        }
    }

    # transition_probability contains values from hidden markov model chain map as given in our diagram provided to us
    transition_probability = {
        "<start>": {
            "noun": 0.2,
            "verb": 0.3,
        },
        "noun": {
            "noun": 0.1,
            "verb": 0.3,
            "adverb": 0.1,
        },
        "verb": {
            "noun": 0.4,
            "verb": 0.1,
            "adverb": 0.4,
        },
        "adverb": {
            "<stop>": 0.1
        },
        "<stop>": {
        }
    }

    input_sentence = "learning changes throughly"

    viterbi_result = create_matrix(input_sentence, emission_probability, transition_probability)

    print("Input Sentence:", input_sentence)
    print("Viterbi Matrix is as follows:\n", viterbi_result)
    print("Output of the tagger is:", backtrace_viterbi_result(viterbi_result))
    print()


if __name__ == '__main__':
    main()