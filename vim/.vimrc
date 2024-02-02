" GENERAL
set nocompatible
set noswapfile
filetype off
filetype indent on
set viminfofile=NONE
syntax on

" SPACES TABS AND SPECIAL CHARACTERS
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

" UI CONFIG
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

" PLUGIN MANAGER
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'python-mode/python-mode'
Plugin 'dense-analysis/ale'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'davidhalter/jedi-vim'


call vundle#end()
filetype plugin indent on

" SEARCH
set ignorecase
set smartcase
set incsearch
set hlsearch

" FOLDING
set foldmethod=indent
set foldenable
set foldlevelstart=10

" CUSTOM LEADER
let mapleader=","

" NAVIGATE SPLITS WITH ARROW KEYS
map <up> <C-w><up>
map <down> <C-w><down>
map <left> <C-w><left>
map <right> <C-w><right>

" NAVIGATE BY DISPLAY LINE NOT PHYSICAL LINE
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk

" FOLDING
nnoremap <space> za

" CUSTOM FUNCTION MAPPING
nnoremap <leader>l :call ToggleNumber()<CR>
nnoremap <leader>w :set list!<CR>
nnoremap <leader>s :set spell!<CR>

" COMMENT BLOCK
map <F2> :s/^\(.*\)$/#\1/g<CR>
map <F3> :s/^#//g<CR>

" HIGHLIGHTING
hi clear SpellBad
hi SpellBad cterm=underline,bold, ctermfg=red

" SAVE LOCATIONS
set backupdir=.backup/,~/.backup/,/tmp//
set undodir=.undo/,~/.undo/,/tmp//
set directory=.swp/~/.swp/,/tmp//

" CUSTOM FUNCTIONS
function! ToggleNumber()
	if(&relativenumber ==1)
		set norelativenumber
		set number
	else
		set relativenumber
	endif
endfunction
