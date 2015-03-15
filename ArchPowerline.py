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
    os.system('/usr/bin/sudo pip install git+git://github.com/powerline/powerline')
    os.system('wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf')
    os.system('wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf')
    os.system('/usr/bin/sudo mv PowerlineSymbols.otf /usr/share/fonts/')
    os.system('/usr/bin/sudo fc-cache -vf')
    os.system('/usr/bin/sudo mv 10-powerline-symbols.conf /etc/fonts/conf.d/')

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
        zshrc.write('''\nif [[ -r /usr/lib/python3.4/site-packages/powerline/bindings/zsh/powerline.zsh ]]; then
    source /usr/lib/python3.4/site-packages/powerline/bindings/zsh/powerline.zsh
fi\n''')
        zshrc.close()

if choice == '2' or choice == '4':
    with open(home + '/.bashrc', 'a') as bashrc:
        bashrc.write('''\nif [[ -r /usr/lib/python3.4/site-packages/powerline/bindings/bash/powerline.sh ]]; then
    source /usr/lib/python3.4/site-packages/powerline/bindings/bash/powerline.sh
fi\n''')
        bashrc.close()

if choice == '3' or choice == '4':
    print('###################')
    print('# Установка в VIM? #')
    print('#     1 - да      #')
    print('#     2 - нет     #')
    print('###################')
    vimchoice = input('1/2: ')

    if vimchoice == '1':
        checkgvim = os.system('pacman -Q vim')
        if checkgvim != 0:
            print('##################')
            print('# Установить VIM? #')
            print('#     1 - да     #')
            print('#     2 - нет     #')
            print('##################')
            vimchoice = input('1/2: ')

            if vimchoice == '1':
                os.system('/usr/bin/sudo pacman -S vim')

    with open(home + '/.vimrc', 'a') as vimrc:
        vimrc.write('''\nset rtp+=/usr/lib/python3.4/site-packages/powerline/bindings/vim/
set laststatus=2
" Использовать 256 цветов (Только если ваш терминал поддерживает 256 цветов)
set t_Co=256\n''')
        vimrc.close()

print('Всё готово! =)')
