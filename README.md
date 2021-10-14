<h1 align="center">🛠️ cvtools</h1>

## 🚀 Installation

```console
# clone project repository
git clone git@github.com:SkalskiP/cvtools.git
# navigate to project root directory
cd cvtools
# create python virtual environment and activate it (optional)
virtualenv venv
source venv/bin/activate
# install project
pip install --upgrade pip
pip install -e ".[test]"
```

## 📜 Scripts

### `cvtools.scripts.record`

| **argument**            | **mandatory** | **type** | **description**                                       |
|:-----------------------:|:-------------:|:--------:|:------------------------------------------------------|
| `device-id`             | ✓             | `int`    | specifies device id of webcam you would like to use   |
| `frame_interval`        | ✗             | `int`    | defines frequency of saving frames                    |
| `target_directory_path` | ✓             | `str`    | specifies target directory where frames will be saved |