# Gnosis Wagyu Key Gen

The Gnosis Chain Port of the Wagyu Key Gen is a GUI application providing functionality to the official[staking-deposit-cli](https://github.com/ethereum/staking-deposit-cli). It is a React app running in Electron.  See `src/electron/` for the simple electron app and `src/react/` for where the magic happens.

## Download the Latest Gnosis Waygu Key Gen with BLS To Execution Change (BTEC) messages at [Releases](https://github.com/vis-nova-labs/Gnosis-Wagyu-Key-Gen)

As of this writing Gnosis Chain does not act like Ethereum as far as partial/excess balance withdrawals being automatically swept every few days when the proper conditions are met. They currently must be submitted manually to sweep the key, full information is availiable in the [Gnosis Chain Withdrawal Docs](https://docs.gnosischain.com/node/management/withdrawals), please read the docs to understand how Gnosis Chain Withdrawals currently differ from Ethereum

### Previous Alpha and Beta Releases can be found [Here](https://github.com/alexpeterson91/wagyu-key-gen/releases)

### Wagyu Audit by HashCloak [Wagyu Key Gen Audit Report](https://github.com/stake-house/wagyu-key-gen/files/7693548/Wagyu.Key.Gen.Audit.Report.pdf)

- This is an audit of the upstream software used as the basis for this project.  The audit was performed by HashCloak, a third party security firm.  The audit was performed on the upstream software and not on the changes made by Vis Nova Labs to work on Gnosis Chain.

## Environment Configuration & Dependencies

Prior to running the Gnosis Wagyu Key Gen a few dependencies need to be installed.

### Ubuntu 20.04 and later

Execute all the following commands in your terminal to setup your dev environment.

```console
sudo apt install -y curl
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

sudo apt install -y build-essential nodejs git python3-distutils python3-dev

PATH="$HOME/.local/bin:$PATH"

curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install pyinstaller

sudo npm install -g yarn

git clone https://github.com/vis-nova-labs/gnosis-wagyu-key-gen
cd gnosis-wagyu-key-gen

yarn install
yarn buildcli
```

### Ubuntu 18.04

Even if Ubuntu 18.04 is somewhat old, it is a great OS to build our releases on for the Linux target because it has an older GLIBC which makes it more compatible. More details [here](https://pyinstaller.readthedocs.io/en/stable/usage.html#making-gnu-linux-apps-forward-compatible).

Execute all the following commands in your terminal to build a distribution for release.

```console
sudo apt update && sudo apt -y upgrade

sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y curl
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

sudo apt install -y python3.10-dev python3.10-distutils zlib1g-dev build-essential nodejs git

PATH="$HOME/.local/bin:$PATH"

curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
alias python3=python3.10
echo -e "\nalias python3=python3.10" >> ~/.bash_aliases
python3 get-pip.py
pip3 install pyinstaller

sudo corepack enable

git clone https://github.com/vis-nova-labs/gnosis-wagyu-key-gen
cd gnosis-wagyu-key-gen

yarn install
yarn build
yarn buildcli
yarn dist
```

### Windows 10

- Download and install Node.js and npm from [here](https://nodejs.org/en/download/) (Use LTS version and 64-bit .msi Installer).
- At the screen named *Tools for Native Modules*, make sure to check the option named *Automatically install the necessary tools.*. It will install chocolatey, Python 3 and VS build tools. Follow the instructions until the end.
- Open a command prompt window as admin (Press `⊞ Win`+`R`, type `cmd`, hold `Ctrl` + `Shift` and press `↵ Enter`)
- Execute this command to install git. Follow the instructions on screen.

```console
choco install git.install
```

- Open a normal command prompt window (Press `⊞ Win`+`R`, type `cmd` and press `↵ Enter`).
- Execute the following commands to upgrade pip, install pyinstaller, Cython, install yarn, clone the repository and install the remaining required packages.

```console
python -m pip install --upgrade --user pip
python -m pip install --user pyinstaller
python -m pip install --user Cython
set PATH=%APPDATA%\python\Python310\Scripts;%PATH%

npm install -g yarn

git clone https://github.com/vis-nova-labs/gnosis-wagyu-key-gen
cd gnosis-wagyu-key-gen

yarn install
yarn buildcliwin
```

### macOS 10.15.1 and later

Execute all the following commands in your terminal to setup your dev environment.  You may be prompted to install "command line developer tools" at some point and please do it.

```console
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/$USER/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

git --version

// If git is not found, run the following
brew install git

python3 --version
pip3 --version

// If either python3 or pip3 are not found, run the following
brew install python3

brew install node
pip3 install pyinstaller
npm install -g yarn

git clone https://github.com/vis-nova-labs/gnosis-wagyu-key-gen
cd gnosis-wagyu-key-gen

yarn install
yarn buildcli
```

## Start Wagyu Key Gen

Run the following commands in the repository directory:

- `yarn build`
  - `yarn build:watch` (will reload build on changes)
  - _In order to get them to show in the app press `ctrl+r` or `cmd+r` once the app is started.*
- `yarn start`

## To run diagnostics

To open dev tools when in the Gnosis Wagyu Key Gen use `Ctrl` + `Shift` + `I`

## Bundling

We use [electron-builder](https://www.electron.build/) to create executable bundles for Gnosis Wagyu Key Gen.  Run the following to create a bundle:

- `yarn run build`
- `yarn run buildcli` (or `yarn run buildcliwin` on Windows)
- `yarn run dist`

Your assets will be in the `dist/` folder.

## Design

Current designs can be found [here](https://github.com/gnosischain/media-kit)

## Funding

If you would like to help with funding this project's source, you can donate to their [Gitcoin grant](https://gitcoin.co/grants/2112/stakehouse-wagyu-tooling-suite-easy-to-use-tools-) or you can send your funds directly to `wagyutools.eth`.

Donations for this Gnosis Chain fork of the Wagyu Key Gen by Vis Nova Labs can be sent to `VisNova.eth`.

## Support

Support for this project can currently be found on the [Dappnode Discord Server](https://discord.gg/dappnode) in the Gnosis Beacon Chain channel.

Reach out to the EthStaker community:

- on [discord](https://discord.io/ethstaker)
- on [reddit](https://www.reddit.com/r/ethstaker/)

## License

[GPL-3.0](LICENSE)
