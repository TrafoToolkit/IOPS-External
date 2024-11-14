# Installation #

```
git submodule update --init --recursive
```


```
python install.py
```

# Running #

Run the components by using the following scripts.

```
start_live_pnp.sh
start_live_viewer.sh
start_location_engine.sh
start_logger.sh
```

# Configuration #

The configuration is placed into the folder `IOPS-data/`.
The main configuration is done in `IOPS_CONFIG.ini`.
Paths specified in `IOPS_CONFIG.ini` are parsed relative to that file.

A default template containing all available options is found in `DEFAULT_CONFIG.ini`
