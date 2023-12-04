# works

import logging
import time
from tqdm.contrib.logging import logging_redirect_tqdm
import tqdm
import click
import alive_progress
from rich.progress import track
from rich.logging import RichHandler
from multiprocessing import freeze_support

@click.group()
def commands():
    pass


# works (resizing rearranges already printed log, but bar is fine)
# with logging_redirect_tqdm():
#     for i in tqdm(range(1,10), dynamic_ncols=True):
#     # for i in range(1,10):
#         logging.debug(f"Before Value is {i}")
#         time.sleep(1)
#         logging.info(f"After Value is {i}")

@commands.command(name="tqdm")
@click.option(
    "--logging-redirect",
    help="Use logging redirector or not",
    default=True
)
@click.option(
    "--freeze-mp",
    help="Call multiprocessor.freeze_support() or not",
    default=False
)
def tqdm_main(logging_redirect, freeze_mp):
    """tqdm as in icloupd"""

    # works (resizing rearranges already printed log and bar is spilling into the log on resizing)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("icloudpd")
    if (freeze_mp):
        freeze_support()

    if (logging_redirect):
        with logging_redirect_tqdm():
            for i in tqdm.tqdm(range(1,100), 
                        dynamic_ncols=True,
                        leave = False,
                        ascii = True):
            # for i in range(1,10):
                logger.debug(f"Before Value is {i}")
                time.sleep(1)
                logger.info(f"After Value is {i}")
    else:
        for i in tqdm.tqdm(range(1,100), 
                    dynamic_ncols=True,
                    leave = False,
                    ascii = True):
        # for i in range(1,10):
            logger.debug(f"Before Value is {i}")
            time.sleep(1)
            logger.info(f"After Value is {i}")


@commands.command(name="alive")
def alive_main():
    """alive.progress"""

    # works (resizing rearranges already printed log and bar is spilling into the log on resizing)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("icloudpd")
    for i in alive_progress.alive_it(
        range(1,100), 
        spinner=None,
        enrich_print=False,
        receipt = False,
        ctrl_c = False,
        ):
    # for i in range(1,10):
        logger.debug(f"Before Value is {i}")
        time.sleep(1)
        logger.info(f"After Value is {i}")

@commands.command(name="rich")
@click.option(
    "--custom-logger",
    help="Use custom logging handler or not",
    default=False
)
def rich_main(custom_logger):
    """rich.progress"""

    # works (resizing rearranges already printed log and bar is spilling into the log on resizing)
    if (custom_logger):
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", handlers=[RichHandler()])
    else:
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("icloudpd")
    for i in track(
        range(1,100), 
        ):
    # for i in range(1,10):
        logger.debug(f"Before Value is {i}")
        time.sleep(1)
        logger.info(f"After Value is {i}")

def main():
    commands()

if __name__ == "__main__":
    main()
