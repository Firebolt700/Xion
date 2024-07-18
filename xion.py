'''
xion.py - No. XIV but as a Discord bot this time, instead of a Replica

Who else would we have ice cream with?

Started on: 2024-07-17

Written by Ben and Dak

~~ Pitiful Heartless, mindlessly collecting hearts. The rage of the 
Keyblade releases those hearts. They gather in darkness, masterless and free...
until they weave together to make Kingdom Hearts. And when that time comes, we 
can truly, finally exist. ~~ 

TODO:
- Separate variables/functions that don't need to be stored in xion.py into other .py files, for organization(13)/education's sake
- Beautify the embedded message for the Organization XIII member list command
- Add DND dice roll functionality
- Add moderator functionality (deleting messages, timing out users, etc)
- Add helper/tracker functionality to assist in completing all of the Kingdom hearts games (Synthesis item locations/drops, achievements, recipes, how to get X, boss guides(?), etc) (Maybe other games too?)
- Other cool stuff, eventually




- Complete Kingdom Hearts
- Wait for KH4


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⢸⡆⠈⠳⣄⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠙⢦⠀⠀⠀⠀⡟⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡇⠀⢷⠀⠀⠈⠳⣄⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⢰⡇⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⡇⠀⠈⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⣸⡇⠀⠙⣆⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢹⡇⠀⣄⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠇⠀⠀⠙⣆⠀⢰⡿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢸⠈⢣⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⢸⠃⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⣿⠳⣄⡀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠻⡝⠷⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇      ⠘⣆⠈⠙⠓⠦⢤⣄⣀⣿⣀⣀⢀⡀⠘⢦⡀⠙⠓⠲⢦⣤⣄⣀⡀                     ⢸⡄         Roxas upon finding out it is, in fact, a stick.
⡇⠀⠀⢀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⡀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠈⢳⣦⣄⡀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣶⣤⣀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⢀⡀⠀⠀⠈⠷⣍⠙⠛⠛⠓⠶⠶⠖⠚⠛⠛⠉⠉⠀⠙⠾⣉⡉⠉⠉⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⣿⡛⠓⠒⠒⢾⣟⡢⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣓⣶⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠸⣿⣦⡀⠀⠀⠈⠛⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠶⠋⢉⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢇⢾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⡀⠹⡄⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠘⣿⣛⠦⣤⣀⠀⠀⠈⠙⠲⣤⣀⣠⠤⠴⠒⠛⠓⠚⣻⠿⠋⠁⠀⠀⣀⡤⠖⠃⠀⢀⡤⣾⡷⢋⡞⠀⠀⣰⠂⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡟⢦⣹⡀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠸⣏⠷⢤⠤⠀⠀⠀⣀⠴⠋⠀⠀⠀⠀⢀⣀⠴⠛⣁⣀⠤⠶⢛⡽⠋⠀⣀⡤⠞⠋⠰⠋⠀⡼⠁⣠⠞⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠙⢷⡀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠹⣆⠀⠀⢀⣤⠚⠁⠀⠀⠀⣀⣤⣶⠯⠖⠚⠋⠉⠀⣠⡴⣋⣤⢶⠟⠉⠀⠀⠀⠀⠀⣼⣃⣼⠋⠀⢀⡜⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠘⠃⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⢈⡿⠖⠋⠀⠀⠀⠀⠀⠈⢀⣠⠖⢫⠀⠀⠀⣠⡾⢛⣻⢟⣟⡏⠀⢀⠀⠀⠀⠀⣾⡿⡿⢣⠀⣠⠞⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⣠
⡇⠀⠀⢀⣤⠔⠋⠀⢀⡀⠀⠀⢀⣠⡴⠚⠋⠁⠀⡏⠀⠀⣠⢏⡤⠚⠁⣸⣿⠁⢠⡾⠀⠀⢠⡾⠋⡾⠁⣎⡴⠃⠀⠀⠹⣆⠀⡆⠀⠀⠀⠀⠀⠀⠀⠘⣆⠠⡇⠀⠀⠀⣠⠖⠁
⣦⠴⠾⠿⠶⢞⣛⣿⣯⡤⠾⠛⢉⠀⠀⠀⠀⠀⣼⠀⢀⣼⡽⠋⠀⠀⢀⣿⠃⢀⡎⠀⠀⢠⡏⢀⡾⠁⣼⣏⣁⣀⣀⣀⣀⣹⡄⢸⡄⠀⠀⡄⠀⠀⠀⠀⠘⢷⣷⠀⢀⡼⠁⠀⠀
⡇⠀⠀⠀⠀⠈⡿⢠⡾⠂⠀⠀⢸⠀⠀⠀⠀⢰⠏⢀⣾⠟⠓⠛⠛⠛⢻⡏⣠⡟⠁⠀⣰⣟⢀⡾⠛⠛⠋⠉⠁⠀⠀⠀⠉⠉⢻⡌⣷⠀⠀⢸⠀⠀⠀⢰⡄⠈⣿⢠⡞⠀⠀⠀⠀
⡇⠀⠀⠀⠀⣼⡷⡿⠁⠀⠀⠀⢸⠀⠀⠀⢀⡏⣠⠟⠁⠀⠀⠀⠀⠀⢸⣱⢋⡇⠀⣠⢯⣧⡟⠀⠀⠀⠀⠀⢀⣀⠠⠤⠀⠀⠀⢳⣹⡀⠀⢸⡄⠀⠀⠸⡇⠀⣿⡟⠀⠀⠀⠀⠀
⠂⠀⠀⠀⠸⠋⣴⠃⣠⡾⠀⠀⢸⠀⠀⠀⣼⡿⠋⢀⣴⣾⣿⣿⣶⣀⡟⠁⣼⠃⡼⠃⣾⠟⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣷⢦⣄⠘⣿⣧⠀⢸⡇⠀⠀⠀⣧⠀⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣯⣾⢿⡇⠀⢠⣿⡆⠀⣸⠏⢀⡴⢛⣿⣿⣿⣿⣿⡿⢧⡀⣏⡼⠁⣠⠟⠀⠀⠀⠀⠀⡞⣹⣿⣿⣿⣿⣿⣷⠙⢧⣹⣽⠀⢸⠻⠘⣆⠀⣿⣤⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡟⠁⡿⢸⠀⣠⠟⠀⡇⠀⡏⠀⡾⠁⢸⣿⣿⣿⣿⣿⣷⠈⢳⡟⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⢿⢿⣿⣿⣿⣿⣿⠀⠘⠋⢻⠀⢸⠀⢠⢻⡄⡏⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⣾⡿⢿⣠⣿⠀⢂⢹⣸⡁⠀⠁⠀⠸⣿⡿⢉⠉⢹⡟⠀⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣾⡿⠋⢹⣿⡿⠀⠀⠀⠈⣇⡇⢀⡾⣼⣷⣧⡿⠀⠀⠀⠀⠀⠀⠀
⡆⠀⠀⠀⠀⢀⡿⠁⣾⢿⠈⣧⣸⡜⣷⡇⠀⠀⠀⠀⠙⠓⠒⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠋⠀⠀⠀⠀⠀⢻⡇⣸⠓⢡⣿⢹⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⢰⣿⠞⢷⡈⢻⣇⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠇⣠⠏⢣⣘⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣶⣫⣧⣤⣤⣝⣦⣙⢦⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠞⣉⣦⣤⣽⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⠿⢿⣒⣒⣉⠉⣿⡿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠓⠃⠳⣶⣒⠒⠉⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⣿⡟⠀⢀⡽⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣟⠀⢄⣀⣀⣙⣓⣦⣼⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠏⢀⣤⣎⡴⠿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣃⣘⣷⣌⣙⢿⣉⠉⠁⠈⢷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢣⣔⣯⣭⡵⠒⠐⣫⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠀⠀⣿⠛⠒⠛⠓⠚⠓⠆⠀⠈⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠩⣭⣶⡯⠶⠒⢻⢿⣾⠏⠙⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⢀⣠⣾⣋⣙⣲⣜⣦⡈⣦⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⣟⣥⡶⣼⠛⡏⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⠈⠻⣿⠉⠙⠛⠛⠮⢧⡄⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠛⠉⠉⣼⠋⢁⣴⣇⠀⠀⡏⠑⠲⣄⡀⠀⠀⠀⣀⣤⡶⣿⡿⣶⢹⣿⣰⣄⣈⠳⣄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣧⠞⠋⠀⣿⣄⡀⢰⠀⠀⢀⡌⠛⢻⣿⢿⢻⣿⣅⣿⣇⡿⢿⠛⢿⣌⠙⠛⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⡿⠈⠹⣮⡀⠀⠰⡇⢀⡆⣿⣾⠸⣿⠸⣡⠏⠀⢸⡇⠀⠉⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣀⡀⠀⠀⠀⠀⠀⠈
⡆⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡿⠋⣽⣿⣷⣦⣤⣄⡀⠀⠀⠀⢠⠇⠀⠀⠀⠙⢦⣀⡇⣸⡇⠃⣿⠀⣿⡟⠁⠀⠀⠘⢧⣤⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣤⡀⠈⠙⠢⣤⡤⣤⣀⣀
⡁⠀⢀⣤⡶⠶⣒⣚⣷⣿⣿⡇⠀⠙⢿⣿⣿⣿⣿⣿⣷⣶⣶⠋⠀⠀⠀⠀⠀⠀⠈⠙⠶⠯⡤⠟⠀⠉⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⠋⠀⠀⢀⣀⣸⣿⣶⣯⣽
⡇⢺⡏⠺⣿⣿⣿⣿⣿⣿⣿⣥⣤⣤⣀⡈⠛⢿⣿⣿⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣹⣿⣿⣿⣿⣿⣥⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⡿⠋⠀⠳⣾⣿⣉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⡤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿
⡇⠀⠀⠀⠈⠻⣿⣿⣷⣬⣝⣻⣛⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠉⠉⠛⠛⠦⣄⠀⠀⣠⠴⠛⠉⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⢿⡛⠛⣛⣋⣭⣴⣶⣶⣿
⡇⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣭⣿⣙⡛⠛⠿⢿⣿⣷⣦⡀⠀⠀⠈⠙⠋⠁⠀⠀⠀⣠⣾⣿⡿⠿⠟⢛⡛⣽⣿⣿⣯⣽⣿⣿⣿⣿⣷⣿⣿⣿⣿⡿⠟⠋⠉
⣧⣄⡀⠀⠀⠀⠀⣀⣤⠞⣿⣿⣿⣿⣿⣿⣝⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣝⠛⠳⢤⡀⠀⠀⠀⣠⡴⢛⣩⣥⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣿⣿⣿⠿⢛⡻⣇⡀⠀⠀⠀
⣿⣿⣿⣷⣶⣶⣾⣿⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠉⣧⣤⣴⡿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣈⠍⠈⣹⣶⣶⣶
⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡏⣇⣸⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡆⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡏⢹⡃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⠉⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠰⠬⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠰⠻⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠒⠂⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⢲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⢠⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢿⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫
⠂⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢸⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣾
⠀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣠⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⣾⣿

''' 

