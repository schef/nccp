# nccp
neovim copy - clipboard paste

It's a python script that copyes lines from neovim buffer and pastes it to the clipboard.

### Typical usage scenario:
  Paste lines to some interactive console like python REPL, gatttool, SQL cli. Text editor like vim is better for prepering lines using regex, macros and manual editing.

### Dependencies
* neovim
* python3
* xdotool
* xsel

Look at <https://github.com/neovim/python-client> for more information on how to setup python with nvim.

### Usage

Start a new terminal with neovim instance
`NVIM_LISTEN_ADDRESS=/tmp/nvim nvim`

In a new terminal start `nccp.py` script.
You will be asked for start line and end line.
Press any key and position the mouse.
You have a start delay of 3 seconds and 0.8 seconds delay for between lines. You can edit those in the file.

