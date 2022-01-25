[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

```
--==================================================--

 _______ ___. ___________                  .__
 \      \\_ |_\__    ___/__________  _____ |__|__  ___
 /   |   \| __ \|    |_/ __ \_  __ \/     \|  \  \/  /
/    |    \ \_\ \    |\  ___/|  | \/  Y Y  \  |>    <
\____|__  /___  /____| \___  >__|  |__|_|  /__/__/\_ \
        \/    \/           \/            \/         \/

      -| Jupyter Kernels at Your Terminal |-

--==================================================--
```
![NBTERMIX SCREEN](https://raw.githubusercontent.com/mtatton/nbtermix/master/nbtermix.png)

Let you view, edit and execute Jupyter Notebooks in the terminal.

## Install

Using pip:

```
pip3 install jupyter_client ipykernel nbtermix
```
## Usage

Open an interactive notebook:

```
$ nbtermix foo.ipynb
```

Run a notebook in batch mode:

```
$ nbtermix --run foo.ipynb
```

## Quickstart

1] execute: nbtermix foo.ipynb

2] There should be notebook ready for You to use

3] ctrl+o to open current cell in external editor

4] type Your python expression, function etc. (like 1+1)

5] press enter to execute current cell

6] type key b to insert cell below

7] repeat from step 3 to continue

For more information type ctrl+h

Hints:

* Using j,k will help You to focus to next, previous cells
* ctrl+f will bring current cell to the top of the screen
* ctrl+s will save current workbook
* nbtermix --fold foo.ipynb - will open the notebook and fold cells
* export EDITOR=vi will use vi for cells editing in external mode
* e will enter current cell for editing, escpe will return to comand mode

## Key bindings

There are two modes: edit mode, and command mode.
- `e`: enter the edit mode, allowing to type into the cell.
- `esc`: exit the edit mode and enter the command mode.

In edit mode:
- `ctrl-e`: run cell.
- `ctrl-r`: run cell and select below in edit mode.
- `ctrl-o`: open cell in external editor.
- `ctrl-t`: open cell result in external editor.
- `ctrl-f`: save tmp file from cell and execute it.
- `ctrl-s`: save.

In command mode:

- `up` or `k`: select cell above.
- `down` or `j`: select cell below.
- `ctrl-f`: current cell to the top.
- `ctrl-g`: go to last cell.
- `gg`: go to first cell.
- `ctrl-up`: move cell above.
- `ctrl-down`: move cell below.
- `right` : scroll output right
- `left` : scroll output left
- `c-j` : scroll output down
- `c-k` : scroll output up
- `ctrl-b` : reset output scroll shift
- `a`: insert cell above.
- `b`: insert cell below.
- `x`: cut the cell.
- `c`: copy the cell.
- `ctrl-v`: paste cell above.
- `v`: paste cell below.
- `o`: set as code cell.
- `r`: set as Markdown cell.
- `l`: clear cell outputs.
- `ctrl-l`: clear all cell outputs.
- `f`: fold current cell input.
- `/`: Search.
- `n`: Repeat last search.
- `N`: Search backwards.
- `m`,`<any>`: Set mark <key>.
- `'`,`<any>`: Go to mark <key>.
- `ctrl-e` or `enter`: run cell.
- `ctrl-f` : focus current cell.
- `ctrl-r` or `alt-enter`: run cell and select below.
- `ctrl-s`: save.
- `ctrl-p`: run all cells.
- `ctrl-q`: exit.
- `ctrl-h`: show help.


## Kernels

For more kernels visit:

![Jupyter kernels . jupyter/jupyter Wiki](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

This nbtermix is tested on (install only if You know what You're doing):

### c kernel

```
pip install jupyter-c-kernel
install_c_kernel
```

### java kernel

```
wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip
unzip ijava-1.3.0.zip -d ijava
cd ijava
python install.py
apt-get isntall default-jdk
```

### javascript kernel

```
apt-get install nodejs npm libczmq-dev
npm install -g --unsafe-perm npm
npm install -g --unsafe-perm ijavascript
ijsinstall --install=global
```

### php kernel

```
apt-get install php composer php-zmq
wget https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar
chmod u+x jupyter-php-installer.phar
./jupyter-php-installer.phar install
```

### sqlite kernel from sqlok

```
pip3 install sqli-kernel
sqlik_install
```

### python3 kernel

```
out of the box
```

## Testing environment

on Debian X using Python 3.7 
(with kernel.json patch see Troubleshooting)

```
$ jupyter --version:

IPython          : 7.31.0
ipykernel        : 6.6.1
jupyter_client   : 7.1.0
jupyter_core     : 4.9.1
traitlets        : 5.1.1

```

## Runtime Environment recommendations


Keep separated environment for the nbtermix

```
|= mkdir -p ~/pyenv
cd ~/pyenv
|= virtualenv -p /usr/bin/python3.9 nbtermix
|= source ~/pyenv/nbtermix/bin/activate
```

## CHANGELOG

```
minor changes in v.0.1.4 by mtatton
* added ! keyboard shortcut to go to
  external editor from command mode
* when there was a cell edit in
  external editor the cell didn't
  refresh
minor changes to v.0.1.3  by mtatton
+ fixed search function (keys /,n,N)
minor changes to v.0.1.2  by mtatton
+ changed visible cells display a bit
+ added ctrl + f for current cell focus
+ added raw text/plain display 
+ added raw text/html display 
minor changes to v.0.0.18 by mtatton
+ scrollable output using left and right
minor changes to v.0.0.17 by mtatton
minor changes to v.0.0.16 by mtatton
minor changes to v.0.0.15 by mtatton
+ added folding for terminal space saving
+ renamed to nbtermix
minor changes to v.0.0.14 by mtatton
minor changes to v.0.0.13 by mtatton
minor changes to v.0.0.12 by mtatton
```
## TROUBLESHOOTING

### Problem: Python (busy) and nothing happens

Solution: Verify if python3 kernel is called

list python3 kernel location

$ jupyter kernelspec list

Find kernel.json in the destination (e.g.):

python3|/usr/local/share/jupyter/kernels/python3

In case Your system has both Python 2.7 and 3.x the 
nbtermix tries to run Python 2.7. And that's something 
that doesn't work. 

Ensure in Your kernel.json for python3 the argv is python3:
```
cat /usr/local/share/jupyter/kernels/python3/kernel.json
{
"argv": [
*"python3"*,
"-m",
"ipykernel_launcher",
... etc.
```

### Problem: On Debian 11 there is no /usr/bin/python binary

In case You are sure there is no Python 2.x installed
on Your machine. You can prepare the binary by updating
the default /usr/bin/python alternative. You can do this
as follows:

```update-alternatives --install /usr/bin/python python /usr/bin/python3.9 2```

