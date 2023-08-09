# CodeAssault - PHP Code Auditing Tool

CodeAssault is a powerful PHP code audit tool that can automatically scan for common web security vulnerabilities, such as SQL injection, XSS, command injection, etc. This tool is designed to assist developers and security experts in quickly discovering potential security risks in code.

## Features 

- **Multi-rule detection**: It has a variety of predefined security rules, covering most of the common web security vulnerabilities.
-  **Extensible**: Users can easily add custom detection rules. 
-  **Easy to use**: The command line interface is straightforward and easy to use. 



## Installation

Make sure you have Python 3 installed on your system.

1. Clone this repository locally：   

   ```bash
   git clone https://github.com/WitchWatcher/CodeAssault.git
   ```

2. Enter the project directory:

   ```bash
   cd CodeAssault
   ```

3. Dependencies required for installation:

   ```bash
   pip3 install -r requirements.txt
   ```



## How to use

### Single file scan

```bash
python3 bin/cli.py yourfile.php
```

<img width="802" alt="image" src="https://github.com/WitchWatcher/CodeAssault/assets/119853210/2812f776-9273-4c81-9be5-eaa5c3ec150c">


### Folder scanning

```
python3 bin/cli.py -f yourdirectory
```

<img width="844" alt="image" src="https://github.com/WitchWatcher/CodeAssault/assets/119853210/89cb38fa-a14e-4ac7-a33c-c5bb46db416e">



### Show Help

```
python3 bin/cli.py -h
```

### Show version

```
python3 bin/cli.py -v
```



## How to add custom rules

See [docs/rules.md](xx) for how to add or modify detection rules.




## License

This project is licensed under the MIT license. See the LICENSE file for details.


## Contribute

Pull requests and issue reports are welcome! Please make sure to read the [Contribution Guidelines](#) before submitting.



## Contact the author

If you have any questions or suggestions, please contact us at [issues](https://github.com/WitchWatcher/CodeAssault/issues).
