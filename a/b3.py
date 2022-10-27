from __future__ import annotations
from typing import Any,Type

class node:
    def __init__(i,key:Any,value:Any,left:node=None,right:node=None):
        i.key=key
        i.value=value
        i.left=left
        i.right=right
class BinarySearchTree:
    def __init__(i):
        i.root=None