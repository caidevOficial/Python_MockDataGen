<table>
  <tr>
  <td><img align="center" alt="Caidev" src="https://github.com/caidevOficial/Resume/blob/main/media/pm/pageImgs/banner.gif?raw=true" height="100px" /></td>
  <td><img align="center" alt="Pyhton" src="https://github.com/caidevOficial/Logos/blob/master/Lenguajes/py_logo1_1.png?raw=true" height="100px" /></td>
  </tr>
</table></br>

---

<p align="left"> <img src="https://komarev.com/ghpvc/?username=caidevoficial&label=Profile%20views&color=0e75b6&style=flat" alt="caidevoficial" /> </p>

<p align="left"> <a href="https://github.com/CaidevOficial"><img src="https://github-profile-trophy.vercel.app/?username=caidevoficial&theme=nord&column=7" alt="caidevoficial" /></a> </p>

---
<details>
  <summary>:zap: GitHub Stats</summary>
    <img align="center" src="https://github-readme-stats-caidevposeidon.vercel.app/api?username=caidevOficial&show_icons=true&theme=chartreuse-dark&count_private=true&show_owner=true&include_all_commits=true" /><br><br>
</details>

<details>
    <summary>:zap: Most Used Languages</summary>
    <img align="center" src="https://github-readme-stats-caidevposeidon.vercel.app/api/top-langs/?username=caidevOficial&layout=compact&theme=chartreuse-dark&langs_count=10&exclude_repo=Java_Lineage2_aCis_From_345&hide=html,css"/><br>
</details>

---

```python
def UpgradeFunction():
    message = "Upgrading my skills [Py Version!]"
    return message
```

# MockData Generator v3.1.0 ⤵️

_The MockData Generator is a tool that allows, through some configurations, to create random records in a document with a '.csv' format or '.sql' for tables, based on their column structure and thus later to be able to load them into bigdata._

## 🚀 0.0 Starting ⤵️

[Main](MockDataGen.py) <- You will find the module in charge of running the entire script here.

[FileHandle](FileHandle_Mod/FileHandle.py) <- You will find the module in charge of opening and creating files here.

[GetData](GetData_Mod/GetData.py) <- You will find the module in charge of collecting data and creating the mockdata here.

[Search](SearchIfExist_Mod/Search.py) <- Module in charge of searching if a file with old data already exists.

[Create](CreateRegisters_Mod/DataCreation.py) <- Module in charge of creating the data according the configurations (SQL or CSV).

### 📋    0.1 Pre-requirements ⤵️

➡️ _Install the libraries specified in [ _'requirements.txt'_ ](requirements.txt) Especially the Faker library_

## ⚙️ 1.0 Configuration process ⤵️

➡️ First of all, you have to pass some parameters for the script to work correctly, we will detail below.

### 🔩    1.1 Main configuration. 

➡️ Inside of "Configurations.json" file. ⤵️

```json
{
    "Configurations":{
        "DatasetName":"MyDataset",
        "DatasetFileToOpen":"MyDataset.config.json",
        "NameOfDatasetToSaveInJson":"MyNewDataset.json",
        "Directory_To_Save_csvFiles":"CSV_Files",
        "Directory_To_Save_jsonFiles":"JSON_Files",
        "Directory_To_Save_sqlFiles":"SQL_Files",
        "SQL_Format":true
    }
}
```
➡️ The field *'DatasetName'* refers to the name of the dataset in question, this field will be used as part of the name of the files generated by the script (the csv with the datamock and the json with the pk of each dataset table).

➡️ The field *'DatasetFileToOpen'* refers to the file that the script will open, where the table settings must be inside to be able to do the mocking data.

➡️ The field *'NameOfDatasetToSaveInJson'* refers to the file with json format that the script will generate, where it will contain the pk of each of the dataset tables, the recommended format is: NameOfTheDataSet.json, where _'NameOfTheDataSet'_ will be the name of the data set.

➡️ The field *'Directory_to_save_csvFiles'*, *'Directory_to_save_jsonFiles'* and *'Directory_to_save_sqlFiles'* refer to the directories that will be created to store the csv,  json and sql files respectively, generated by the script.

### ⚙️    1.2 Configuration of the dataset. ⤵️

➡️ The name of this file must be the one specified in *'DatasetFileToOpen'* in the _'Configurations.json'_ file. The configuration instructions **can be found in the following [Link](README2.md)**


## 🛠️ 2.0 Script operation. ⤵️

➡️ As mentioned before, the libraries contained in [_'requirements.txt'_](requirements.txt) must be installed for their correct operation.
The script will open the *Configurations.json* file to save the variables set by the user in its environment, it will search if there is already a json with tables and pks in the directory to avoid re-creating those tables and stepping on the old existing data. It will use the variable _'DatasetFileToOpen'_ to open the file with the dataset table structure and thus be able to iterate each of the dataset tables and within them, each of the column structures. As each column iterates, it will generate its data based on your settings. Later create a csv with said data for each table as well as a json file containing all the stations of each table.

---

## ⚠️ Limitations ⤵️
The script does not create data following a logic, but creates random data following the configuration patterns of the dataset.

---

## 📄 License ⤵️
This project is under license [MIT License] - read the file [LICENSE.md](LICENSE) for details.

---

## 📌 Technologies used. ⤵️

|<a href="https://www.python.org/downloads/"><img align="center" alt="Pyhton" src="https://github.com/caidevOficial/Logos/blob/master/Lenguajes/py_logo1_1.png?raw=true" width="50px" height="50px" />|<h3>Python</h3>|
|--------|----------|
|<a href="https://code.visualstudio.com/download"><img align="center" alt="VSC" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" width="50px" height="50px" />|<h3>VS Code</h3>|

---

## Where to find me: 🌎⤵️

| <img class="circular" alt="Facu" src="https://avatars1.githubusercontent.com/u/12877139?s=400&u=d369ee24466653d9bbeeb9654930e3ff1c67b76a&v=4" width="80px" height="80px" />||
|:----:|:----:|
|🤴 Facu Falcone|<center>Junior Developer</center>|
|<img alt="GitHub" src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white" width="125px" height="30px" />|<center><a href="https://github.com/caidevOficial/"><center>Github</center></a></center>|
|<img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" width="125px" height="30px" />|<a href="https://www.linkedin.com/in/facundo-falcone/"><center>LinkedIn</center></a>|
|<img alt='Invitame un café en cafecito.app' srcset='https://cdn.cafecito.app/imgs/buttons/button_5.png 1x, https://cdn.cafecito.app/imgs/buttons/button_5_2x.png 2x, https://cdn.cafecito.app/imgs/buttons/button_5_3.75x.png 3.75x' src='https://cdn.cafecito.app/imgs/buttons/button_5.png' width="125px" height="30px" />|<a href="https://cafecito.app/caidevoficial/"><center>CafecitoApp</center></a>|
|<img width="125px" height="30px" style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi1.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' />|<a href='https://ko-fi.com/P5P74JBOH' target='_blank'><center>Ko-Fi</center></a>|


<table>
    <tr>
        <td>
            <a href="#mockdata-generator-️">⬆️ Go Top</a>
        </td>
        <td>
            <a href="https://faker.readthedocs.io/en/master/providers.html">➡️ Go to Faker WebPage</a>
        </td>
    </tr>
</table>
