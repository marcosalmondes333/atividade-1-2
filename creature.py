from pydantic import BaseModel

dict_thing = {
    "name": "yeti",
    "country": "CN",
    "area": "Himalayas",
    "description": "Hirsute Himalayan",
    "aka": "Abominable Snowman",
}

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

creature1 = Creature(**dict_thing)

creature2 = Creature(
    name="dragon",
    country="JP",
    area="Mountains",
    description="Fire-breathing creature",
    aka="Ryuu"
)

creature3 = Creature(
    name="bigfoot",
    country="US",
    area="Forests",
    description="Large hairy humanoid",
    aka="Sasquatch"
)

print(creature1.name)
print(creature2.name)
print(creature3.name)
