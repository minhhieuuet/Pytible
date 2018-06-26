import requests
import os
r = requests.delete('https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAADZAb0ZA3rd8BACjySOYwg7GOlY4CX8foWIVYZCCkD3DZAE83TEdSKis6hLKqOwpgdr7c5Uc2qr7FIFTMIyTvCG8AZAUBZAinSZCzpMZBJpVc3xgSgQGOS956R2HTLZCkyDeHgCzOGR9spZAdZCwO69H7ZBTxNRgucvHs7JSiQGGuPf1QZDZD',json={"fields":["persistent_menu"]})
print (r.status_code)
