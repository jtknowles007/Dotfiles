" {{{ GENERAL SETTINGS
set nocompatible
filetype off
filetype plugin indent on
let mapleader=","
set noswapfile
syntax on
set viminfofile=NONE
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
set undodir=~/.vim/undodir
set undofile
set undolevels=10000
set undoreload=100000
" }}}
" {{{ FILE HANDLING
set backupdir=.backup/,~/.backup/,/tmp//
set undodir=.undo/,~/.undo/,/tmp//
set directory=.swp/~/.swp/,/tmp//
" }}}
" {{{ APPEARANCE 
set termguicolors
set showmatch
set matchtime=2
autocmd FileType * : ColorHighlight
let ayucolor="dark"
colorscheme ayu
hi clear SpellBad
" }}}
" {{{ INDENTATION
set tabstop=4
set expandtab
set softtabstop=4
set shiftwidth=4
set autoindent
set copyindent
set smartindent
set smarttab
" }}}
" {{{ FOLDING
set foldmethod=marker
set foldenable
set foldlevelstart=99
set viewoptions+=folds
" }}}
" {{{ SEARCH AND REPLACE
set incsearch
set hlsearch
set ignorecase
set smartcase
" }}}
" {{{ KEY MAPPING
" Map arrow keys to navigate windows
nnoremap <up> <C-W>k
nnoremap <down> <C-W>j
nnoremap <left> <C-W>h
nnoremap <right> <C-W>l

"Allow movement over displayed lines, not physical lines
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk

"Folds
nnoremap <space> za

map <F2> :s/^\(.*\)$/#\1/g<CR>
map <F3> :s/^#//g<CR>

map <Tab> <C-W>w
map <S-tab> <C-W>p
map - <C-W><Down>
" }}}
" {{{ AUTOCOMMANDS
" }}}
" {{{ CUSTOM FUNCTION
" Toggle Line Numbers
function! ToggleNumber()
	if(&relativenumber ==1)
		set norelativenumber
		set number
	else
		set relativenumber
	endif
endfunction
" }}}
" {{{ PLUGIN MANAGER (VUNDLE) 
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
" Plugin 'SirVer/ultisnips' "Custom text snippets/templates
Plugin 'vimwiki/vimwiki' "Vim based personal wiki
Plugin 'img-paste-devs/img-paste.vim' "Paste image links into vimwiki
Plugin 'iamcco/markdown-preview.nvim' "Live preview vimwiki page in browser
call vundle#end()
" }}}
" {{{ PLUGIN - ALE
let g:ale_linters={'python': ['Mypy','pylint']}
" }}}
" {{{ PLUGIN - IMAGE PASTE
let g:mdip_imgdir = 'images'
let g:mdip_imgname = 'image'
autocmd FileType markdown nmap <buffer><silent> <leader>, :call mdip#MarkdownClipboardImage()<CR>
" }}}
" {{{ PLUGIN - MARKDOWN PREVIEW
autocmd FileType markdown nmap <leader>pp :MarkdownPreviewToggle<CR>
" }}} 
" {{{ PLUGIN - NERD TREE
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
let NERDTreeShowHidden=1 "Show hidden files (1=Y, 2=N)
" }}}
" {{{ PLUGIN - VIMWIKI

" Wiki list
let g:vimwiki_list = [{'path': '~/Dropbox/vimwiki/',
            \ 'template_path': '~/.vim/vimwiki/templates',
            \ 'template_default': 'default.tpl',
            \ 'path_html': '~/wiki/',
            \ 'syntax': 'markdown',
            \ 'ext': 'md',
            \ 'name': 'Knowledge Base',
            \ 'custom_wiki2html': '~/bin/wiki2html'}]

let g:vimwiki_key_mappings = { 'table_mappings': 0, } "UltiSnips compatibility
let g:vimwiki_global_ext = 0
let g:vimwiki_auto_header = 0 "Disable automatic header based on file name
let g:vimwiki_conceal_onechar_markers = 0 "Disable conceal 1char marks
let g:vimwiki_url_maxsave = 0 "Disables keeping track of links
let g:vimwiki_links_space_char = '-' "Character used to replace spacese in links

" Hide link paths in vimwiki
set conceallevel=2
set concealcursor=n
let g:vimwiki_conceallevel = 2
let g:markdown_conceal = 2
" }}}
