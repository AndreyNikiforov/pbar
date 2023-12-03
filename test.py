# works

import logging
import time
from tqdm.contrib.logging import logging_redirect_tqdm
from tqdm import tqdm


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# works (resizing rearranges already printed log, but bar is fine)
# with logging_redirect_tqdm():
#     for i in tqdm(range(1,10), dynamic_ncols=True):
#     # for i in range(1,10):
#         logging.debug(f"Before Value is {i}")
#         time.sleep(1)
#         logging.info(f"After Value is {i}")

# works (resizing rearranges already printed log and bar is spilling into the log on resizing)
logger = logging.getLogger("icloudpd")
with logging_redirect_tqdm():
    for i in tqdm(range(1,100), 
                  dynamic_ncols=True,
                  leave = False,
                  ascii = True):
    # for i in range(1,10):
        logger.debug(f"Before Value is {i}")
        time.sleep(1)
        logger.info(f"After Value is {i}")


# nested from examples - works (except resizing)
# with logging_redirect_tqdm():