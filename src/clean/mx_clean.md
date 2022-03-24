# mx clean

```bash
mx clean [options] mx-file
```

Drops rows and columns where all elements are zero

## Options

`-mi`, `--input-metadata-files`

Comma delimited list of metadata that matches the shape of the matrix, ordered by axis (e.g. row,col)

`-mo`, `--output-metadata-files`

Comma delimited list of metadata to be written, ordered by axis (e.g. row,col)

`-o`, `--output`

The name of the output mx file

## Examples

```bash
$ mx clean -mi barcodes.txt,genes.txt -mo clean_barcodes.txt,clean_genes.txt -o clean.mx matrix.mx
# drops rows and columns that sum to zeros
```