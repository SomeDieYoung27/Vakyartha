from __future__ import annotations

from abc import abstractmethod

from vakyartha.base import BaseComponent, Document

class BaseRanking(BaseComponent):
    @abstractmethod
    def run(self,documents : list[Document],query : str) -> list[Document]:
         """Main method to transform list of documents
        (re-ranking, filtering, etc)"""
         ...