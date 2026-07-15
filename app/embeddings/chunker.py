from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:

    @staticmethod

    def chunk(text: str):

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,

            chunk_overlap=100

        )

        return splitter.split_text(text)