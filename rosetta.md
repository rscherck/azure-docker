Set up rosetta terminal for i386 in vscode
https://dev.to/markwitt_me/creating-a-custom-vscode-terminal-profile-for-using-rosetta-on-an-m1-mac-apple-silicon-2gb2
arch

https://medium.com/mkdir-awesome/how-to-install-x86-64-homebrew-packages-on-apple-m1-macbook-54ba295230f

https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cportal%2Cv2%2Cbash&pivots=programming-language-python

vim ~/.zshrc

# rosetta terminal setup

if [ $(arch) = "i386" ]; then
alias python86="/usr/local/homebrew/bin/python3.10"
alias brew86='/usr/local/homebrew/bin/brew'
alias pyenv86="arch -x86_64 pyenv"
alias func86="/usr/local/homebrew/bin/func"
fi

python86 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

func86 init --python
func86 new --name HttpExample --template "HTTP trigger" --authlevel "anonymous"
func86 start

http://localhost:7071/api/HttpExample
http://localhost:7071/api/HttpExample?name=richard

func86 new
option 12 -> Queue Storage Trigger
name it