# import stuff
import os
import discord
import datetime
import random
from random import shuffle
from discord.ext import tasks, commands
from dotenv import load_dotenv

# load .env file contents
load_dotenv() 

# Get Xion bot token value
TOKEN = os.getenv('DISCORD_TOKEN')

 # Assign command prefix and all intents perms
bot = commands.Bot(command_prefix='*', intents = discord.Intents.all())

# Event that runs every time Xion is first loaded
@bot.event
async def on_ready():
    # Print ready message to console
    print(f'{bot.user} has entered the Round Room. Praise Kingdom Hearts.')
    
    # For each Discord server Xion is in
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # Test for sending ready message to Discord server chat
        '''
        if guild.id == 710204623394308106:
            await send_message(bot.get_channel(1263303758410940427), f'{bot.user} has entered the Round Room. Praise Kingdom Hearts.')
        '''
		
# Event that runs for every messsage sent in the server, but only responds to specific hard-coded messages
@bot.event
async def on_message(message):
    # Xion, don't read your own messages
    if message.author == bot.user:
        return
    
    # Meme messages #
    if message.content == 'I\'ll use this instead!':
        response = 'Roxas, that\'s a stick.'
        await send_message(message.channel,response)

    if message.content == 'Who am I supposed to eat ice cream with?':
        response = 'What the fuck is wrong with u'
        await send_message(message.channel,response)
    
    if message.content.casefold() == 'Skibidi Toilet'.casefold():
        response = ':skull: you\'re going straight to Kingdom Hearts for that one'
        await send_message(message.channel,response)        

    # Test for auto deleting messages from a specified user
    '''if message.author.id == 305783441943953419:
        await message.delete()
        response = 'To the Realm of Darkness with your bullshit.'
        await message.channel.send(response)
    '''
    

    await bot.process_commands(message)

