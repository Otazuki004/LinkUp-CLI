import logging

logging.basicConfig(
  format="[LinkUp] - %(message)s",
  handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
  level=logging.INFO,
)
