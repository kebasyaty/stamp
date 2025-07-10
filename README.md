<div align="center">
 <br>
  <p align="center">
    <a href="https://github.com/kebasyaty/stamp">
      <img
        height="120"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/stamp/main/assets/logo.svg">
    </a>
  </p>
  <p>
    <h1>Stamp</h1>
    <h3>UV + FastAPI + Ramifice = Stamp</h3>
    <p align="center">
      A template project for creating web applications.
    </p>
  </p>
</div>

##

[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
<br>
_Supports MongoDB 3.6, 4.0, 4.2, 4.4, 5.0, 6.0, 7.0, and 8.0._
<br>
_For more information see [PyMongo](https://pypi.org/project/pymongo/ "PyMongo")_.

<br>

## Install for work with Stamp

**Install MongoDB:**<br>
[![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)](https://github.com/kebasyaty/stamp/blob/main/assets/FEDORA_INSTALL_MONGODB.md)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/kebasyaty/stamp/blob/main/assets/UBUNTU_INSTALL_MONGODB.md)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.mongodb.com/try/download/community)

**Install gettext:**

```shell
# Fedora:
sudo dnf install gettext
gettext --version
# Ubuntu:
sudo apt install gettext
gettext --version
# Windows:
https://mlocati.github.io/articles/gettext-iconv-windows.html
gettext --version
```

**Install UV:**

```shell
# Install UV:
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Checking installed version:
uv --version

# Install the latest version of Python:
uv python install
```

**Run Stamp:**

```shell
# Go to the directory with a Stamp:
cd stamp
# Install all dependencies:
uv sync
# Run:
uv run python src/run_server.py
# Open the browser on:
http://127.0.0.1:8000
```

### How to create custom translations ?

```python
from ramifice import translations

translations.DEFAULT_LOCALE = "en"  # For Ramifice by default = "en"
LANGUAGES = frozenset(("en", "ru"))  # For Ramifice by default = ["en", "ru"]
```

```shell
cd project_name
# Add your custom translations:
uv run pybabel extract -o config/translations/custom.pot src/app
uv run pybabel init -i config/translations/custom.pot -d config/translations/custom -l en
uv run pybabel init -i config/translations/custom.pot -d config/translations/custom -l ru
...
# Hint: Do not forget to add translations for new languages.
uv run pybabel compile -d config/translations/custom

# Update your custom translations:
uv run pybabel extract -o config/translations/custom.pot src/app
uv run pybabel update -i config/translations/custom.pot -d config/translations/custom
# Hint: Do not forget to check the translations for existing languages.
uv run pybabel compile -d config/translations/custom
```

### How to add new languages ​​to Ramifice ?

```python
from ramifice import translations

translations.DEFAULT_LOCALE = "en"  # For Ramifice by default = "en"
translations.LANGUAGES = frozenset(("en", "ru", "de", "de_ch"))  # For Ramifice by default = ["en", "ru"]
```

```shell
cd project_name
# Example:
uv run pybabel init -i config/translations/ramifice.pot -d config/translations/ramifice -l de
uv run pybabel init -i config/translations/ramifice.pot -d config/translations/ramifice -l de_ch
...
# Hint: Do not forget to add translations for new languages.
uv run pybabel compile -d config/translations/ramifice

# Update translations to Ramifice:
uv run pybabel extract -o config/translations/ramifice.pot ramifice
uv run pybabel update -i config/translations/ramifice.pot -d config/translations/ramifice
# Hint: Do not forget to check the translations for existing languages.
uv run pybabel compile -d config/translations/ramifice
```
