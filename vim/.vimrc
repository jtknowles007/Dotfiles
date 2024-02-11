if has('packages')
    let package_dir = '~/.vim/pack/plugins/start'
    packadd! lightline
    packadd! ale
    packadd! indentpython.vim
    packadd! vim-fugitive
    packadd! jedi-vim
    packadd! vim-gitbranch
    packadd! vim-gitgutter
    packadd! lightline-ale
endif
packloadall

set noswapfile
filetype plugin indent on
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
let mapleader=","
highlight ColorColumn ctermbg=233 ctermfg=93
let &colorcolumn="80,".join(range(120,999),",")
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk
nnoremap <space> za
map <F2> :s/^\(.*\)$/#\1/g<CR>
map <F3> :s/^#//g<CR>
hi clear SpellBad
hi SpellBad cterm=underline,bold, ctermfg=red
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
let g:ale_linters={'python': ['Mypy','pylint']}
let g:lightline = {}

let g:lightline.component_expand = {
      \  'linter_checking': 'lightline#ale#checking',
      \  'linter_infos': 'lightline#ale#infos',
      \  'linter_warnings': 'lightline#ale#warnings',
      \  'linter_errors': 'lightline#ale#errors',
      \  'linter_ok': 'lightline#ale#ok',
      \ }

let g:lightline.component_type = {
      \     'linter_checking': 'right',
      \     'linter_infos': 'right',
      \     'linter_warnings': 'warning',
      \     'linter_errors': 'error',
      \     'linter_ok': 'right',
      \ }

let g:lightline.active = {
            \ 'right': [ [ 'linter_checking', 'linter_errors', 'linter_warnings', 'linter_infos', 'linter_ok' ],
            \            [ 'lineinfo' ],
	        \            [ 'fileformat', 'fileencoding', 'filetype'] ],
            \ 'left': [ ['mode','paste' ],
            \ [ 'gitbranch', 'readonly', 'filename', 'modified' ]]
            \ }

let g:lightline.component_function = {'gitbranch':'gitbranch#name'}
