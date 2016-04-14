# fdroid-miner
A simple miner for FDroid

## Usage
```{bash}
$> git clone https://github.com/jeandersonbc/fdroid-miner.git && cd fdroid-miner 
$> ./main.py
```

## Expected Output

Given that `main.py` executed without erros, a subdirectory named "downloads" will be created with all
downloaded apps and respectives sources:

```
fdroid-miner
|_ main.py
|_ downloads
    |_ com-app-example
    |   |_ com.app.example_1.apk
    |   |_ com.app.example_1_src.tar.gz
    ...  
```

It's important to mention that, if a given app has multiple packages available for donwload, it is going to
be considered only the latest version.

## Dependencies
* Python 2
