# Web server for image classification


## Download the repository

Use git to clone the repository:

```bash
git clone https://github.com/unica-isde/web-server-2023
```

Optional but recommended - create conda environment: https://docs.conda.io/projects/miniconda/en/latest/
```bash
conda create --name isde python=3.10
conda activate isde
```

And install the requirements with 

```bash
pip install -r requirements.txt
```

Additional requirements:
* Redis - install redis and check that it is running

## Configuration

Configure the service by editing the file `app/config.py`.

## Prepare the resources

It is recommended to pre-download images and models before running 
the server. This is to avoid unnecessary waits for users.

Run `python app/prepare_images.py` and `python app/prepare_models.py`. Models will 
be stored in your PyTorch cache directory, while the path for 
the image directory can be found in the `app/config.py` file. 

```bash
python app/prepare_images.py
python app/prepare_models.py
```

## Usage

### Run locally


To run the code without containers, it is sufficient to run 
separately the server,

```bash
uvicorn main:app --reload
```

And then run the `worker.py` script. 
The worker will process jobs stored in the queue. 
In order for the queue to work, you should have `redis`  
installed and running (specify port in `config.py`). 

NOTE: on MacOS, it is necessary to disable the fork safety 
before running the worker. Don't worry, it will be disabled only 
for the current session of the terminal.

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```
