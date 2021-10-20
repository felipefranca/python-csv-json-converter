import logging

from pathlib import Path

import click

logging.basicConfig(
  level="DEBUG", format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
)

logger = logging.getLogger(__name__)


@click.command()
@click.option(
  "--input", 
  "-i", 
  default="./", 
  help="Path where to find the CSV files to be converter to JSON.", 
  type=str
)
@click.option(
  "--output", 
  "-o", 
  default="./", 
  help="Path where the converted files will be saved.", 
  type=str
)
@click.option(
  "--prefix", 
  "-p",
  prompt=True,
  prompt_required=False,
  default="file", 
  help=(
    "Prefix used to prepend to the name of the converted file saved on disk. " 
    "The suffix will be a number starting from 0. ge: file_0.json"
  )
)
def converter(input: str = "./", output: str = "./", delimiter: str = ",", prefix: str = None):
    input_path = Path(input)
    output_path = Path(output)
    logger.info("input Path %s", input_path)
    logger.info("output Path %s", output_path)
    for p in [input_path, output_path]:
      if not (p.is_file() or p.is_dir()):
        raise TypeError("Not a valid path of file name.")
    data = read_csv_file()
    save_to_json_files()

def read_csv_file(source: Path, delimiter: str = ",") -> tuple:
    """Load a single csv file or all files withing a directory.

    Args:
        source (Path): Path for a single file or directory .
        delimiter (str, optional): Separator for collumns int the csv's. Defaults to ",".
    
    Returns:
        tuple: All dataframes loaded from the given source path.
    """
    if source.is_file():
        logger.info("Reading csv file %s",source)

def save_to_json_files():
     logger.info("Saving")
