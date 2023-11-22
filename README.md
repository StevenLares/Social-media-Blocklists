# Social media - Blocklists
Social media DNS Blocklists for Pihole/AdGuard
Now includes a script (create_hosts.py) to convert host files to both Pihole and Adguard formats.

## Usage

# Pi-Hole
1. Login into `Pi-hole admin`
2. Navigate to `Settings`
3. Expand `Pi-Hole's Block Lists`
4. Copy this URL: `https://raw.githubusercontent.com/StevenLares/Block_facebook_dns/master/pihole-facebook.txt`
5. Paste the URL in the Edit box and click on `Save and update`


# AdGuard
1. Login into `AdGuard`
2. Navigate to `Filters`
3. Click `Add filter`
4. Enter name
5. Copy this URL: `https://raw.githubusercontent.com/StevenLares/Social-media-Blocklists/master/adguard-facebook.txt`
6. Paste the URL in the Edit box and click on `Add filter`

https://kb.adguard.com/en/general/how-to-create-your-own-ad-filters#example-blocking-by-domain-name

You're done. 


# Converting hosts files to Pihole and AdGuard formats

1. Add host files into the 'input' folder.
    * Refer to the provided input files for valid formatting examples.
    * The input files may have comments and empty lines
2. Run 'python3 create_hosts.py' in a terminal.
3. The new host files can now be found in the 'output' folder.


The input files are not deleted after running the python script
The requirements.txt file is not included, since only the standard Python library is used.
