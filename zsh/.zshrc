# Main keymap 
bindkey -v

# Path
export PATH="$PATH:/home/john/.local/bin/:/snap/bin:/home/john/bin/"

# Aliases
source $HOME/.aliases


# History
HISTFILE=~/.histfile
HISTSIZE=5000
SAVEHIST=$HISTSIZE
HISTDUP=erase

# Remap LS_COLORS
#LS_COLORS=':*.tmp=00;31:*.old=00;31:fi=01;33:*.swp=00;32:*.heic=01;35:*.pdf=01;30:*.xmp=00;31:*.theme=00;33:*.mp4=00;36'
#export LS_COLORS

# Shell options
bindkey '^p' history-search-backward
bindkey '^n' history-search-forward
setopt autocd
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls $realpath'
#

# The following plugin sections come from u/colemaker360 at https://www.reddit.com/r/zsh/comments/dlmf7r/manually_setup_plugins/

# Plugins from github only
github_plugins=(
    MichaelAquilina/zsh-you-should-use
    rupa/z
)

# Plugin clone/load script
for plugin in $github_plugins; do
  if [[ ! -d ${ZDOTDIR:-$HOME}/.zsh_plugins/$plugin ]]; then
    mkdir -p ${ZDOTDIR:-$HOME}/.zsh_plugins/${plugin%/*}
    git clone --depth 1 --recursive https://github.com/$plugin.git ${ZDOTDIR:-$HOME}/.zsh_plugins/$plugin
  fi
  for initscript in ${plugin#*/}.zsh ${plugin#*/}.plugin.zsh ${plugin#*/}.sh; do
    if [[ -f ${ZDOTDIR:-$HOME}/.zsh_plugins/$plugin/$initscript ]]; then
      source ${ZDOTDIR:-$HOME}/.zsh_plugins/$plugin/$initscript
      break
    fi
  done
done

# Plugin clean up
unset github_plugins
unset plugin
unset initscript

# Completion
zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|[._-]=* r:|=*'
zstyle ':completion:*' menu select=1
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle :compinstall filename '/home/john/.zshrc'
autoload -Uz compinit
compinit

# Version control
autoload -Uz add-zsh-hook vcs_info
setopt prompt_subst
add-zsh-hook precmd vcs_info

zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' unstagedstr ' *'
zstyle ':vcs_info:*' stagedstr ' +'
zstyle ':vcs_info:git:*' formats       '(%b%u%c)'
zstyle ':vcs_info:git:*' actionformats '(%b|%a%u%c)'
setopt PROMPT_SUBST

# Prompt
PROMPT='%F{12}[%n@%M]%f %F{11}%~%f %F{yellow}${vcs_info_msg_0_}%f %F{11}%# %f'
RPROMPT=''

eval "$(dircolors ~/.dircolors)"
