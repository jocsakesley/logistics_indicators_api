import pandas as pd
from pathlib import Path
from faker import Faker


df = pd.read_csv(Path(__file__).parent.parent / "bd_desafio.csv", sep=";")

print(df.shape)
df = df.drop_duplicates(subset='id_cliente')
print(df.shape)

fake = Faker()

with open("customers_data.csv", "w+") as file:
    for id_cliente in df['id_cliente']:
        name = fake.name()
        email = fake.free_email()
        phone = fake.numerify("###########")
        file.write(f"{id_cliente};{name};{str(id_cliente) + email};{phone}\n")