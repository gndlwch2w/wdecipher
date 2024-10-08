# WDecipher

![Static Badge](https://img.shields.io/badge/Author-Chisheng%20Chen-blue)
![PyPI - License](https://img.shields.io/pypi/l/pycinante)
![GitHub last commit](https://img.shields.io/github/last-commit/gndlwch2w/wdecipher)
![PyPI - Version](https://img.shields.io/pypi/v/wdecipher)

WDecipher (Wechat Database dECIPER) is a third-party extension tool for WeChat that can decrypt WeChat SQLite databases and export and merge databases. This enables various backend extension services such as data analysis and model training to be implemented on it. 

WDecipher is a compressed version of [PyWxDump](https://github.com/xaoyaoo/PyWxDump) with a small amount of code and interface optimization.

## Features

- Get the WeChat decryption key (db_key) for the SQLite database
- Supports automatic search for the location and type of all databases
- Allows to decrypt WeChat SQLite database based on the key
- Allows merging different types of databases into one
- Provides standard package-level interfaces and code comments to facilitate expansion and development

## Interfaces

There are two package-level interfaces for you to use, namely `wx_info.py` and `wx_db.py`. For `wx_info.py`, it provides interfaces for obtaining WeChat account information, mainly including:

- `get_wx_pids() -> List[int]`: Returns all currently running WeChat process ids
- `get_wxid(process) -> Optional[str]`: Retrieves the wxid of the specified WeChat process login
- `get_wx_dir(wxid: str, process=None) -> Optional[str]`: Finds the working directory of the specified WeChat id
- `verify_db_key(db_key: bytes, db_path: str) -> bool`: Verifies that the key is valid by decrypting the specified database
- `get_db_key(process, wx_dir: str, **kwargs: Any) -> Optional[bytes]`: Retrieves the database decryption key
- `get_wx_info(pid: int) -> Dict[str, str]`: Returns the account information of the current online WeChat process
- *`get_wx_infos() -> List[Dict[str, str]]`: Returns all currently running WeChat account information

For `wx_db.py`, it provides interfaces for WeChat database operations, mainly including:

- *`get_wx_dbs(wx_dir: str, db_types: Optional[str | List[str]] = None) -> List[Dict[str, str]]`:  Returns all databases of the specified type that exist in the specified WeChat working directory
- `merge_wx_db(srcs: List[str], dest: str, verbose: bool = True) -> None`: Merges multiple WeChat databases of the same type into one
- `decrypt_wx_db(key: str, db_path: str, out_path: str) -> None`: Decrypt the WeChat database.
- *`batch_decrypt_wx_db(key: str, dbs: List[Dict[str, str]], out_dir: str, merge_db: bool = True, verbose: bool = True) -> None`: Batch decryption of WeChat database

If there is no development purpose, the interfaces marked with * can complete most of the work. Here is an example (**before you execute the following script you need ensure your WeChat account logined**): 

```python
from wdecipher import get_wx_infos, get_wx_dbs, batch_decrypt_wx_db

info = get_wx_infos()[0]
db_key, wx_dir = info["db_key"], info["wx_dir"]

out_dir = "/tmp/decrypted_db"
dbs = get_wx_dbs(wx_dir)
batch_decrypt_wx_db(db_key, dbs, out_dir)
```

## Supported platforms

The support for each platform is shown in the following table. **MacOS is being supported in the future** and a unified access interface will be provided. **For mobile devices, no further support is considered.** If there are related services, please refer to [Migrate WeChat Chat History](https://zhuanlan.zhihu.com/p/709164758) and then perform subsequent operations on the PC.

|    Platform    | Supported |
|:--------------:| :-------: |
| Windows >= 10  |    Yes    |
|     MacOS      |    No     |
| Android or IOS |    No     |

## Disclaimer

- This project is only for learning and communication purposes, **do not use it for illegal purposes**, otherwise the consequences will be borne by yourself
- Users understand and agree that any violation of laws and regulations, infringement of the legitimate rights and interests of others, is unrelated to this project and its developers, and the consequences are borne by the user themselves

## Acknowledgments

- PyWxDump: [https://github.com/xaoyaoo/PyWxDump](https://github.com/xaoyaoo/PyWxDump)
