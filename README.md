<div align="center">
 <br>
  <p align="center">
    <a href="https://github.com/kebasyaty/stamp">
      <img
        height="160"
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

<br>

## Install for work with Stamp

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

# Install UV:
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Checking installed version:
uv --version

# Install the latest version of Python:
uv python install

# Go to the directory with an example:
cd stamp
# Run:
uv sync
uv run python src/stamp/main.py
```

## Contributors

- [kebasyaty](https://github.com/kebasyaty) Gennady Kostyunin - creator and maintainer

## Changelog

[View the change history.](https://github.com/kebasyaty/stamp/blob/main/CHANGELOG.md "Changelog")

## License

**This project is licensed under the** [MIT](https://github.com/kebasyaty/stamp/blob/main/LICENSE "MIT")**.**
