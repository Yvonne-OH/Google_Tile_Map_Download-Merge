
<h1 align="center">
  <br>
  <img src="Logo/Upenn.jpg" alt="Markdownify" width="600"></a>
  <br>
</h1>

<h4 align="center">The provided Python script utilizes various modules for GIS mapping, image processing, and merging map tiles.</h4>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#license">License</a>
</p>

![screenshot](merge.jpg)

## Key Features

* Map Tile Downloading:
  - Utilizes the Tile_Map_Download module to download map tiles within a specified geographic area defined by bounding box coordinates.
* GIS Calculation:
  - Employs the Gis_Calculate module to calculate distances and midpoint coordinates based on the provided bounding box.
* Map Tile Merging:
  - Uses the Tile_Map_Merge module to merge the downloaded map tiles into a single image.
* Image Processing:
  - Utilizes the Image_Processing module to enhance the merged image by adding a center marker, a white border, filled corner rectangles, and overlaying logos.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and requirements installed on your computer. 
From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Yvonne-OH/Google_Tile_Map_Download-Merge.git

# Go into the repository
$ cd Google_Tile_Map_Download-Merge

# Install dependencies
$ pip install geopy numpy opencv-python tqdm

# Run the app
$ Your API KEY ="**********************"
```

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)

