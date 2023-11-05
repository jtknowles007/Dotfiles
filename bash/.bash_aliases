alias cls='clear'
alias l1='ls -1' #Display contents of directory with no additional info one file per line
alias ll='ls -lhFA' #Display current directory listing in long format.  Include hidden directories
alias la='ls -A' 
alias l='ls -CF' #Display in columns with file type indicator
alias lq='ls -Q' #Print contents of directory to STDOUT enclosed by double quotes.
alias lsl='ls -lhFA | less' #Pipe output of ls to less for viewing large directory listings
alias cd..='cd ..' #Change directory even if you forget the space
alias ..='cd ..' #Move up one directory with double elipses
alias ...='cd ../..' #Move up two directories with triple elipses
alias histg='history | grep' #Quickly search through command history histg [keyword]
alias grep='grep --color=auto' #Add color to grep output
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


	
