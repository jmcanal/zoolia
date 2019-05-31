"""
Seed object to represent seed examples for bootstrapping
"""
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import pickle

class Seed:

    # Loading glove vectors
    GLOVE_SIZE = 25
    glove_file = '../../lib/glove/glove' + str(GLOVE_SIZE) + '.pkl'
    glove_embeddings = pickle.load(open(glove_file, 'rb'))

    def __init__(self, emo, cause, tweet):
        """
        Initialize by setting the emotion and cause values
        :param emo:
        :param cause:
        :param tweet:
        """
        self.emo = emo
        self.cause = cause
        self.tweet = tweet
        self.bef = []
        self.btwn = []
        self.aft = []
        self.cosine = None
        self.cycle = None

    def calc_glove_score(self, context):
        """
        Calculate context score with GLoVe embedding
        :param context: list of Word objects
        :return: vector
        """
        context_embedding = np.ones(self.GLOVE_SIZE)
        for word in context:    # todo: fix the tokenization; glove has: 's, 'm; twokenizer has i'm, it's
            if word in self.glove_embeddings.keys():
                word_vec = np.array(self.glove_embeddings[word])
                context_embedding += word_vec

        return context_embedding

    def get_context_before(self, reln1):
        """
        Get the context before the given relation
        :param reln1: the given relation
        :return: void
        """
        before = self.tweet.words[0:reln1[0].idx-1]
        if before:
            self.bef = self.calc_glove_score(before)
        else:
            self.bef = np.ones(self.GLOVE_SIZE)

    def get_context_btwn(self, reln1, reln2):
        """
        Get the context between the two relations
        :param reln1: the first relation
        :param reln2: the second relation
        :return: void
        """
        between = self.tweet.words[reln1[-1].idx:reln2[0].idx-1]
        if between:
            self.btwn = self.calc_glove_score(between)
        else:
            self.btwn = np.ones(self.GLOVE_SIZE)

    def get_context_after(self, reln2):
        """
        Get the context after the given relation
        :param reln2: the given relation
        :return: void
        """
        after = self.tweet.words[reln2[-1].idx:-1]
        if after:
            self.aft = self.calc_glove_score(after)
        else:
            self.aft = np.ones(self.GLOVE_SIZE)