#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'belyaev.rs@live.ru'

import os

print('##############################################')
print('# Установить powerline и необходимые шрифты? #')
print('##############################################')
install = input('Y/n: ')

if install != 'n':
    os.system('/usr/bin/sudo pacman -S python-pip git wget')
    os.system('pip install git+git://github.com/Lokaltog/powerline')
    os.system('wget https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf')
    os.system('wget https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf')
    os.system('mv PowerlineSymbols.otf /usr/share/fonts/')
    os.system('fc-cache -vf')
    os.system('mv 10-powerline-symbols.conf /etc/fonts/conf.d/')

print('#####################################')
print('# Куда добавить поддержу powerline? #')
print('#            1 - zsh                #')
print('#            2 - bash               #')
print('#            3 - vim                #')
print('#            4 - Во все             #')
print('#####################################')
choice = input('1/2/3/4: ')

home = os.getenv('HOME')

if choice == '1' or choice == '4':
    with open(home + '/.zshrc', 'a') as zshrc:
        zshrc.write('''\nif [[ -r /usr/lib/python3.3/site-packages/powerline/bindings/zsh/powerline.zsh ]]; then
    source /usr/lib/python3.3/site-packages/powerline/bindings/zsh/powerline.zsh
fi\n''')
        zshrc.close()

if choice == '2' or choice == '4':
    with open(home + '/.bashrc', 'a') as bashrc:
        bashrc.write('''\nif [[ -r /usr/lib/python3.3/site-packages/powerline/bindings/bash/powerline.sh ]]; then
    source /usr/lib/python3.3/site-packages/powerline/bindings/bash/powerline.sh
fi\n''')
        bashrc.close()

if choice == '3' or choice == '4':
    print('##########################################')
    print('# Установка в GVIM или компиляция клона? #')
    print('#         1 - gvim                       #')
    print('#         2 - скомпилировать клон        #')
    print('##########################################')
    vimchoice = input('1/2: ')

    if vimchoice == '1':
        checkgvim = os.system('pacman -Q gvim')
        if checkgvim != 0:
            print('###########################################')
            print('# Установить GVIM или компилировать клон? #')
            print('#         1 - установить gvim             #')
            print('#         2 - скомпилировать клон         #')
            print('###########################################')
            vimchoice = input('1/2: ')

            if vimchoice == '1':
                os.system('/usr/bin/sudo pacman -S gvim')

    if vimchoice == '2':
        print('################################################################################')
        print('# Скомпилировать VIM с поддержкой python 3.3? (необходимо для powerline)       #')
        print('# Чтобы не было конфликтов с официальным VIM будет создана программа-клон      #')
        print('# Для использования VIM с поддержкой python3.3 будет назначена команда "vimpy" #')
        print('################################################################################')
        vim = input('Y/n: ')
        if vim != 'n':
            os.system('wget ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2')
            os.system('tar xvjf vim-7.4.tar.bz2')
            os.system('cd vim74/ && ./configure --enable-python3interp --enable-rubyinterp --enable-gui=no --without-x --enable-cscope --enable-multibyte --prefix=/usr')
            os.system('cd vim74/ && make')
            os.system('/usr/bin/sudo mkdir /usr/local/bin/vimpy')
            os.system('/usr/bin/sudo cp -R vim74/src/* /usr/local/bin/vimpy')
            os.system('rm vim-7.4.tar.bz2 && rm -R vim74/')
            with open(home + '/.zshenv', 'a') as zshenv:
                zshenv.write('\nalias vimpy="/usr/local/bin/vimpy/vim"\n')
                zshenv.close()
            with open(home + '/.bashrc', 'a') as bashrc:
                bashrc.write('\nalias vimpy="/usr/local/bin/vimpy/vim"\n')
                bashrc.close()

    with open(home + '/.vimrc', 'a') as vimrc:
        vimrc.write('''\nset rtp+=/usr/lib/python3.3/site-packages/powerline/bindings/vim/
set laststatus=2
" Использовать 256 цветов (Только если ваш терминал поддерживает 256 цветов)
set t_Co=256\n''')
        vimrc.close()

print('Всё готово! =)')
