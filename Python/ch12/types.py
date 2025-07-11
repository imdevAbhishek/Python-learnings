from typing import List, Tuple, Dict, Union

age: int=34
def greeting(name: str) -> str: 
   return f"Hello, {name}!" 
print(greeting("Abhi"))



numbers: List[int] = [1, 2, 3, 4, 5] 
person: Tuple[str, int] = ("Alice", 30)  
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}  
identifier: Union[int, str] = "ID123" 
