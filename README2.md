<table>
    <tr>
        <td>
            <a href="README.md">⬅️ Back</a>
        </td>
    </tr>
</table>

# 1.2 Configuration of the Dataset's file

## Regarding the dataset configuration: ⤵️
It **must be in JSON format** , inside it will have as many keys as there are tables that dataset has.

```json
{
    "Customers": {
        "MetaData": [
            {
                "AmountOfRegisters": 15570
            }
        ],
        "Data": [
            {
                "mode": "NULLABLE",
                "name": "customer_id",
                "type": "STRING",
                "ispk": "true",
                "format":"??###",
                "letters":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            },
            {
                "mode": "NULLABLE",
                "name": "customer_code",
                "type": "STRING",
                "faketype": "bothify",
                "format":"??###",
                "letters":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            }
        ]
    }
}

```

Each table key will have inside two keys: _MetaData_ and _Data_.

Inside _MetaData_ there will be a list and inside it, a dictionary with a unique key called **AmountOfRegisters** in which the number of records that will be generated in that table will be valued.
<ul><li>Each table will have its own quantity.</li></ul>

```json
"MetaData": [
                {
                    "AmountOfRegisters": 285
                }
            ]
```
Inside **Data** there will be a list of dictionaries, in which *_each of these dictionaries will have the characteristics of each column of said table_*

```json
"Data": [
            {
                "mode": "NULLABLE",
                "name": "customer_id",
                "type": "STRING",
                "ispk": "true",
                "format":"??###",
                "letters":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            }
        ]
```

Regarding the keys within these dictionaries, we are going to focus the explanation on some of them since they are necessary for the correct functioning of the script.

### ⚠️ Attention to the following cases: ⤵️

## 1 - If is Primary Key ⤵️
If the column is Primary Key (PK from now on, to simplify terms.) **MUST** take the key _"ispk"_ in true, as indicated in the image.

```json
    "ispk": "true"
```
## 2 - If is Foreign Key ⤵️
If the column is Foreign Key (FK from now on, to simplify the terms) **It must** have the key _"isfk"_ in _"true"_ **and also** it must contain two additional keys indicating the table to the one it refers to as well as the column of the table it refers to.
These fields will be:

**"sourceTable"**: The field that refers to the table from which the pk / fk is extracted.
**"sourceField"**: The column of the aforementioned table from which this value is extracted.

```json
{
    "mode": "NULLABLE",
    "name": "customer_id",
    "type": "STRING",
    "isfk": "true",
    "sourceTable": "Customers",
    "sourceField": "customer_id"
}
```
# ⚠️ **ADVICE** ⚠️ ⤵️
The column **must not be PK and FK at the same time**, this would generate an error so the script will fail. It is prudent to determine whether the column is PK or FK or neither.

## 3 - If the column is a simple data field (No PK & No FK) ⤵️
If the column is simple data, it will not have the keys mentioned in the previous points, instead it will have a key called **_"faketype"_** where as a value, it will be indicated what type of method of the Faker module should be use to generate the data of the column in question. Some of these Faker methods carry parameters and others do not, let's see some examples to better graph the explanation.

#### Method without parameters. ⤵️

```json
{
    "mode": "NULLABLE",
    "name": "customer_city",
    "type": "STRING",
    "faketype": "city",
    "parameters":[]
}
```
In this example, the **"faketype"** is "country", this means that the script will use the **country method** from the Faker library which does not receive parameters to generate that data for the column named _"customer_city"_. The field 'parameters' with square brackets will be mandatory to always be present.

#### Method with parameters. ⤵️

```json
{
    "mode": "NULLABLE",
    "name": "customer_age",
    "type": "NUMERIC",
    "faketype":"pyint",
    "parameters":[
        0,
        100,
        1
    ]
}
```
In this example, the **"faketype"** is "word" and that method needs parameters to work correctly, so the dictionary **Needs** a key called **"parameters"** in which its value is a list of 1 to 3 parameters, as needed.

