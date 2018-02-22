# :fist: gripper
Script to render an entire folder's GitHub Markdown files to HTML while keeping relative links.

---

## Pre-requisites

- [Python](https://python.org/)
- [A GitHub account](https://github.com/join)
- [A GitHub access token with an empty scope](https://github.com/settings/tokens/new?scopes=)
- [grip](https://github.com/joeyespo/grip)
> NOTE: Both Python2 and Python3 should work.

Once **grip** is installed, create `~/.grip/settings.py`
> NOTE: Create `%userprofile%/.grip/settings.py` if using Windows.

Add the following lines to the file:
```python
USERNAME = 'YOUR_GITHUB_USERNAME'
PASSWORD = 'YOUR_GITHUB_ACCESS_TOKEN'
```
> NOTE: You can also put in your GitHub password but this is not safe.

This allows you to use the GitHub API for rendering with an increased limit of 5,000 requests per hour (instead of 60).

---

## Usage
Copy `grip-folder.py` and paste it into some folder that contains Markdown files.

Run the script and pass the current folder:
```
python grip-folder.py ./
```
> NOTE: You can also pass the relative path to some folder that contains Markdown files instead of copying and pasting.

Additionally, the script contains a list called `ignored`. You can pass folder and file names if you wish to ignore them.

---

## Example
Say you have some kind of wiki going on in the following structure:

```bash
├── wiki
│   ├── chapters
│   │   ├── chapter1.md
│   │   ├── chapter2.md
│   │   ├── chapter3.md
│   │   └── chapter4.md
│   ├── images
│   │   ├── image1.png
│   │   └── image2.png
└────── README.md
```

The easiest way would be for you to copy `grip-folder.py` and paste it on the `wiki` folder:

```bash
├── wiki
│   ├── chapters
│   │   ├── chapter1.md
│   │   ├── chapter2.md
│   │   ├── chapter3.md
│   │   └── chapter4.md
│   ├── images
│   │   ├── image1.png
│   │   └── image2.png
│   └── README.md
└────── grip-folder.py
```

Then simply run:
```
python grip-folder.py ./
```

This will recursively enter all folders, make the necessary references and convert the GitHub Markdown to HTML using **grip**. The HTML files will be right next to their Markdown counterparts:

```bash
├── wiki
│   ├── chapters
│   │   ├── chapter1.md
│   │   ├── chapter1.html
│   │   ├── chapter2.md
│   │   ├── chapter2.html
│   │   ├── chapter3.md
│   │   ├── chapter3.html
│   │   └── chapter4.md
│   │   └── chapter4.html
│   ├── images
│   │   ├── image1.png
│   │   └── image2.png
│   ├── README.md
│   └── README.html
└────── grip-folder.py
```

---

## Credits
**[grip](https://github.com/joeyespo/grip)** is a great tool created by [Joe Esposito](https://github.com/joeyespo).

This script simply uses his tool to recursively convert Markdown files in a folder structure.
