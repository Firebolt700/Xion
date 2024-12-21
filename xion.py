"""
xion.py - No. XIV but as a Discord bot this time, instead of a Replica

Who else would we have ice cream with?

Started on: 2024-07-17

Written by Firebolt and ItsDerPing

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

"""

### Import stuff
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands import XionCommands


### Xion
# Declare Xion object (same type as Discord command bot)
class Xion(commands.Bot):
    # When Xion is finished starting, print startup messages to console and add the Xion_Commands cog module to unlock Xion_Commands functions
    async def on_ready(self):
        # For each Discord server Xion is in
        for guild in self.guilds:
            # Print the server name and server ID
            print(f"- {guild.name} (ID: {guild.id})")

        # Print ready message to console
        print(f"{self.user} has entered the Round Room. Praise Kingdom Hearts.")

        # Add Xion_Commands cog to Xion bot
        await self.add_cog(XionCommands(self))


# Main method for Xion
def main():
    # Load Discord bot token environment variable (needed to run Xion)
    if load_dotenv() and os.getenv("DISCORD_TOKEN") is not None:
        # Get Discord token value from .env
        TOKEN = os.getenv("DISCORD_TOKEN")

        # Create discord.Bot Xion object instance and run Xion with Discord bot token
        # command_prefix and intents must be declared in object instance creation, NOT set as a property in __init__
        bot = Xion(command_prefix="*", intents=discord.Intents.all())
        bot.run(TOKEN)

    # Couldn't find either the .env file or the DISCORD_TOKEN value is missing from the .env file
    else:
        print("Unable to load bot token.")
        print("Make sure .env exists and DISCORD_TOKEN has a value in it.")
        print()


# Make sure only main method is run
if __name__ == "__main__":
    main()
