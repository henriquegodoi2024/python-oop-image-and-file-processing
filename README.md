# python-oop-image-and-file-processing
Python project featuring object oriented programming, image manipulation, and file processing. Includes a custom Rectangle class with geometric methods, image transformation functions for black and white conversion and flipping, and a simple city population search program built from file based data.

A multi-part Python project covering object-oriented programming, data file searching, and image processing through three independent modules.

---

## Project Structure

| File | Responsibility |
|---|---|
| `rectangle_class.py` | `Rectangle` class — geometric shape representation and manipulation |
| `city_population_search.py` | Interactive CLI tool for searching historical US city population data |
| `image_transformations.py` | Pixel-level image processing transformations |

---

## Part 1 — Rectangle Class (`rectangle_class.py`)

A class representing a 2D rectangle with support for geometric calculations, scaling, and comparison.

### Usage

```python
from rectangle_class import Rectangle

r = Rectangle(5, 3, 'cm')
print(r)                  # 5 x 3 cm

r.area()                  # 15
r.perimeter()             # 16
r.diagonal()              # 5.83...

r.grow(2, 1)
print(r)                  # 7 x 4 cm

r.scale(2)
print(r)                  # 14 x 8 cm

# Compare two rectangles
r1 = Rectangle(4, 5, 'cm')
r2 = Rectangle(4, 5, 'cm')
r1 == r2                  # True

r1.larger_than(r2)        # False (equal area)
```

### Methods

| Method | Description |
|---|---|
| `area()` | Returns width × height |
| `perimeter()` | Returns 2×width + 2×height |
| `diagonal()` | Returns the length of the diagonal using Pythagoras |
| `grow(dwidth, dheight)` | Increases dimensions by the given amounts (in place) |
| `scale(factor)` | Multiplies both dimensions by factor (in place) |
| `larger_than(other)` | Returns `True` if this rectangle's area exceeds `other`'s |
| `__eq__(other)` | Returns `True` if width, height, and unit all match |
| `__repr__()` | Returns a string like `5 x 3 cm` |

---

## Part 2 — City Population Search (`city_population_search.py`)

An interactive command-line tool that searches a CSV data file for historical US city population rankings and prints formatted results.

### Data File Format

Expects a CSV file with the following columns:

```
year, rank, city, state, population
```

Where population is stored in thousands (e.g., `250` = 250,000).

### Usage

Run the program directly:

```
python city_population_search.py
```

Then follow the prompts:

```
Enter the name of data file: cities.txt
city: Boston
state abbreviation: MA
```

**Example output:**
```
1950     5       362,000
1960     8       697,000
1970    12       641,000
```

Type `quit` at the city prompt to exit.

### Functions

| Function | Description |
|---|---|
| `find_results(filename, city, state)` | Searches the file and prints all matching records |
| `output_formatted(year, rank, population)` | Formats and prints a single result row |
| `main()` | Interactive loop — prompts for city and state until `quit` |

---

## Part 3 — Image Transformations (`image_transformations.py`)

A set of pixel-level image processing functions that transform images represented as 2D lists of `[R, G, B]` pixels.

### Dependencies

Requires the `hmcpng` library for loading and saving images:

```python
from hmcpng import load_pixels, save_pixels, compare_images
```

### Usage

```python
from hmcpng import load_pixels, save_pixels
from image_transformations import bw, flip_horiz, fold_diag

pixels = load_pixels('photo.png')

# Convert to black and white
bw_image = bw(pixels, threshold=128)
save_pixels(bw_image, 'photo_bw.png')

# Flip horizontally
flipped = flip_horiz(pixels)
save_pixels(flipped, 'photo_flipped.png')

# Fold along diagonal
folded = fold_diag(pixels)
save_pixels(folded, 'photo_folded.png')
```

### Transformations

| Function | Description |
|---|---|
| `bw(pixels, threshold)` | Converts image to black and white — pixels brighter than `threshold` become white, the rest black |
| `flip_horiz(pixels)` | Mirrors the image horizontally (left becomes right) |
| `fold_diag(pixels)` | Folds the image along its top-left to bottom-right diagonal — everything below the diagonal becomes white |
| `brightness(pixel)` | Helper — returns a 0–255 brightness value for a single pixel using weighted RGB formula |
| `create_green_image(height, width)` | Helper — creates a blank all-green pixel grid of the given dimensions |

### Brightness Formula

Brightness is calculated using a weighted average that approximates human visual perception:

```
brightness = (21×R + 72×G + 7×B) / 100
```

Green is weighted most heavily because human eyes are most sensitive to it.

---

## Requirements

- Python 3.x
- `hmcpng` library (for image transformations only)
- A CSV data file for the city population search
- No other external libraries required

---

## Limitations

- `city_population_search.py` — city and state inputs are case-sensitive; `boston` will not match `Boston`
- `image_transformations.py` — `fold_diag` assumes a square image; on non-square images the fold effect will be asymmetric
- `rectangle_class.py` — `__eq__` compares units as strings, so `Rectangle(5, 3, 'cm')` and `Rectangle(5, 3, 'CM')` are treated as unequal
