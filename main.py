import logging
import time
import sys
import os

import add_products_to_cart_and_checkout_wf as awf

# TODO: Add command line param for number of iterations.

if __name__ == "__main__":
    file_handler = logging.FileHandler("otel-simulator.log")
    stderr_handler = logging.StreamHandler(stream=sys.stderr)

    logging.basicConfig(
        level=logging.DEBUG if os.environ.get("OTEL_DEMO_DEBUG") else logging.INFO, 
        handlers=[file_handler, stderr_handler],
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )

    logger = logging.getLogger(__name__)
    iterations = 100

    while iterations > 0:
        iterations -= awf.execute(iterations)
        if iterations > 0:
            logger.warn("Not all iterations were completed, continuing")
            time.sleep(5)
        else:
            logger.info("Done")