# Useful method for having Xion send a message in custom commands/events
@bot.event
async def send_message(channel, message):
    await channel.send(message)

''' DOES NOT WORK - MUDAE CANT READ COMMANDS FROM OTHER BOTS
@tasks.loop(time=mudaeRollTimes)
async def mudae_rolls():
    mudaeChannel = bot.get_channel(1216546351081328671)
    print('Running mudae rolls...')
    await mudaeChannel.send('Free community rolls!')
    await mudaeChannel.send('$m')
'''

# Cool embedded message command to print out all of the members of Organization XIII and some details about each of them in a pretty looking way
@bot.command(name='orgxiii', help='Lists members of Organization XIII, the element they control, and type of Nobody they command.')
async def orgXIII(ctx):

    ''' Old stinky way just using text and markup
    orgXIIIList = [
        '### Organization XIII',
        '* I. Xemnas AKA Ansem (Xehanort), power over **Nothingness**, commands **Sorcerers**',
        '* II. Xigbar AKA Braig, power over **Space**, commands **Snipers**',
        '* III. Xaldin AKA Dilan, power over **Wind**, commands **Dragoons**',
        '* IV. Vexen AKA Even, power over **Ice**',
        '* V. Lexaeus AKA Aeleus, power over **Earth**',
        '* VI. Zexion AKA Ienzo, power over **Illusions**',
        '* VII. Saix AKA Isa, power over the **Moon**, commands **Berserkers**',
        '* VIII. Axel AKA Lea, power over **Fire**, commands **Assassins**',
        '* IX. Demyx, power over ***DANCE WATER DANCE***, commands **Dancers**',
        '* X. Luxord, power over **Time**, commands **Gamblers**',
        '* XI. Marluxia AKA Lauriam, power over **Flowers**, commands **Reapers**',
        '* XII. Larxene AKA Elrena, power over **Lightning**, commands **Ninjas**',
        '* XIII. Roxas AKA Sora, power over **Light**, commands **Samurai**',
        '* XIV. Xion AKA Replica No. i, power over **Light**'
    ]

    message = ''

    for orgXIIIMember in orgXIIIList:
        message += orgXIIIMember + '\n'

    await ctx.send(message)
    '''

    # New cool way using embedded messages
    embedOrgXIII = discord.Embed(title="Organization XIII", description="Seeking to complete Kingdom Hearts and become whole", color=0x808080) # 808080 - Hex code for the color grey
    embedOrgXIII.add_field(name="I. Xemnas", value="AKA Ansem (Xehanort), power over **Nothingness**, commands **Sorcerers**", inline=False)
    embedOrgXIII.add_field(name="II. Xigbar", value="AKA Braig, power over **Space**, commands **Snipers**", inline=False)
    embedOrgXIII.add_field(name="III. Xaldin", value="AKA Dilan, power over **Wind**, commands **Dragoons**", inline=False)
    embedOrgXIII.add_field(name="IV. Vexen", value="AKA Even, power over **Ice**", inline=False)
    embedOrgXIII.add_field(name="V. Lexaeus", value="AKA Aeleus, power over **Earth**", inline=False)
    embedOrgXIII.add_field(name="VI. Zexion", value="AKA Ienzo, power over **Illusions**", inline=False)
    embedOrgXIII.add_field(name="VII. Saix", value="AKA Isa, power over the **Moon**, commands **Berserkers**", inline=False)
    embedOrgXIII.add_field(name="VIII. Axel", value="AKA Lea, power over **Fire**, commands **Assassins**", inline=False)
    embedOrgXIII.add_field(name="IX. Demyx", value="Power over ***DANCE WATER DANCE***, commands **Dancers**", inline=False)
    embedOrgXIII.add_field(name="X. Luxord", value="Power over **Time**, commands **Gamblers**", inline=False)
    embedOrgXIII.add_field(name="XI. Marluxia", value="Marluxia AKA Lauriam, power over **Flowers**, commands **Reapers**", inline=False)
    embedOrgXIII.add_field(name="XII. Larxene", value="AKA Elrena, power over **Lightning**, commands **Ninjas**", inline=False)
    embedOrgXIII.add_field(name="XIII. Roxas", value="AKA Sora, power over **Light** and **Sticks**, commands **Samurai**", inline=False)
    embedOrgXIII.add_field(name="XIV. Xion", value="AKA Replica No. i, power over **Light**", inline=False)
    await ctx.send(embed=embedOrgXIII)


