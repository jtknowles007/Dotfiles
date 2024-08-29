set nocompatible
filetype off
let mapleader=","

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim' "Enable Vundle plugin manager
Plugin 'preservim/nerdtree' "A tree explorer for vim
Plugin 'dense-analysis/ale' "Linting (syntax checking and semantic errors)
Plugin 'tpope/vim-fugitive' "Git plugin
Plugin 'itchyny/vim-gitbranch' "Returns name of git branch
Plugin 'airblade/vim-gitgutter' "Shows git diff in the sign column
Plugin 'davidhalter/jedi-vim' "Python autocompletion
Plugin 'chrisbra/Colorizer' "Colorize color definitions
call vundle#end()
filetype plugin indent on
 
set termguicolors
let ayucolor="dark"
colorscheme ayu
set noswapfile
syntax on
set viminfofile=NONE
set tabstop=4
set expandtab
set softtabstop=4
set shiftwidth=4
set autoindent
set copyindent
set smartindent
set smarttab
set backspace=indent,eol,start
set nolist
set encoding=utf-8
set fileencoding=utf-8
set termencoding=utf-8
set ttimeoutlen=10
set visualbell
set noerrorbells
set number
set signcolumn=yes
set ruler
set hidden
set encoding=utf-8
set showcmd
set laststatus=2
set cmdheight=2
set lazyredraw
set showmatch
set showmode
set confirm
set undolevels=1000
set shell=bash
set updatetime=250
set spell
set ttyfast
set buftype=""
set clipboard=unnamedplus
set completeopt=noinsert,menuone,noselect
set mouse=a
set splitbelow splitright
set title
set ignorecase
set smartcase
set incsearch
set hlsearch
set foldmethod=indent
set foldenable
set foldlevelstart=10
set undodir=~/.vim/undodir
set undofile
set undolevels=10000
set undoreload=100000
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk
nnoremap <space> za
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
map <F2> :s/^\(.*\)$/#\1/g<CR>
map <F3> :s/^#//g<CR>
hi clear SpellBad

set backupdir=.backup/,~/.backup/,/tmp//
set undodir=.undo/,~/.undo/,/tmp//
set directory=.swp/~/.swp/,/tmp//

function! ToggleNumber()
	if(&relativenumber ==1)
		set norelativenumber
		set number
	else
		set relativenumber
	endif
endfunction
autocmd FileType * : ColorHighlight
let g:ale_linters={'python': ['Mypy','pylint']}
