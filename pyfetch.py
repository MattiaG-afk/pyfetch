#!/usr/bin/python3
import os, sys, psutil, distro, platform

def secs_to_other(time):
    d = int(time / 86400)
    h = int(time / 3600 % 24)
    m = int(time / 60 % 60)

    time = ''
    if d > 1:
        time += str(d) + ' days '
    if h > 1:
        time += str(h) + ' hours '
    if m > 1:
        time += str(m) + ' mins '
    return time

def convert(bytes):
    unitIndex = 0
    units = ['B','KB','MB','GB','TB']
    while 1000 <= bytes:
        bytes /= 1000
        unitIndex += 1
    return f"{round(bytes)}{units[unitIndex]}"

values = {'username': 'os.environ[\'USER\']',
        'nodename': 'os.uname()[1]',
        'os_name': 'distro.linux_distribution()[0]', 
        'os_version': 'distro.linux_distribution()[1]',
        'arch': 'os.uname()[4]',
        'kernel': 'os.uname()[2]',
        'uptime': 'secs_to_other(int(float(open(\'/proc/uptime\').read().split(' ')[0]) - (float(open(\'/proc/uptime\').read().split(\' \')[0]) % 1)))',
        'shell': 'os.environ[\'SHELL\']',
        'editor': 'os.environ[\'EDITOR\']', 
        'lang': 'os.environ[\'LANGUAGE\']',
        'encoding': 'os.device_encoding(0)',
        'pythonv': 'sys.version[0] + sys.version[1] + sys.version[2] + sys.version[3] + sys.version[4] + sys.version[5]',
        'cpu': 'platform.processor()',
        'cpu_number': 'os.cpu_count()',
        'cpu_current_clock': 'int(psutil.cpu_freq().current)',
        'cpu_max_clock': 'psutil.cpu_freq().max',
        'ram': 'convert(psutil.virtual_memory().total)',
        'used_ram': 'convert(psutil.virtual_memory().used)',
        'ram_percent': 'psutil.virtual_memory().percent',
        'swap': 'convert(psutil.swap_memory().total)',
        'used_swap': 'convert(psutil.swap_memory().used)',
        'swap_percent': 'psutil.swap_memory().percent',
        'batt_percentage': 'int(psutil.sensors_battery().percent)',
        'batt_time_left': 'secs_to_other(psutil.sensors_battery().secsleft)'}

for value in open('/etc/pyfetch/pyfetch.conf').readlines():
    if value.find(' = ') != -1:
        if value.split(' = ')[1].replace('\n', '') == 'auto' or value.split(' = ')[1].replace('\n', '') == 'yes':
            try:
                exec(value.split(' = ')[0] + ' = ' + values[value.split(' = ')[0]])
            except:
                exec(value.split(' = ')[0] + ' = \'no\'')
        elif value.split(' = ')[1].replace('\n', '') == 'no':
            exec(value.split(' = ')[0] + ' = \'no\'')
        else:
            exec(value.split(' = ')[0] + ' = "' + value.split(' = ')[1].replace('\n', '') + '"')


