# CryptoFever

## Miner in the Middle

CryptoFever is an interactive python script that use Bettercap2 to perform 
a Man In The Middle attack and inject javascript cryptonight miner on requested http/https (sslstrip) webpages
by the hosts connected to the same access point (wifi).

Bettercap2 has been rewritten in Golang (https://github.com/bettercap/bettercap) and outperform widely old Bettercap 
and all others mitm tools around.

## Scope

> setup LEGAL pay-per-use AP services

> easy way to make some crypto with YOUR devices 

> as a PROOF of concept to test on network you OWN or you've permissions

Any misuse is not under the resposibility of the developer

## Getting Started

Simply git clone or download and unzip CryptoFever folder

## Setup

### Linux

Automatic setup on first run

```
sudo python cryptofever.py 
```
or:
```
sudo chmod +x ./phantom-evasion.py

sudo ./phantom-evasion.py

```

### Osx

Automatic setup on first run

```
sudo python cryptofever.py 
```
or:
```
sudo chmod +x ./phantom-evasion.py

sudo ./phantom-evasion.py

```
 

### Windows

Manual setup required

require Go >= 1.8 

require winpcap https://github.com/bettercap/bettercap/wiki/Compilation-on-Windows

download bettercap https://github.com/bettercap/bettercap/releases/download/v2.3.1/bettercap_windows_amd64_2.3.1.zip

and extract it inside CryptoFever/lib 


## Automatic setup 

if available (actually only linux and osx) it will:

> check for the presence of Go >= 1.8
> download and extract it if not found. 
> download and compile libpcap 1.8.1
> create a symlink (sudo ln -s /usr/lib/x86_64-linux-gnu/libpcap.so.1.8.1  /usr/lib/libpcap.so.1)
> download libnetfilterqueue-dev if apt is present
> download and extract related precompiled version of bettercap2 on lib folder

TO DISABLE AUTOMATIC SETUP on First Run change the value of the var Setup inside Cryptofever/lib/config.txt

## Start Http miner injection 

inject javascript miner only on http page request 

option required:

> Interface to use

> Target mode (All connected devices,select target(targets) or select target(targets) to ignore (whitelist))

> A valid unused port to use as a http-proxy-port for bettercap2

## Start Http + sslstrip miner injection 

inject javascript miner on http page request and use sslstrip to try to downgrade https to http (injecting miner into https page) 

option required:

> Interface to use

> Target mode (All connected devices,select target(targets) or select target(targets) to ignore (whitelist))

> A valid unused port to use as a http-proxy-port for bettercap2

## Javascript Pool Miner Generator

CryptoFever is also capable to generate javascript miner (actually only webminerpool type) and will prompt the user to miner generation if the miners folder is empty (CryptoFever/js-miners). 
 
Interactive menu to set miner speed, number of threads ,miner visibilty(alertbox or hidden),mining pool,wallet address and cryptocoin to mine.

No account is required (while it require a wallet address).

List of Minable coin:

Monero (XMR),Sumokoin (SUMO),Electroneum (ETN),Turtlecoin (TRTL)

Miner generated with cryptofever include a 5% dev-donation. 

In order to use custom javascript miner move the .js file inside CryptoFever/js-miner folder and then select it on cryptofever.  


##Pre-release

for any issue or question: oddcod3@gmail.com 


## license

GPLv3.0





