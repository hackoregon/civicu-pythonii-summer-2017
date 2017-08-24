

```python
import sys
import os

```


```python
os.environ
```




    environ({'WINDOWID': '69206022', 'XDG_SESSION_TYPE': 'x11', 'PROJECT_HOME': '/home/hobs/src', 'CLUTTER_IM_MODULE': 'xim', 'XMODIFIERS': '@im=ibus', 'XDG_CURRENT_DESKTOP': 'Unity:Unity7', 'GDFONTPATH': '/usr/share/fonts/truetype/ttf-dejavu', 'MANAGERPID': '1480', 'GNOME_SESSION_XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'IM_CONFIG_PHASE': '1', 'PROMPT_COMMAND': 'DATETIMESTAMP=$(history 1 | cut -c -27); echo "${DATETIMESTAMP}# cd $PWD" >> $HISTORY_PATH; history -a; history -c; history -r; history 1 >> /home/hobs/.bash_history_forever; ', 'MPLBACKEND': 'module://ipykernel.pylab.backend_inline', 'EDITOR': 'nano', 'PATH': '/home/hobs/.virtualenvs/civicu/bin:/home/hobs/.virtualenvs/civicu/bin:.:/usr/local/bin/:/home/hobs/bin:/home/hobs/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 'OLDPWD': '/home/hobs', 'USER': 'hobs', 'COLORTERM': 'truecolor', 'SESSION_MANAGER': 'local/spectre:@/tmp/.ICE-unix/1805,unix/spectre:/tmp/.ICE-unix/1805', 'SHLVL': '2', 'GDMSESSION': 'ubuntu', 'GDM_LANG': 'en_US', 'XDG_MENU_PREFIX': 'gnome-', 'PAGER': 'cat', 'DISPLAY': ':0', 'COMPIZ_BIN_PATH': '/usr/bin/', 'TERM': 'xterm-color', 'HOME': '/home/hobs', '_': '/home/hobs/.virtualenvs/civicu/bin/jupyter', 'COMPIZ_CONFIG_PROFILE': 'ubuntu', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'XAUTHORITY': '/home/hobs/.Xauthority', 'XDG_SESSION_DESKTOP': 'ubuntu', 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/hobs', 'LANGUAGE': 'en_US', 'GTK_MODULES': 'gail:atk-bridge:unity-gtk-module', 'VIRTUALENVWRAPPER_WORKON_CD': '1', 'VIRTUAL_ENV': '/home/hobs/.virtualenvs/civicu', 'JPY_PARENT_PID': '17683', 'XDG_RUNTIME_DIR': '/run/user/1000', 'LANG': 'en_US.UTF-8', 'DESKTOP_SESSION': 'ubuntu', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'SSH_AGENT_LAUNCHER': 'gnome-keyring', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'CLICOLOR': '1', 'VIRTUALENVWRAPPER_HOOK_DIR': '/home/hobs/.virtualenvs', 'GTK2_MODULES': 'overlay-scrollbar', 'QT_LINUX_ACCESSIBILITY_ALWAYS_ON': '1', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'TOUCHSCREEN_DEVICE_ID': '12', 'EC2_HOME': '/usr/local/ec2-api-tools', 'WORKON_HOME': '/home/hobs/.virtualenvs', 'JOURNAL_STREAM': '8:29472', 'GIT_PAGER': 'cat', 'PS1': '(civicu) ${debian_chroot:+($debian_chroot)}\\u@\\h:\\w/ \\[\\033[00;32m\\]$(parse_git_branch)\\[\\033[00m\\]\n$ ', 'VIRTUALENVWRAPPER_PROJECT_FILENAME': '.project', 'GNUPLOT_DEFAULT_GDFONT': 'DejaVuSans.ttf', 'QT_IM_MODULE': 'ibus', 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'LOGNAME': 'hobs', 'EB_HOME': '/usr/local/AWS-ElasticBeanstalk-CLI', 'VIRTUALENVWRAPPER_SCRIPT': '/usr/local/bin/virtualenvwrapper.sh', 'PWD': '/home/hobs/src/civicu-pythonii-summer-2017', 'INVOCATION_ID': 'e83e8bbe87234a0e82a0cab937fad320', 'HISTORY_PATH': '/home/hobs/.bash_history_forever', 'VTE_VERSION': '4402', 'QT_ACCESSIBILITY': '1', 'SHELL': '/bin/bash', 'GTK_IM_MODULE': 'ibus', 'QT4_IM_MODULE': 'xim', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated'})




```python
os.environ['PATH'] = '.'
```


```python
os.environ['PATH']
```




    '/home/hobs/.virtualenvs/civicu/bin:/home/hobs/.virtualenvs/civicu/bin:.:/usr/local/bin/:/home/hobs/bin:/home/hobs/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'




```python
os.getenv('USERNAME') or os.getenv('USER')
```




    1


