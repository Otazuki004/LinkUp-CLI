import logging

class Server:
  def __init__(url = "localhost:8080", https=True):
    self.httpurl = f"https://{url}/" if https else f"http://{url}/"
    self.wsurl = f"wss://{url}/" if https else f"ws://{url}/"
    self.info = logging.info
    self.info("hm")