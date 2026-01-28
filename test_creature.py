from pydantic import BaseModel, Field, ValidationError

class Creature(BaseModel):
    name: str = Field(min_length=3)  # nome deve ter pelo menos 3 caracteres
    country: str
    area: str
    description: str
    aka: str

# ERRO DE TIPO
try:
    creature_error_type = Creature(
        name="orc",
        country="US",
        area="Forest",
        description=["should", "be", "string"],  # ERRADO: deveria ser str
        aka="Monster"
    )
except ValidationError as e:
    print("ERRO DE TIPO:")
    print(e)

# ERRO DE VALOR
try:
    creature_error_value = Creature(
        name="ab",  # ERRADO: min_length=3
        country="US",
        area="Desert",
        description="Too short name",
        aka="Unknown"
    )
except ValidationError as e:
    print("\nERRO DE VALOR:")
    print(e)
