from __future__ import annotations

from vakyartha.base import BaseComponent, Document,DocumentWithEmbedding


class BaseEmbeddings(BaseComponent):

    def run(
            self,
            text:str | list[str] | Document | list[Document],*args,**kwargs
    ) -> list[DocumentWithEmbedding]:
        
        return self.invoke(text,*args,**kwargs)
    

    def invoke(
            self,
            text:str | list[str] | Document | list[Document],*args,**kwargs
    ) -> list[DocumentWithEmbedding]:
        """Main method to transform text into embeddings"""
        raise NotImplementedError("Embeddings not implemented"
    )

    async def invoke(
            self,
            text:str | list[str] | Document | list[Document],*args,**kwargs
    ) -> list[DocumentWithEmbedding]:
        """Main method to transform text into embeddings"""
        raise NotImplementedError("Embeddings not implemented"
    )

    def prepare_input(
            self,
            text : str | list[str] | Document | list[Document],
            *args,**kwargs
    ) -> list[Document]:
        
        if isinstance(text,(str,Document)):
            return [Document(content=text)]
        
        elif isinstance(text,list):
             return [Document(content=_) for _ in text]
        
        return text

