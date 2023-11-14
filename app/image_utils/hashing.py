from datasketch import MinHashLSH, MinHash


# 해싱 처리
class LSHHash:
    def __init__(self, num_perm=256):
        self.num_perm = num_perm
        self.lsh = MinHashLSH(num_perm=num_perm)
        
    def hash_tensor(self, tensor):

        minhash = MinHash(num_perm=self.num_perm)
        dense_vector = [0.0] * self.num_perm
        
        for value in tensor:
            minhash.update(str(value).encode('utf-8'))
        
        for i, value in enumerate(minhash.hashvalues):
            dense_vector[i] = float(value)
        return dense_vector