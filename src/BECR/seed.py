"""
Seed object to represent seed examples for bootstrapping
"""
import numpy as np
import pickle

class Seed:

    glove_embeddings = None

    def __init__(self, emo, cause, tweet, glove_size):
        """
        Initialize by setting the emotion and cause values
        :param emo:
        :param cause:
        :param tweet:
        """
        self.emo = emo
        self.cause = cause
        self.emo_embedding = None
        self.cause_embedding = None
        self.tweet = tweet
        self.bef = []
        self.btwn = []
        self.aft = []
        self.cosine = None
        self.cycle = None
        self.glove_size = glove_size
        self.bad = None

    @staticmethod
    def load_glove_embeddings(glove_size):
        glove_file = '../../lib/glove/glove' + (str(glove_size)) + '.pkl'
        Seed.glove_embeddings = pickle.load(open(glove_file, 'rb'))

    def calc_glove_score(self, context):
        """
        Calculate context score with GLoVe embedding
        :param context: list of text objects
        :return: vector
        """
        context_embedding = np.full(self.glove_size, 1.e-28)
        for word in context:
            if word in Seed.glove_embeddings.keys():
                word_vec = np.array(Seed.glove_embeddings[word])
                context_embedding += word_vec

        return context_embedding

    def get_context_before(self, reln1):
        """
        Get the context before the given relation - emotion or cause
        :param reln1: the given relation, a Word object
        :return: void
        """
        before = self.tweet.tokens[0:reln1[0].idx-1]
        if before:
            self.bef = self.calc_glove_score(before)
        else:
            self.bef = np.full(self.glove_size, 1.e-28)

    def get_context_btwn(self, reln1, reln2):
        """
        Get the context between the two relations - emotion and cause
        :param reln1: the first relation, a Word object
        :param reln2: the second relation,
        :return: void
        """
        between = self.tweet.tokens[reln1[-1].idx:reln2[0].idx-1]
        if between:
            self.btwn = self.calc_glove_score(between)
        else:
            self.btwn = np.full(self.glove_size, 1.e-28)

    def get_context_after(self, reln2):
        """
        Get the context after the given relation -- emotion or cause
        :param reln2: the given relation, a Word object
        :return: void
        """
        after = self.tweet.tokens[reln2[-1].idx:-1]
        if after:
            self.aft = self.calc_glove_score(after)
        else:
            self.aft = np.full(self.glove_size, 1.e-28)