In the particular case of the method _"word"_, it receives as its only parameter a list of words (They can also be phrases, declared as a string, but _always within a list_.), That is why in the image there is a list within another list.
<table>
    <tr>
        <td>
            <a href="https://faker.readthedocs.io/en/master/providers/faker.providers.lorem.html#faker.providers.lorem.Provider.word" target="_blank">➡️ Go to Word documentation</a>
        </td>
    </tr>
</table>


```json
"faketype": "word",
"parameters":[
    [
        "LOSE",
        "WIN", 
        "TIE"
    ]
]
```
That list counts as a single parameter (the list object) of the key _"parameters"_.

### ⚠️ Important Note ⚠️ ⤵️
In the case of the bothify method, although it receives parameters, the correct way to use it in this script is by declaring two keys that we will detail below:

**"format"**: this key will detail the format of the data generated by bothify, using a '?' for each letter that we want it to generate and a '#' for each number that we want it to generate, allowing the possibility of using the amount and variety that we want.
**"letters"**: In this key, in the form of a string, you must put all the letters which the script can use randomly to generate the data.

### Example ⤵️

```json
{
    "mode": "NULLABLE",
    "name": "internal_code",
    "type": "STRING",
    "faketype": "bothify",
    "format":"??###",
    "letters":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
```

In this example, **"format"** has the value **"?? ###"**, which corresponds to two letters (_"??"_) and three numbers (_"###"_) and **"letters"** have as value a string of uppercase letters. This means that bothify will generate a data of two capital letters followed by three numbers, i.e. **"FF007"**.

They can play with the variety and quantity, being able to insert letters and numbers of the key **"format"**, as well as adding more characters to the string of the key **"letters"**
<table>
    <tr>
        <td>
            <a href="https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.bothify" target="_blank">➡️ Go to Bothify documentation</a>
        </td>
    </tr>
</table>


### ✅ Recommended methods to use
#### 1 - Without parameters: ⤵️

[_city_](https://faker.readthedocs.io/en/master/providers/faker.providers.address.html#faker.providers.address.Provider.city): It will generate data with the name of a city.

[_state_](): It will generate data with the name of a state or province.

[_country_](https://faker.readthedocs.io/en/master/providers/faker.providers.address.html#faker.providers.address.Provider.country): It will generate data with the name of a country.

[_address_](https://faker.readthedocs.io/en/master/providers/faker.providers.address.html#faker.providers.address.Provider.address): It will generate a data with an address.

[_random\_uppercase\_letter_](https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_uppercase_letter): It will generate data with a capital letter.

[_name_](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html#faker.providers.person.Provider.name): It will generate a name data.

[_first\_name_](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html#faker.providers.person.Provider.first_name): It will generate a name data.

[_first\_name\_female_](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html#faker.providers.person.Provider.first_name_female): It will generate a female name data.

[_first\_name\_male_](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html#faker.providers.person.Provider.first_name_male): It will generate a male name data.

[_first\_name\_nonbinary_](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html#faker.providers.person.Provider.first_name_nonbinary): It will generate a non-binary name data.

[_language\_name_](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html#faker.providers.person.Provider.language_name): It will generate a language data.

[_pybool_](https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pybool): It will generate a boolean data (True or False).
#### 2 - With parameters: ⤵️

[_pyfloat_](https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pyfloat): It will generate a decimal value, in the value of your key _"parameters"_, you must put 3 parameters, i.e. [4,2, true], the first field is for numbers on the left side of the comma (integer part), the second field is for numbers on the right side of the comma (decimal part) and the third field is to indicate if It is a positive (true) or negative (false) number.

[_pyint_](https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pyint): It will generate an integer value, in the value of your key _"parameters"_, you must put 3 parameters, i.e. [0,1000,1]. The first field is to indicate the minimum number, the second field is for the maximum number and the third field is to indicate the jumps (1 in 1, 2 in 2, etc).

For more information, you can visit the official website of [Faker](https://faker.readthedocs.io/en/master/providers.html)

<table>
    <tr>
        <td>
            <a href="README.md">⬅️ Back</a>
        </td>
        <td>
            <a href="https://faker.readthedocs.io/en/master/providers.html" target="_blank">➡️ Go to Faker WebPage</a>
        </td>
    </tr>
</table>
