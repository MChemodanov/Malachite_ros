Инструкция:

0. Как создать workspace, если его еще нет:
smtu@smtu-VirtualBox:~$ mkdir ws_w
smtu@smtu-VirtualBox:~$ cd ws_w
smtu@smtu-VirtualBox:~/ws_w$ mkdir src
smtu@smtu-VirtualBox:~/ws_w$ cd src
smtu@smtu-VirtualBox:~/ws_w/src$ catkin_init_workspace 

1. Как получить последнюю версию кода:

smtu@smtu-VirtualBox:~$ cd ~/ws_w/src
smtu@smtu-VirtualBox:~/ws_w/src$ git clone https://github.com/MChemodanov/Malachite_ros.git
smtu@smtu-VirtualBox:~/ws_w/src$ mv Malachite_ros turtle
smtu@smtu-VirtualBox:~/ws_w/src$ cd ..
smtu@smtu-VirtualBox:~/ws_w$ catkin_make

2. Как запустить:
Сначала добавляем нужные пути:
smtu@smtu-VirtualBox:~/ws_w$ source devel/setup.bash 

2.1. roslaunch turtle lesson1.launch
Запускаем черепаху в режиме телеуправления (управляется стрелками клавиатуры из консоли)
2.2. roslaunch turtle lesson2.launch
Запускаем черепаху, которая ездит по квадрату, не используя обратную связь.
Исходный код управляющей программы тут: ~/ws_w/src/turtle/scripts/square.py

2.3. roslaunch turtle lesson3.launch
Запускаем черепаху, которая ездит по шестиугольнику, используя обратную связь и алгоритм p-регулятора.
Исходный код управляющей программы тут: ~/ws_w/src/turtle/scripts/square_p.py
В программе можно менять k_p и наблюдать, как изменяется поведение черепахи.

3. Добавляем динамику

3.1 roslaunch turtle lesson4_1.launch

Управление черепахой с клавиатуры. Параметры симулятора (масса, момент иннерции, коэффициент сопротивления задаются в файле lesson4_1.launch)

3.2 roslaunch turtle lesson4_2.launch

Запускаем черепаху, которая ездит по шестиугольнику, используя обратную связь и алгоритм p-регулятора.
Исходный код управляющей программы тут: ~/ws_w/src/turtle/scripts/square_pid.py
Реализован только П-регулятор. Остальное предлагается реализовать студентам.

Параметры симулятора (масса, момент иннерции, коэффициент сопротивления) и регуляторов задаются в файле lesson4_2.launch

