#!/bin/zsh

import argparse

"""
- SED
- AWK
- RSYNC
- SCP
- WHICH
- FIND
- LOCATE
- FFUF
- WFUZZ
- OPENSSL
- Hashcat
- Hydra
- John the ripper
- Hashid

"""

def sed():
    sed_text = """

░██████╗███████╗██████╗░
██╔════╝██╔════╝██╔══██╗
╚█████╗░█████╗░░██║░░██║
░╚═══██╗██╔══╝░░██║░░██║
██████╔╝███████╗██████╔╝
╚═════╝░╚══════╝╚═════╝░

===================
\033[30;42;5m [!] Important flags  \033[m
===================
GLOBAL FLAGS:
   -i   Edit file in-place
   -g   Allow multiple commands in a single execution

COMMAND FLAGS:
    s	Substitute (Replace) text	sed 's/foo/bar/' file.txt
    g	Global replacement (replace all in a line)	sed 's/foo/bar/g' file.txt
    I	Case-insensitive replacement	sed 's/foo/bar/Ig' file.txt
    p	Print matching lines (use with -n)	sed -n '/error/p' file.txt
    d	Delete matching lines	sed '/debug/d' file.txt
    !	Negate a command (apply to non-matching lines)	sed '/critical/!d' file.txt
    y	Transform characters (like tr)	sed 'y/abc/XYZ/' file.txt
    q	Quit after first match


    
\033[30;42;3m Replace occurrences of a string in a file - case sensitve \033[m
=> sed -i '' 's/old-text/new-text/' file.txt

\033[30;42;3m Replace occurrences of a string in a file - case insensitve \033[m
=> sed -i '' 's/old-text/new-text/I' file.txt

\033[30;42;3m Print only specific lines: \033[m
=> sed -n '3p' file.txt

\033[30;42;3m Print a range of lines: \033[m
=> sed -n '2,5p' file.txt

\033[30;42;3m Delete empty lines: \033[m
=> sed -i '' '/^$/d' file.txt

\033[30;42;3m Chain multiple replacements / replace multiple words in a file \033[m
=> sed -i '' -e 's/word1/replacement1/g' -e 's/word2/replacement2/g' file.txt

\033[30;42;3m Convert lowercase to uppercase: \033[m
=> sed -i '' 'y/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/' file.txt


"""
    print(sed_text)

##############################################################################################################################