color = {
    'normal': '\u001b[00;0m',
    'Arch': '\u001b[36;1m',
    'Debian': '\u001b[31;1m',
    'Elementary': '\u001b[94;1m',
    'Fedora': '\u001b[34;1m',
    'Gentoo': '\u001b[35;1m',
    'Linux': '\u001b[00;1m',
    'Manjaro': '\u001b[32;1m',
    'Mint': '\u001b[32;1m',
    'Slackware': '\u001b[94;1m',
    'Solus': '\u001b[94;1m',
    'Ubuntu': '\u001b[31;1m',
    'Void': '\u001b[32;1m'
}
logo = {
    'Arch': [
        '                    \u001b[36;1my:\u001b[00;0m\t\t\t\t',
        '                  \u001b[36;1msMN-\u001b[00;0m\t\t\t\t',
        '                 \u001b[36;1m+MMMm`\u001b[00;0m\t\t\t\t',
        '                \u001b[36;1m/MMMMMd`\u001b[00;0m\t\t\t',
        '               \u001b[36;1m:NMMMMMMy\u001b[00;0m\t\t\t',
        '              \u001b[36;1m-NMMMMMMMMs\u001b[00;0m\t\t\t',
        '             \u001b[36;1m.NMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '            \u001b[36;1m.mMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '            \u001b[36;1moNMMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '          \u001b[36;1m`+:-+NMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        '          \u001b[36;1m.sNMNhNMMMMMMMMMMMM/\u001b[00;0m\t\t\t',
        '        \u001b[36;1m`hho/sNMMMMMMMMMMMMMMM/\u001b[00;0m\t\t\t',
        '       \u001b[36;1m`.`omMMmMMMMMMMMMMMMMMMM+\u001b[00;0m\t\t',
        '      \u001b[36;1m.mMNdshMMMMd+::oNMMMMMMMMMo\u001b[00;0m\t\t',
        '     \u001b[36;1m.mMMMMMMMMM+\u001b[00;0m     \u001b[36;1m`yMMMMMMMMMs\u001b[00;0m\t\t',
        '    \u001b[36;1m.NMMMMMMMMM/\u001b[00;0m        \u001b[36;1myMMMMMMMMMy\u001b[00;0m\t\t',
        '   \u001b[36;1m-NMMMMMMMMMh\u001b[00;0m         \u001b[36;1m`mNMMMMMMMMd`\u001b[00;0m\t\t',
        '  \u001b[36;1m/NMMMNds+:.`\u001b[00;0m             \u001b[36;1m`-/oymMMMm.\u001b[00;0m\t\t',
        ' \u001b[36;1m+Mmy/.\u001b[00;0m                          \u001b[36;1m`:smN:\u001b[00;0m\t\t',
        '\u001b[36;1m/+.\u001b[00;0m                                  \u001b[36;1m-o.\u001b[00;0m\t'],
    'Debian': [
        '       \u001b[00;1m_,met$$$$$gg.\t\t',
        '    \u001b[00;1m,g$$$$$$$$$$$$$$$P.\t\t',
        '  \u001b[00;1m,g$$P"     """Y$$.".\t\t',
        ' \u001b[00;1m,$$P\'              `$$$.\t',
        '\u001b[00;1m,$$P       ,ggs.     `$$b:\t',
        '\u001b[00;1m`d$$\'     ,$P"\'   \u001b[31;1m.\u001b[00;1m    $$$\t',
        ' \u001b[00;1m$$P      d$\'     \u001b[31;1m,\u001b[00;1m    $$P\t',
        ' \u001b[00;1m$$:      $$.   \u001b[31;1m-\u001b[00;1m    ,d$$\'\t',
        ' \u001b[00;1m$$;      Y$b._   _,d$P\'\t',
        ' \u001b[00;1mY$$.    \u001b[31;1m`.\u001b[00;1m`"Y$$$$P"\'\t\t',
        ' \u001b[00;1m`$$b      \u001b[31;1m"-.__\u001b[00;1m\t\t',
        '  \u001b[00;1m`Y$$\t\t\t\t',
        '   \u001b[00;1m`Y$$.\t\t\t',
        '     \u001b[00;1m`$$b.\t\t\t',
        '       \u001b[00;1m`Y$$b.\t\t\t',
        '          \u001b[00;1m`"Y$b._\t\t',
        '              \u001b[00;1m`"""\t\t'],
    'Elementary': [
        '         \u001b[00;1meeeeeeeeeeeeeeeee\t\t',
        '      eeeeeeeeeeeeeeeeeeeeeee\t\t',
        '    eeeee  eeeeeeeeeeee   eeeee\t\t',
        '  eeee   eeeee       eee     eeee\t',
        ' eeee   eeee          eee     eeee\t',
        'eee    eee            eee       eee\t',
        'eee   eee            eee        eee\t',
        'ee    eee           eeee       eeee\t',
        'ee    eee         eeeee      eeeeee\t',
        'ee    eee       eeeee      eeeee ee\t',
        'eee   eeee   eeeeee      eeeee  eee\t',
        'eee    eeeeeeeeee     eeeeee    eee\t',
        ' eeeeeeeeeeeeeeeeeeeeeeee    eeeee\t',
        '  eeeeeeee eeeeeeeeeeee      eeee\t',
        '    eeeee                 eeeee\t\t',
        '      eeeeeee         eeeeeee\t\t',
        '         eeeeeeeeeeeeeeeee\t\t'],
    'Fedora': [
        '          \u001b[34;1m/:-------------:\\\u001b[00;0m\t\t',
        '       \u001b[34;1m:-------------------::\u001b[00;0m\t\t',
        '     \u001b[34;1m:-----------\u001b[00;0m/shhOHbmp\u001b[34;1m---:\\\u001b[00;0m\t\t',
        '   \u001b[34;1m/-----------\u001b[00;0momMMMNNNMMD  \u001b[34;1m---:\u001b[00;0m\t',
        '  \u001b[34;1m:-----------\u001b[00;0msMMMMNMNMP\u001b[34;1m.    ---:\u001b[00;0m\t',
        ' \u001b[34;1m:-----------\u001b[00;0m:MMMdP\u001b[34;1m-------\u001b[00;0m    \u001b[34;1m---\\\u001b[00;0m\t',
        '\u001b[34;1m,------------\u001b[00;0m:MMMd\u001b[34;1m--------\u001b[00;0m    \u001b[34;1m---:\u001b[00;0m\t',
        '\u001b[34;1m:------------\u001b[00;0m:MMMd\u001b[34;1m-------\u001b[00;0m    \u001b[34;1m.---:\u001b[00;0m\t',
        '\u001b[34;1m:----    \u001b[00;0moNMMMMMMMMMNho\u001b[34;1m     .----:\u001b[00;0m\t',
        '\u001b[34;1m:--     .\u001b[00;0m+shhhMMMmhhy++\u001b[34;1m   .------/\u001b[00;0m\t',
        '\u001b[34;1m:-    -------\u001b[00;0m:MMMd\u001b[34;1m--------------:\u001b[00;0m\t',
        '\u001b[34;1m:-   --------\u001b[00;0m/MMMd\u001b[34;1m-------------;\u001b[00;0m\t',
        '\u001b[34;1m:-    ------\u001b[00;0m/hMMMy\u001b[34;1m------------:\u001b[00;0m\t\t',
        '\u001b[34;1m:--\u001b[00;0m :dMNdhhdNMMNo\u001b[34;1m------------;\u001b[00;0m\t\t',
        '\u001b[34;1m:---\u001b[00;0m:sdNMMMMNds:\u001b[34;1m------------:\u001b[00;0m\t\t',
        '\u001b[34;1m:------\u001b[00;0m:://:\u001b[34;1m-------------::\u001b[00;0m\t\t',
        '\u001b[34;1m:---------------------://\u001b[00;0m\t\t'],
    'Gentoo': [
        '         \u001b[35;1m-/oyddmdhs+:.\u001b[00;1m\t\t\t',
        '     \u001b[35;1m-o\u001b[00;1mdNMMMMMMMMNNmhy+\u001b[35;1m-`\u001b[00;0m\t\t',
        '   \u001b[35;1m-y\u001b[00;1mNMMMMMMMMMMMNNNmmdhy\u001b[35;1m+-\u001b[00;0m\t\t',
        ' \u001b[35;1m`o\u001b[00;1mmMMMMMMMMMMMMNmdmmmmddhhy\u001b[35;1m/`\u001b[00;0m\t\t',
        ' \u001b[35;1mom\u001b[00;1mMMMMMMMMMMMN\u001b[35;1mhhyyyo\u001b[00;1mhmdddhhhd\u001b[35;1mo`\u001b[00;0m\t',
        '\u001b[35;1m.y\u001b[00;1mdMMMMMMMMMMd\u001b[35;1mhs++so/s\u001b[00;1mmdddhhhhdm\u001b[35;1m+`\u001b[00;0m\t',
        ' \u001b[35;1moy\u001b[00;1mhdmNMMMMMMMN\u001b[35;1mdyooy\u001b[00;1mdmddddhhhhyhN\u001b[35;1md.\u001b[00;0m\t',
        '  \u001b[35;1m:o\u001b[00;1myhhdNNMMMMMMMNNNmmdddhhhhhyym\u001b[35;1mMh\u001b[00;0m\t',
        '    \u001b[35;1m.:\u001b[00;1m+sydNMMMMMNNNmmmdddhhhhhhmM\u001b[35;1mmy\u001b[00;0m\t',
        '       \u001b[35;1m/m\u001b[00;1mMMMMMMNNNmmmdddhhhhhmMNh\u001b[35;1ms:\u001b[00;0m\t',
        '    \u001b[35;1m`o\u001b[00;1mNMMMMMMMNNNmmmddddhhdmMNhs\u001b[35;1m+`\u001b[00;0m\t',
        '  \u001b[35;1m`s\u001b[00;1mNMMMMMMMMNNNmmmdddddmNMmhs\u001b[35;1m/.\u001b[00;0m\t',
        ' \u001b[35;1m/N\u001b[00;1mMMMMMMMMNNNNmmmdddmNMNdso\u001b[35;1m:`\u001b[00;0m\t\t',
        '\u001b[35;1m+M\u001b[00;1mMMMMMMNNNNNmmmmdmNMNdso\u001b[35;1m/-\u001b[00;0m\t\t',
        '\u001b[35;1myM\u001b[00;1mMNNNNNNNmmmmmNNMmhs+/\u001b[35;1m-`\u001b[00;0m\t\t',
        '\u001b[35;1m/h\u001b[00;1mMMNNNNNNNNMNdhs++/\u001b[35;1m-`\u001b[00;0m\t\t\t',
        '\u001b[35;1m`/\u001b[00;1mohdmmddhys+++/:\u001b[35;1m.`\u001b[00;0m\t\t\t',
        '  \u001b[35;1m`-//////:--.\u001b[00;1m\t\t\t\t'],
    'Linux': [
        '        \u001b[30;1m#####\u001b[00;1m\t\t',
        '       \u001b[30;1m#######\u001b[00;1m\t\t',
        '       \u001b[30;1m##\u001b[00;1mO\u001b[30;1m#\u001b[00;1mO\u001b[30;1m##\u001b[00;1m\t\t',
        '       \u001b[30;1m#\u001b[33;1m#####\u001b[30;1m#\u001b[00;1m\t\t',
        '     \u001b[30;1m##\u001b[00;1m##\u001b[33;1m###\u001b[00;1m##\u001b[30;1m##\u001b[00;1m\t',
        '    \u001b[30;1m#\u001b[00;1m##########\u001b[30;1m##\u001b[00;1m\t',
        '   \u001b[30;1m#\u001b[00;1m############\u001b[30;1m##\u001b[00;1m\t',
        '   \u001b[30;1m#\u001b[00;1m############\u001b[30;1m###\u001b[00;1m\t',
        '  \u001b[33;1m##\u001b[30;1m#\u001b[00;1m###########\u001b[30;1m##\u001b[33;1m#\u001b[00;1m\t',
        '\u001b[33;1m######\u001b[30;1m#\u001b[00;1m#######\u001b[30;1m#\u001b[33;1m######\u001b[00;1m\t',
        '\u001b[33;1m#######\u001b[30;1m#\u001b[00;1m#####\u001b[30;1m#\u001b[33;1m#######\u001b[00;1m\t',
        '  \u001b[33;1m#####\u001b[30;1m#######\u001b[33;1m#####\u001b[00;1m\t',
        '\t\t\t',
        '\t\t\t',
        '\t\t\t',
        '\t\t\t'],
    'Manjaro': [
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m██████████████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m            \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t',
        '\u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\u001b[00;1m  \u001b[32;1m████████\t'],
    'Mint': [
        '             \u001b[00;1m...-:::::-...\t\t\t',
        '          \u001b[00;1m.-MMMMMMMMMMMMMMM-.\t\t\t',
        '      \u001b[00;1m.-MMMM\u001b[32;1m`..-:::::::-..`\u001b[00;1mMMMM-.\t\t',
        '    \u001b[00;1m.:MMMM\u001b[32;1m.:MMMMMMMMMMMMMMM:.\u001b[00;1mMMMM:.\t\t',
        '   \u001b[00;1m-MMM\u001b[32;1m-M---MMMMMMMMMMMMMMMMMMM.\u001b[00;1mMMM-\t\t',
        ' \u001b[00;1m`:MMM\u001b[32;1m:MM`\u001b[00;1m  \u001b[32;1m:MMMM:....::-...-MMMM:\u001b[00;1mMMM:`\t\t',
        ' \u001b[00;1m:MMM\u001b[32;1m:MMM`\u001b[00;1m  \u001b[32;1m:MM:`\u001b[00;1m  \u001b[32;1m``\u001b[00;1m    \u001b[32;1m``\u001b[00;1m  \u001b[32;1m`:MMM:\u001b[00;1mMMM:\t\t',
        '\u001b[00;1m.MMM\u001b[32;1m.MMMM`\u001b[00;1m  \u001b[32;1m:MM.\u001b[00;1m  \u001b[32;1m-MM.\u001b[00;1m  \u001b[32;1m.MM-\u001b[00;1m  \u001b[32;1m`MMMM.\u001b[00;1mMMM.\t',
        '\u001b[00;1m:MMM\u001b[32;1m:MMMM`\u001b[00;1m  \u001b[32;1m:MM.\u001b[00;1m  \u001b[32;1m-MM-\u001b[00;1m  \u001b[32;1m.MM:\u001b[00;1m  \u001b[32;1m`MMMM-\u001b[00;1mMMM:\t',
        '\u001b[00;1m:MMM\u001b[32;1m:MMMM`\u001b[00;1m  \u001b[32;1m:MM.\u001b[00;1m  \u001b[32;1m-MM-\u001b[00;1m  \u001b[32;1m.MM:\u001b[00;1m  \u001b[32;1m`MMMM:\u001b[00;1mMMM:\t',
        '\u001b[00;1m:MMM\u001b[32;1m:MMMM`\u001b[00;1m  \u001b[32;1m:MM.\u001b[00;1m  \u001b[32;1m-MM-\u001b[00;1m  \u001b[32;1m.MM:\u001b[00;1m  \u001b[32;1m`MMMM-\u001b[00;1mMMM:\t',
        '\u001b[00;1m.MMM\u001b[32;1m.MMMM`\u001b[00;1m  \u001b[32;1m:MM:--:MM:--:MM:  \u001b[32;1m`MMMM.\u001b[00;1mMMM.\t',
        ' \u001b[00;1m:MMM\u001b[32;1m:MMM-\u001b[00;1m  \u001b[32;1m`-MMMMMMMMMMMM-`  \u001b[32;1m-MMM-\u001b[00;1mMMM:\t\t',
        '  \u001b[00;1m:MMM\u001b[32;1m:MMM:`\u001b[00;1m                `\u001b[32;1m:MMM:\u001b[00;1mMMM:\t\t',
        '   \u001b[00;1m.MMM\u001b[32;1m.MMMM:--------------:MMMM.\u001b[00;1mMMM.\t\t',
        '     \u001b[00;1m\'-MMMM\u001b[32;1m.-MMMMMMMMMMMMMMM-.\u001b[00;1mMMMM-\'\t\t',
        '       \u001b[00;1m\'.-MMMM\u001b[32;1m``--:::::--``\u001b[00;1mMMMM-.\'\t\t',
        '            \u001b[00;1m\'-MMMMMMMMMMMMM-\'\t\t\t',
        '               \u001b[00;1m``-:::::-``\t\t\t'],
    'Solus': [
        '            \u001b[00;0m-```````````\t\t',
        '          \u001b[00;0m`-+/------------.`\t\t',
        '       \u001b[00;0m.---:mNo---------------.\t\t',
        '     \u001b[00;0m.-----yMMMy:---------------.\t',
        '   \u001b[00;0m`------oMMMMMm/----------------`\t',
        '  \u001b[00;0m.------/MMMMMMMN+----------------.\t',
        ' \u001b[00;0m.------/NMMMMMMMMm-+/--------------.\t',
        '\u001b[00;0m`------/NMMMMMMMMMN-:mh/-------------`\t',
        '\u001b[00;0m.-----/NMMMMMMMMMMM:-+MMd//oso/:-----.\t',
        '\u001b[00;0m-----/NMMMMMMMMMMMM+--mMMMh::smMmyo:--\t',
        '\u001b[00;0m----+NMMMMMMMMMMMMMo--yMMMMNo-:yMMMMd/.\t',
        '\u001b[00;0m.--oMMMMMMMMMMMMMMMy--yMMMMMMh:-yMMMy-`\t',
        '\u001b[00;0m`-sMMMMMMMMMMMMMMMMh--dMMMMMMMd:/Ny+y.\t',
        '\u001b[00;0m`-/+osyhhdmmNNMMMMMm-/MMMMMMMmh+/ohm+\t',
        '  \u001b[00;0m.------------:://+-/++++++\u001b[94;1moshddys:\u001b[00;0m\t',
        '   \u001b[94;1m-hhhhyyyyyyyyyyyhhhhddddhysssso-\u001b[00;0m\t',
        '    \u001b[94;1m`:ossssssyysssssssssssssssso:`\u001b[00;0m\t',
        '      \u001b[94;1m`:+ssssssssssssssssssss+-\u001b[00;0m\t\t',
        '         \u001b[94;1m`-/+ssssssssssso+/-`\u001b[00;0m\t\t',
        '              \u001b[94;1m`.-----..`\u001b[00;0m\t\t'],
    'Slackware': [
        '                  \u001b[94;1m:::::::\u001b[00;1m\t\t\t',
        '            \u001b[94;1m:::::::::::::::::::\u001b[00;1m\t\t\t',
        '         \u001b[94;1m:::::::::::::::::::::::::\u001b[00;1m\t\t',
        '       \u001b[94;1m::::::::\u001b[00;1mcllcccccllllllll\u001b[94;1m::::::\u001b[00;1m\t\t',
        '    \u001b[94;1m:::::::::\u001b[00;1mlc               dc\u001b[94;1m:::::::\u001b[00;1m\t\t',
        '   \u001b[94;1m::::::::\u001b[00;1mcl   clllccllll    oc\u001b[94;1m:::::::::\u001b[00;1m\t',
        '  \u001b[94;1m:::::::::\u001b[00;1mo   lc\u001b[94;1m::::::::\u001b[00;1mco   oc\u001b[94;1m::::::::::\u001b[00;1m\t',
        ' \u001b[94;1m::::::::::\u001b[00;1mo    cccclc\u001b[94;1m:::::\u001b[00;1mclcc\u001b[94;1m::::::::::::\u001b[00;1m\t',
        ' \u001b[94;1m:::::::::::\u001b[00;1mlc        cclccclc\u001b[94;1m:::::::::::::\u001b[00;1m\t',
        '\u001b[94;1m::::::::::::::\u001b[00;1mlcclcc          lc\u001b[94;1m::::::::::::\u001b[00;1m\t',
        '\u001b[94;1m::::::::::\u001b[00;1mcclcc\u001b[94;1m:::::\u001b[00;1mlccclc     oc\u001b[94;1m:::::::::::\u001b[00;1m\t',
        '\u001b[94;1m::::::::::\u001b[00;1mo    l\u001b[94;1m::::::::::\u001b[00;1ml    lc\u001b[94;1m:::::::::::\u001b[00;1m\t',
        ' \u001b[94;1m:::::\u001b[00;1mcll\u001b[94;1m:\u001b[00;1mo     clcllcccll     o\u001b[94;1m:::::::::::\u001b[00;1m\t',
        ' \u001b[94;1m:::::\u001b[00;1mocc\u001b[94;1m:\u001b[00;1mo                  clc\u001b[94;1m:::::::::::\u001b[00;1m\t',
        '  \u001b[94;1m::::\u001b[00;1mocl\u001b[94;1m:\u001b[00;1mccslclccclclccclclc\u001b[94;1m:::::::::::::\u001b[00;1m\t',
        '   \u001b[94;1m:::\u001b[00;1moclcccccccccccccllllllllllllll\u001b[94;1m:::::\u001b[00;1m\t',
        '    \u001b[94;1m::\u001b[00;1mlcc1lcccccccccccccccccccccccco\u001b[94;1m::::\u001b[00;1m\t',
        '      \u001b[94;1m::::::::::::::::::::::::::::::::\u001b[00;1m\t\t',
        '        \u001b[94;1m::::::::::::::::::::::::::::\u001b[00;1m\t\t',
        '           \u001b[94;1m::::::::::::::::::::::\u001b[00;1m\t\t',
        '                \u001b[94;1m::::::::::::\u001b[00;1m\t\t\t'],
    'Ubuntu': [
        '            \u001b[31;1m.-/+oossssoo+/-.\u001b[00;1m\t\t\t',
        '        \u001b[31;1m`:+ssssssssssssssssss+:`\u001b[00;1m\t\t',
        '      \u001b[31;1m-+ssssssssssssssssssyyssss+-\u001b[00;1m\t\t',
        '    \u001b[31;1m.ossssssssssssssssss\u001b[00;1mdMMMNy\u001b[31;1msssso.\u001b[00;1m\t\t',
        '   \u001b[31;1m/sssssssssss\u001b[00;1mhdmmNNmmyNMMMMh\u001b[31;1mssssss/\u001b[00;1m\t\t',
        '  \u001b[31;1m+sssssssss\u001b[00;1mhm\u001b[31;1myd\u001b[00;1mMMMMMMMNddddy\u001b[31;1mssssssss+\u001b[00;1m\t\t',
        ' \u001b[31;1m/ssssssss\u001b[00;1mhNMMM\u001b[31;1myh\u001b[00;1mhyyyyhmNMMMNh\u001b[31;1mssssssss/\u001b[00;1m\t\t',
        '\u001b[31;1m.ssssssss\u001b[00;1mdMMMNh\u001b[31;1mssssssssss\u001b[00;1mhNMMMd\u001b[31;1mssssssss.\u001b[00;1m\t',
        '\u001b[31;1m+ssss\u001b[00;1mhhhyNMMNy\u001b[31;1mssssssssssss\u001b[00;1myNMMMy\u001b[31;1msssssss+\u001b[00;1m\t',
        '\u001b[31;1moss\u001b[00;1myNMMMNyMMh\u001b[31;1mssssssssssssss\u001b[00;1mhmmmh\u001b[31;1mssssssso\u001b[00;1m\t',
        '\u001b[31;1moss\u001b[00;1myNMMMNyMMh\u001b[31;1msssssssssssssshmmmh\u001b[31;1mssssssso\u001b[00;1m\t',
        '\u001b[31;1m+ssss\u001b[00;1mhhhyNMMNy\u001b[31;1mssssssssssss\u001b[00;1myNMMMy\u001b[31;1msssssss+\u001b[00;1m\t',
        '\u001b[31;1m.ssssssss\u001b[00;1mdMMMNh\u001b[31;1mssssssssss\u001b[00;1mhNMMMd\u001b[31;1mssssssss.\u001b[00;1m\t',
        ' \u001b[31;1m/ssssssss\u001b[00;1mhNMMM\u001b[31;1myh\u001b[00;1mhyyyyhdNMMMNh\u001b[31;1mssssssss/\u001b[00;1m\t\t',
        '  \u001b[31;1m+sssssssss\u001b[00;1mdm\u001b[31;1myd\u001b[00;1mMMMMMMMMddddy\u001b[31;1mssssssss+\u001b[00;1m\t\t',
        '   \u001b[31;1m/sssssssssss\u001b[00;1mhdmNNNNmyNMMMMh\u001b[31;1mssssss/\u001b[00;1m\t\t',
        '    \u001b[31;1m.ossssssssssssssssss\u001b[00;1mdMMMNy\u001b[31;1msssso.\u001b[00;1m\t\t',
        '      \u001b[31;1m-+sssssssssssssssss\u001b[00;1myyy\u001b[31;1mssss+-\u001b[00;1m\t\t',
        '        \u001b[31;1m`:+ssssssssssssssssss+:`\u001b[00;1m\t\t',
        '            \u001b[31;1m.-/+oossssoo+/-.\u001b[00;1m\t\t\t'],
    'Void': [
        '                \u001b[32;1m__.;=====;.__\t\t\t',
        '            \u001b[32;1m_.=+==++=++=+=+===;.\t\t',
        '             \u001b[32;1m-=+++=+===+=+=+++++=_\t\t',
        '        \u001b[32;1m.     -=:``     `--==+=++==.\t\t',
        '       \u001b[32;1m_vi,    `            --+=++++:\t\t',
        '      \u001b[32;1m.uvnvi.       _._       -==+==+.\t\t',
        '     \u001b[32;1m.vvnvnI`    .;==|==;.     :|=||=|.\t\t',
        '\u001b[90;1m+QmQQm\u001b[32;1mpvvnv; \u001b[90;1m_yYsyQQWUUQQQm #QmQ#\u001b[32;1m:\u001b[90;1mQQQWUV$QQm.\t',
        '\'\u001b[90;1m -QQWQW\u001b[32;1mpvvo\u001b[90;1mwZ?.wQQQE\u001b[32;1m==<\u001b[90;1mQWWQ/QWQW.QQWW\u001b[32;1m(: \u001b[90;1mjQWQE\'\t',
        '\u001b[90;1m  -$QQQQmmU\'  jQQQ@\u001b[32;1m+=<\u001b[90;1mQWQQ)mQQQ.mQQQC\u001b[32;1m+;\u001b[90;1mjWQQ@\'\t',
        '\u001b[90;1m   -$WQ8Y\u001b[32;1mnI:   \u001b[90;1mQWQQwgQQWV\u001b[32;1m`\u001b[90;1mmWQQ.jQWQQgyyWW@!\t',
        '\u001b[32;1m     -1vvnvv.     `~+++`        ++|+++\t\t',
        '      \u001b[32;1m+vnvnnv,                 `-|===\t\t',
        '       \u001b[32;1m+vnvnvns.           .      :=-\t\t',
        '        \u001b[32;1m-Invnvvnsi..___..=sv=.     `\t\t',
        '          \u001b[32;1m+Invnvnvnnnnnnnnvvnn;.\t\t',
        '            \u001b[32;1m~|Invnvnvvnvvvnnv}+`\t\t',
        '               \u001b[32;1m-~|{*l}*|~\t\t\t']
}

if os_name in logo:
    os_logo = logo[os_name]
    os_color = color[os_name]
else:
    os_logo = logo['Linux']
    os_color = color['Linux']

line = 0
print(os_logo[line] + os_color + username + color["normal"] + '@' + os_color + nodename + color["normal"])
line += 1
print(os_logo[line] + color["normal"] + ('-' * (len(username + nodename) + 1)))
line += 1
if os_name != 'no':
    print(os_logo[line] + os_color + 'OS' + color["normal"] + ':', os_name + '/Linux', 'v' + os_version, arch)
    line += 1
if kernel != 'no':
    print(os_logo[line] + os_color + 'Kernel' + color["normal"] + ':', kernel)
    line += 1
if uptime != 'no':
    print(os_logo[line] + os_color + 'Uptime' + color["normal"] + ':', uptime)
    line += 1
if shell != 'no':
    print(os_logo[line] + os_color + 'Shell' + color["normal"] + ':', shell)
    line += 1
if editor != 'no':
    print(os_logo[line] + os_color + 'Editor' + color["normal"] + ':', editor)
    line += 1
if lang != 'no':
    print(os_logo[line] + os_color + 'Language' + color["normal"] + ':', lang)
    line += 1
if encoding != 'no':
    print(os_logo[line] + os_color + 'Encoding' + color["normal"] + ':', encoding)
    line += 1
if pythonv != 'no':
    print(os_logo[line] + os_color + 'Python version' + color["normal"] + ':', pythonv)
    line += 1
if cpu != 'no' or values['cpu_number'] != 'no' or value['cpu_current_clock'] != 'no' or value['cpu_max_clock'] != 'no':
    print(os_logo[line] + os_color + 'CPU' + color["normal"] + ':', cpu, '(' + str(cpu_number) + ')', '@', str(cpu_current_clock) + 'GHz', '/', str(cpu_max_clock) + 'GHz')
    line += 1
if ram != 'no' or values['used_ram'] != 'no' or value['ram_percent'] != 'no':
    print(os_logo[line] + os_color + 'Memory' + color["normal"] + ':', str(used_ram), '/', str(ram), str(ram_percent) + '%')
    line += 1
if swap != 'no' or values['used_swap'] != 'no' or value['swap_percent'] != 'no':
    print(os_logo[line] + os_color + 'Swap' + color["normal"] + ':', str(used_swap), '/', str(swap), str(swap_percent) + '%')
    line += 1
if batt_percentage != 'no' or batt_time_left != 'no':
    if psutil.sensors_battery().power_plugged:
        print(os_logo[line] + os_color + 'Battery' + color["normal"] + ':', 'Plugged', '(' + str(batt_percentage) + '%)')
        line += 1
    else:
        print(os_logo[line] + os_color + 'Battery' + color["normal"] + ':', str(batt_percentage) + '%', '(' + str(batt_time_left) + 'left)')
        line += 1
for i in range(line, len(os_logo)):
    print(os_logo[i])
