alias cls='clear'
alias ls='ls -A --color=auto'
alias ll='ls -lhFA' #Display current directory listing in long format.  Include hidden directories
alias cd..='cd ..' #Change directory even if you forget the space
alias ..='cd ..' #Move up one directory with double elipses
alias ...='cd ../..' #Move up two directories with triple elipses
alias grep='grep --color=auto' #Add color to grep output
alias histg='history | grep' #Quickly search through command history histg [keyword]
alias svim='sudo vim'
alias install='sudo apt install'
alias remove='sudo apt remove'
alias update='sudo apt update'
alias upgrade='sudo apt update && sudo apt upgrade'
alias upgradable='sudo apt list --upgradable'
alias reboot='sudo shotdown -r now'
alias shutdown='sudo shutdown -h now'
alias open='xdg-open'

alias reloadbashrc='source ~/.bashrc' #Reload .bashrc file
function mcd {
	mkdir -p $1
	cd $1
} #Make directory and cd directly into it.  mcd [foldername]
function cl() { cd "$@" && la;} #Change directory to [foldername] and list all contents. cdla [foldername]
alias count='find . -type f | wc -l'


	
