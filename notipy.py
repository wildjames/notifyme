import getpass
import glob
import json

import yagmail as yag


if __name__ == "__main__":
    # Gather the files
    myLoc = '.'
    fnames = list(glob.iglob('{}/Final_figs/*.pdf'.format(myLoc), recursive=True))
    fnames = [name for name in fnames if not "corner" in name.lower()]
    print("fnames: ")
    for name in fnames:
        print("-> '{}'".format(name))

    # Who from, who to
    send_to = 'jwild2@sheffield.ac.uk'

    with open("email_details.json", 'r') as f:
        details = json.load(f)
        send_from = details['user']
        pword = details['pass']

    # Server
    server = "smtp.gmail.com"


    subject = "Incoming files"

    contents = [
        'This is some test body text'
    ]
    contents.extend(fnames)

    client = yag.SMTP(send_from, pword)
    client.send(send_to, subject, contents)
