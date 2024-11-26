"""
Xion.py - No. XIV but as a Discord bot this time, instead of a Replica

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

# Import stuff
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from Xion_Commands import Xion_Commands


# Declare Xion object (same type as Discord command bot)
class Xion(commands.Bot):
    # When Xion is ready, add the commands cog that contains most of her functionality
    async def on_ready(self):
        # Add cog for commands to Xion
        await self.add_cog(Xion_Commands(self))

        # For each Discord server Xion is in
        for guild in self.guilds:
            # Print the server name and server ID
            print(f"- {guild.name} (ID: {guild.id})")

        # Print ready message to console
        print(f"{self.user} has entered the Round Room. Praise Kingdom Hearts.")


# Main method for Xion
def main():
    # Load discord bot token environment variable (needed to run Xion)
    if load_dotenv():
        TOKEN = os.getenv("DISCORD_TOKEN")

        # Create Xion instance and run Xion with bot token
        bot = Xion(command_prefix="*", intents=discord.Intents.all())
        bot.run(TOKEN)
    else:
        print("There was an issue when loading the Discord bot token from the environment variables, stopping Xion")
        exit


# Make sure only main method is run
if __name__ == "__main__":
    main()
