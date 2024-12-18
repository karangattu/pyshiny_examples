This app demonstrates:

1. Use of `page_opts()` to set:
   - A custom page title
   - Fillable layout (content fills available space)
   - A Bootstrap theme ("united")

2. A responsive layout with:
   - A sidebar containing date range and category filters
   - Two cards in a column layout showing a plot and summary table

3. Key features:
   - Date range selection
   - Category filtering
   - Reactive data filtering
   - Plot and table outputs

To run this app, you'll need the following packages:
```
pip install shiny pandas numpy matplotlib
```

The app provides a simple but functional dashboard interface where users can:
- Select a date range
- Filter by category
- See sales trends in a plot
- View summary statistics in a table

All data is generated on the fly using numpy and pandas, and the layout is responsive thanks to the `fillable=True` option in `page_opts()`.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKPEs2MKBXQAbUhW10ARjlw69C9toqiAZs1IxkvABZ0I81ZOZwoxCnQA3OFt7Rxc3XCw4AA90b15+TzY3dGkKImk6Im9uOGZRUQBiZABhb004J1gdSp4KKFElLGZOLgcsXjg4LgAKAEYAJgBmAEpROqhkAF4hLAARTSgAMRb4HpBRZC3kAHI6uB2UdC4sfYB9FogAczge3nrWKZ2BgAYBgBYAWhe+776dojoPJ0UhcXhTPovF5EOxwACOTzmOxGBE22x2vCg2jgvEOUmwlzaMGarTcFH6UKIkMpyGpKLRWx2xAqVxYuDxTUJ7WIzlIdGIt2AOwAggDdgAhMU7Eo7AC6VKhYwgAF8lUVkABlOBsDg3ZCkdD+ci8USZHBQG5nA0UXg9BnIfz6OBTYRgDVYnHIBYuQykKDMESEe02OjabRQQzYqYAFWY0mCEDVEGKZR8VCcdC4cEM-uQAHc6BRnMgyJR7NoTRAC0XkGbeJns-6eiNEPazSk0mdzpcbnaINsB8hXd3ODdXaj+4Otq6tdi-F6KsgAEqj4JBydT+7+ihTCZC-ZyrAwNzNidTrbULi7xb7iqHjTRZv2pUDtt0LAdihnTpz-wAL1ue1XzAZkqFZZhcHHIDthnOBf1KFk2SgjdBx5PkBXBYBXWFMNXVlZAAGpkAMe4ej3JlEIgw9pDEOF42bekUIHH84D8boXTAHDtFdZ8CmTZAAFkoDcEtyCoShRGrYszXDXBSE7MhtFkCBbRDMMYzjOAW3tKTa3fZkA2bVsmO2M0DK4M5nB8LNmDtN0PX4AB5IJmGQaMGDXF9z2grYAAEchsnBdGsEytizGwqmxXgzjMcltNCwc1KobwLImaZkCSvIu0WJ8EoHEMriIKBonSnQKA6aRDFi1S6CuesAKmCkiAANhGLzz22Yqgr0HpMpS7L6lvKg5RhUNku6AaoCFTEorldqOoEaIOm1M5HWxOyFlDeR3Si115o6rrOi-aJw0MOCNoqPafMHQ6VtwU7zpnByrry7YyqwaJ-GIABrW17HqI0ICmd4AFZ9vPd7-CuZwv1k+S4uugdvAoaRmH7Aq+IHXSzP9Xp4o6nGA0s6y8jsnbPQ1WQNAgl6Ouu-zLzyU5FjOOxYATDrwqcKn-VwVaI3W-GFq2PqJrSmY+sm3Lha2XgeYg0qTgWeoVnZ9ZEfPHYBO1Zh+TxIVoz0LFNQcqVhRci1Kk27RttNogdgAOVkM7XNICKFlwXF5Q1qcdgANSxeN9Z9habFdAASEBRdSm8MVN2UKpgIyCCwF4bGVZCZdDiOo7GvIxdjmacXvHwIGT1P08zrPz2xMvo8m8HhdlEPVRD5HUf7OWYGpyCIFEBnfH8IIsGZbRiHGOAIsliYjPtFNyBc5IlDSZmqAuVdmwdUhkH2fx4HtEdrkqGZP1XuB16P6Xti3VgBuP2YKFIO+99uQ+bmAF5ZXmy878VrBH+fh5MiFQL7vz6F-e0c9kBLDzq5Qw8h9j2g0Lwb66VgGDT2HefCAA+GYN8vz7BGMgAAZMgdBU1MHDXwgAHhmD-QhwZYHdHSnuZB30E5kDwFfacKFigwKsHkZA8CSyUQ8BFCA5hsK4TAPaOgEVT6gTgOBXAm8ACEMwpHcSQNdaO6Vo7AH0RRMCbI5TTBPsvcqijlHNmbihe07c0YZSYVwMAyoiDgGgPAWgYBvB0ToN4eAlBeD-0+oQEgYlqAUG8aIDQWhgoGEMI0WQeBRAcG4HwTGMtXGyiAA)