# Searches the KH wiki for an entered term, has to match the format of the KH Wiki URL format
@bot.command(name='khwiki', help='Searches for a specific term on the KH Wiki and sends the link to the webpage')
async def khwiki(ctx, *target):
    # Check if a parameter for the command was given or if its null/empty
    if target is None or not target:
        await ctx.send('Please specify a term to search for on the KH Wiki.')
        return
    
    khWikiLink = 'https://www.khwiki.com/' + '_'.join(target)

    await ctx.send(khWikiLink)

# Takes any name/word and turns into a Nobody styled name similar to the names of the Organization XIII members
@bot.command(name='nobodyname', help='Takes a word/name and Nobody-izes it (shuffles the letters and adds an X)')
async def nobody_name(ctx, target):
    # Check if a parameter for the command was given or if its null/empty
    if target is None or not target:
        await ctx.send('Please specify a word or name to create a Nobody name.')
        return
    
    # Choose a random spot to place the added X
    randomCharIndex = random.randint(0, len(target))

    # Create the Nobody name
    nobodyName = list(target) # initially create name as list of input string
    nobodyName.insert(randomCharIndex, 'x') # add the letter X to a random spot in the list
    shuffle(nobodyName) # shuffle the list contents
    nobodyName = ''.join(nobodyName) # re-join the characters from the list as a string

    # Make all characters in the name lowercase...
    nobodyName = nobodyName.lower()
    # ...then capitalize the first letter to make it look like a name
    nobodyName = nobodyName.capitalize()

    # Send Nobody name
    await ctx.send('Your Nobody name is ' + nobodyName)
        
# Runs Xion using the generated bot token
bot.run(TOKEN)