def ffuf():
    ffuf_text = """

███████╗███████╗██╗░░░██╗███████╗
██╔════╝██╔════╝██║░░░██║██╔════╝
█████╗░░█████╗░░██║░░░██║█████╗░░
██╔══╝░░██╔══╝░░██║░░░██║██╔══╝░░
██║░░░░░██║░░░░░╚██████╔╝██║░░░░░
╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░░░░

===================
\033[30;42;5m [!] Important flags  \033[m
===================
MATCHER OPTIONS:
    -mc    Match HTTP status codes, or "all" for everything. (default: 200-299,301,302,307,401,403,405,500)
    -mr    Match regexp
    -ms    Match HTTP response size

    FILTER OPTIONS:
    -fc    Filter HTTP status codes from response. Comma separated list of codes and ranges
    -fr    Filter regexp
    -fs    Filter HTTP response size. Comma separated list of sizes and ranges

==========================
\033[30;42;5m [!] Attack Types available \033[m
==========================

[1] Clusterbomb (Default) : FFUF will use first word from wordlist 1 and then all words from wordlist 2 (Basically all combinations)
[2] Pitchfork : FFUF will use the words sequentially: the first word in the username list with the first in the password list.

============================
\033[30;42;5m [>>>] Via URL in commandline \033[m
============================

\033[30;42;3m 1) Enumerate directories in a URL: \033[m
=> ffuf -u http://Target-URL/FUZZ -w wordlist.txt

\033[30;42;3m 2) Enumerate files in a URL: \033[m
=> ffuf -u http://Target-URL/FUZZ -w wordlist.txt -e .php,.html,.txt

\033[30;42;3m 3) Enumerate subdomains in a URL: \033[m
=> ffuf -u http://FUZZ.mydomain.com -w wordlist.txt

\033[30;42;3m 4) Find pre-existing usernames: \033[m
=> ffuf -w usernames_wordlist.txt -X POST -d "username=FUZZ&&password=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://mydomain.com/login -mr "username already exists"

\033[30;42;3m 5) Enumerate multiple subdomains: (Clusterbomb) (no need to specify using -mode, clusterbomb is default) \033[m
=> ffuf -u https://W2/W1 -w ./wordlist1.txt:W1,./wordlist2.txt:W2
=> ffuf -u http://example.com/FUZZ1/FUZZ2 -w /path/to/wordlist1:FUZZ1 -w /path/to/wordlist2:FUZZ2

\033[30;42;3m 6) Enumerate multiple subdomains: (Pitchfork) \033[m
=> ffuf -u http://targetwebsite.com -w /path/to/list/username.txt:FUZZ1 -w /path/to/list/password.txt:FUZZ2 -mode pitchfork

[>>>] Via HTTP Request in a file

\033[30;42;3m 1) via request file  \033[m
=> ffuf -request request.txt -request-proto http -mode clusterbomb -w /path/to/users/file.txt:USERFUZZ -w /path/to/password/file.txt:PASSFUZZ -mc 200


=> Request.txt file

POST /login HTTP/1.1
Host: 10.10.10.10
Content-Length: 37
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36
Content-Type: application/json
Origin: http://10.10.10.10
Referer: http://10.10.10.10/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"username":"USERFUZZ","password":"PASSFUZZ"}
     
"""
    print(ffuf_text)

##############################################################################################################################

def awk():
    awk_text="""
░█████╗░░██╗░░░░░░░██╗██╗░░██╗
██╔══██╗░██║░░██╗░░██║██║░██╔╝
███████║░╚██╗████╗██╔╝█████═╝░
██╔══██║░░████╔═████║░██╔═██╗░
██║░░██║░░╚██╔╝░╚██╔╝░██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝

\033[30;42;3m To print contents of a file \033[m
=> awk '{print $0}' <file_name>

\033[30;42;3m To print line number before every line \033[m
=> awk '{print NR, $0}' <file_name>

\033[30;42;3m To print specific columns \033[m
=> awk '{print $column_no }' <file_name>
(The way awk determines where each column starts and ends is with a space, by default.)

\033[30;42;3m To print the lines which match the given pattern. \033[m
=> awk '/string/ {print}' <file_name>

\033[30;42;5m [!] Important flags  \033[m
 - NR : Line Number
 - NF : Last field
=> awk '{print $0, $NF}' <file_name>


"""
    print(awk_text)


def rsync():
    pass

def scp():
    pass

def which():
    pass

def find():
    pass

def wfuzz():
    pass

def openssl():
    pass

def hashcat():
    pass

def hydra():
    pass

def johntheripper():
    pass

def hashid():
    pass

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="A Kali helper to help you with command syntax")

    # Add command-line arguments
    #parser.add_argument('-f', '--flag', action='store_true', help="A boolean flag")
    #parser.add_argument('-n', '--number', type=int, default=42, help="An integer argument (default: 42)")
    parser.add_argument('-c', '--command', type=str, help="A command argument")
    
    # Parse the arguments
    args = parser.parse_args()
    command_dictionary={'ffuf':ffuf,'sed':sed, 'awk':awk, 'rsync':rsync, 'scp':scp, 'which':which, 'find':find, 'wfuzz':wfuzz, 'openssl':openssl, 'hashcat':hashcat, 'hydra':hydra, 'johntheripper':johntheripper, 'hashid':hashid }

    
    command_dictionary[args.command]()

    #if args.string:
    #    print(f"String is: {args.string}")
if __name__ == "__main__":
    main()
