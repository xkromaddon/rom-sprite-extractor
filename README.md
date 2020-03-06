# XKROM - Ragnarok Mobile Atlas Sprites Extractor using Python

## Prerequisite
1. Download [AssetStudioGUI](https://github.com/Perfare/AssetStudio).
2. Python 3.6 and above with [Pillow Library](https://pypi.org/project/Pillow/#description) 
3. `picture` and `preferb` folder located on your game's data. Usually located at:
```
Android > data > package_name > files > Android > resources > gui > atlas
```

## How to Extract Atlas Sprites into Individual Textures
1. Open AssetStudioGUI and load the `picture` and `preferb` asset files.
2. Extract all Texture2D and MonoBehaviour.
3. Run the python script: `py import.py`
4. wait for it to finish.