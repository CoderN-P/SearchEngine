from typing import Dict
import numpy as np


class VectorComparison:
    def __init__(self, concordance1: Dict[str, int], concordance2: Dict[str, int]):
        self.doc1 = concordance1
        self.doc2 = concordance2

    def similarity(self):
        """
        Returns the cosine similarity between two documents
        :return:
        """

        vector1 = np.array(list(self.doc1.values()))
        vector2 = np.empty(vector1.size)

        for index, key in enumerate(self.doc1):
            if key in self.doc2:
                vector2[index] = self.doc2[key]

        magnitudes = np.sqrt(vector2.dot(vector2)) * np.sqrt(vector1.dot(vector1))

        if magnitudes == 0:
            return 0

        return np.dot(vector1, vector2) / magnitudes
