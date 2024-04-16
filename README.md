# Linux Desktop File V1.0.7 (PyQt6)

## Linux Desktop File est un utilitaire permettant la création de fichiers de configuration desktop simplifiés.
### Il utilise une interface graphique (Qt).
\
\
Dépendance PyQt6 :  
`pip3 install -r requirements.txt`  
\
\
L'interface :  
![Interface](https://github.com/diablo76600/Linux-Desktop-File/assets/3962168/795caaaa-b517-4aa3-a508-94d3c8661dc4)
\
\
L'option Categories :  
![Categories](https://github.com/diablo76600/Linux-Desktop-File/assets/3962168/2d6daffc-0086-422d-a43f-5920f62324de)
\
\
![InterfaceFinale](https://github.com/diablo76600/Linux-Desktop-File/assets/3962168/71ef9d0c-e7bc-4d46-b94a-22e556440ff7)
\
\
Le fichier généré :
<pre><code>[Desktop Entry]
Categories=DesktopSettings;Settings;Utility
Comment=Application permettant la création de fichier de configuration desktop simplifié
Exec=/home/diablo/Public/Applications/ubuntu_desktop_file/ubuntu_desktop_file.bin
GenericName=Création de fichier desktop
Icon=/home/diablo/Public/Applications/ubuntu_desktop_file/Assets/Images/Ubuntu_logo.png
Name=Ubuntu Desktop File
Path=/home/diablo/Public/Applications/ubuntu_desktop_file
StartupNotify=true
Terminal=false
Type=Application
Version=1.0.6</code></pre>


### Linux Desktop File permet également l'execution de fichiers Python avec l'option : 
Launch with Python (par défaut Python3)

L'option activée :  
![InterfaceFinalePy](https://github.com/diablo76600/Linux-Desktop-File/assets/3962168/924ef60c-89e7-483a-891d-e4417dc7ee35)


Le fichier généré :  
<pre><code>[Desktop Entry]
Categories=DesktopSettings;System;Utility  
Comment=Application permettant la création de fichier de configuration desktop simplifié
Exec=python3 /home/diablo/Documents/GitHub/Ubuntu-Desktop/Ui_ubuntu_desktop_file.py
GenericName=Création de fichier desktop
Icon=/home/diablo/Documents/GitHub/Ubuntu-Desktop/Assets/Images/Ubuntu_logo.png
Name=Ubuntu Desktop File
Path=/home/diablo/Documents/GitHub/Ubuntu-Desktop
StartupNotify=true
Terminal=false
Type=Application
Version=1.0.6</code></pre>
\
\
Pour executer le programme, double-cliquez sur le fichier `run_script.sh`




