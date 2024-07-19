# Squares

Squares is a simple library that provides geometric primitives.

## Usage
```python
import squares

circle = squares.Circle(5)
print(circle.square())

triangle = squares.Triangle(3, 4, 5)
print(triangle.square())
print(triangle.is_right())

patched = triangle.with_sides(b=5)


```

## Building & Testing
```shell
git clone https://github.com/burenotti/squares
cd squares

make install # prepares project
make cover # Runs test and reports coverage
```
