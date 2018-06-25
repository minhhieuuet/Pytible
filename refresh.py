import requests
import os
r = requests.delete('https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAADZAb0ZA3rd8BAA6nyWL3hzlHN87mW4WC2dltYbZBSGZAFNZC3vacIR9cg2lMpZBO9r4PU4wZCZAD0pvYBkUUo77k2etZAJg3WDlpQy2FQQDMDEqQFFLMdOnSKfysZB7plLoXv5lN4nYslzov9tF55RY9jIvRgZCEy0KeuGiVApaZBVOQZDZD',json={"fields":["persistent_menu"]})
print (r.status_code)
