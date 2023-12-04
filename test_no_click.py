# works
from multiprocessing import freeze_support
freeze_support()

import warnings
warnings.filterwarnings("ignore")

import logging
import time
import sys

import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

def tqdm_main():
    """tqdm as in icloupd without click"""

    # works (resizing rearranges already printed log and bar is spilling into the log on resizing)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", stream=sys.stdout)
    logger = logging.getLogger("icloudpd")

    with logging_redirect_tqdm():
        for i in tqdm.tqdm(range(1,100), 
                    dynamic_ncols=True,
                    leave = False,
                    ascii = True):
        # for i in range(1,10):
            logger.debug(f"Before Value is {i}")
            time.sleep(1)
            logger.info(f"After Value is {i}")

if __name__ == "__main__":
    tqdm_main()
