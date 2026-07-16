class TextChunker:

    def __init__(self, chunk_size=400):
        self.chunk_size = chunk_size

    def split(self, text):

        words = text.split()

        chunks = []

        for i in range(0, len(words), self.chunk_size):

            chunk = " ".join(words[i:i+self.chunk_size])

            if chunk.strip():
                chunks.append(chunk)

        return chunks