# Main keymap 
bindkey -v
bindkey '^p' history-search-backward
bindkey '^n' history-search-forward

# Completion
zmodload zsh/complist
autoload -U compinit; compinit

# Path
export PATH="$PATH:/home/john/.local/bin/:/snap/bin:/home/john/bin/"

# Aliases
source $HOME/.aliases

# History
HISTFILE=~/.histfile
HISTSIZE=5000
SAVEHIST=$HISTSIZE
HISTDUP=erase


# Shell options - man zshoptions
setopt AUTO_CD
setopt HASH_LIST_ALL
setopt CORRECT
setopt CDABLE_VARS

setopt MENU_COMPLETE
setopt AUTO_LIST
setopt COMPLETE_IN_WORD

setopt EXTENDED_HISTORY
setopt SHARE_HISTORY
setopt APPEND_HISTORY
setopt HIST_EXPIRE_DUPS_FIRST
setopt HIST_IGNORE_SPACE
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_SAVE_NO_DUPS
setopt HIST_IGNORE_DUPS
setopt HIST_FIND_NO_DUPS
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

# Define completers
zstyle ':completion:*' completer _extensions _complete _approximate

#Use cache for commands using cache
zstyle '"completion:*' use-cache on
zstyle ':completion:*' cache-path "$XDG_CACHE_HOME/zsh/.zcompcache"

#Complete the alias when _expand_alias is used as a function
zstyle ':completion:*' complete true

# Allow you to select in a menu
zstyle ':completion:*' menu select

# Autocomplete options for cd instead of directory stack
zstyle ':completion:*' complete-options true
zstyle ':completion:*' file-sort modification

zstyle ':completion:*:*:*:*:corrections' format '%F{yellow}!- %d (errors: %e) -!%f'
zstyle ':completion:*:*:*:*:descriptions' format '%F{blue}-- %D %d --%f'
zstyle ':completion:*:*:*:*:messages' format ' %F{purple} -- %d --%f'
zstyle ':completion:*:*:*:*:warnings' format ' %F{red}-- no matches found --%f'

# Colors for files and directories
zstyle ':completion:*:*:*:*:default' list-colors "${(s.:.)LS_COLORS}"

# Only display some tags for the cd command
zstyle ':completion:*:*:cd:*' tag-order local-directories directory-stack path-directories

# Required for completion to be in good groups (named after the tags)
zstyle ':completion:*' group-name ''
zstyle ':completion:*:*:-command-:*:*' group-order aliases builtins functions commands 

# Completion matching control
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' keep-prefix true

zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls $realpath'
zstyle :compinstall filename '/home/john/.zshrc'
autoload -Uz compinit

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
PROMPT='%F{#008000}[%n@%M]%f %F{11}%~%f %F{yellow}${vcs_info_msg_0_}%f %F{11}%# %f'
RPROMPT=''

# Remap LS_COLORS
eval "$(dircolors ~/.dircolors)"
