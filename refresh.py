import requests
import os
r = requests.delete('https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAADZAb0ZA3rd8BAHi3iKW5M28Uus9WkDY26iCeANMfZAGX76GDlJWnS517IkvWUS84cXxoaUP9z7070hDZBEA9pdzdPDoIVFHS8XNPnDy1r97rNnD79SEJ6gq8UUF30vNuEZAvlwe992plzzYdaRNzPkfZAUrx3LbbTsY5em4LxwZDZD',json={"fields":["persistent_menu"]})
print (r.status_code)
