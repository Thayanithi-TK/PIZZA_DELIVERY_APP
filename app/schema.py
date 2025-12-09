from pydantic import BaseModel

class UserCreate(BaseModel):

    name:str
    email:str
    password:str

class UserResponse(BaseModel):

    id:int
    name:str
    email:str

    class Config:
        from_attributes=True



class PizzaCreate(BaseModel):

    name:str
    price:float
    description:str


class PizzaResponse(BaseModel)
    
    id:int
    name:str
    price:float
    description:str

    class Config:
        from_attributes=True


class OrderCreate(BaseModel):

    user_id:int
    pizza_id:int

class OrderResponse(BaseModel):
    id:int
    user_id:int
    pizza_id:int
    status:str

    class Config:
        from_attributes =True
        
                

