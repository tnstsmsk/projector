def jccard_similarity(set1, set2):
    method_inters = set1.intersection(set2)
    method_union = set1.union(set2)

    jaccard_similarity = len(method_inters) / len(method_union)

    return round(jaccard_similarity, 2)


set1 = {'a', 't', 4, 8, 'm', 'd'}
set2 = {'c', 4, 'm', 7, 2, 9, 'k', 'di', 91, 'mkl', 'd'}

print(jccard_similarity(set1, set2))
