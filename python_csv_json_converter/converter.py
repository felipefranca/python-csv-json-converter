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
    
    
    logger.info("teste")
