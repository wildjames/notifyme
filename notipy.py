import getpass
import glob
import json

import yagmail as yag


if __name__ == "__main__":
    # Gather the files
    myLoc = '.'
    fnames = list(glob.iglob('{}/**/*.png'.format(myLoc), recursive=True))
    fnames = [name for name in fnames if not "corner" in name.lower()]
    print("fnames: ")
    for name in fnames:
        print("-> '{}'".format(name))

    # Who from, who to
    send_to = 'wild.james343@gmail.com'
    send_from = "jwild2@sheffield.ac.uk"

    # Server
    server = "smtp.gmail.com"

    pword = getpass.getpass("Enter email password: ")

    subject = "Incoming files"

    contents = [
        'This is some test body text'
    ]
    contents.extend(fnames)

    client = yag.SMTP(send_from, pword)
    client.send(send_to, subject, contents)
