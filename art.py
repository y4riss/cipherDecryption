from random import choice

ascii_art = [
    """
      ________     ____      _____     ____   ______    __      __  _____    ________  
     (___  ___)   / __ \    / ___/    / ___) (   __ \   ) \    / ( (  __ \  (___  ___) 
         ) )     / /  \ \  ( (__     / /      ) (__) )   \ \  / /   ) )_) )     ) )    
        ( (     ( ()  () )  ) __)   ( (      (    __/     \ \/ /   (  ___/     ( (     
     __  ) )    ( ()  () ) ( (      ( (       ) \ \  _     \  /     ) )         ) )    
    ( (_/ /      \ \__/ /   \ \___   \ \___  ( ( \ \_))     )(     ( (         ( (     
     \___/        \____/     \____\   \____)  )_) \__/     /__\    /__\        /__\                                                                                 
    """,
    """
         _    ___    _____    ____   ____   __   __  ____    _____ 
        | |  / _ \  | ____|  / ___| |  _ \  \ \ / / |  _ \  |_   _|
     _  | | | | | | |  _|   | |     | |_) |  \ V /  | |_) |   | |  
    | |_| | | |_| | | |___  | |___  |  _ <    | |   |  __/    | |  
     \___/   \___/  |_____|  \____| |_| \_\   |_|   |_|       |_|  
                                                               
    """,
    """
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ 
          ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     
          ▐░▌    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     
          ▐░▌    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     
          ▐░▌    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     
          ▐░▌    ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌     
     ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌      ▐░▌     ▐░▌               ▐░▌     
    ▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌     
     ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀                 ▀      
                                                                                                        
    """,
    """
           █████    ███████    ██████████   █████████  ███████████   █████ █████ ███████████  ███████████
          ░░███   ███░░░░░███ ░░███░░░░░█  ███░░░░░███░░███░░░░░███ ░░███ ░░███ ░░███░░░░░███░█░░░███░░░█
           ░███  ███     ░░███ ░███  █ ░  ███     ░░░  ░███    ░███  ░░███ ███   ░███    ░███░   ░███  ░ 
           ░███ ░███      ░███ ░██████   ░███          ░██████████    ░░█████    ░██████████     ░███    
           ░███ ░███      ░███ ░███░░█   ░███          ░███░░░░░███    ░░███     ░███░░░░░░      ░███    
     ███   ░███ ░░███     ███  ░███ ░   █░░███     ███ ░███    ░███     ░███     ░███            ░███    
    ░░████████   ░░░███████░   ██████████ ░░█████████  █████   █████    █████    █████           █████   
     ░░░░░░░░      ░░░░░░░    ░░░░░░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░    ░░░░░           ░░░░░    
                                                                                                                                                                                           
    """,
    """
         ▄█  ▄██████▄     ▄████████  ▄████████    ▄████████ ▄██   ▄      ▄███████▄     ███     
        ███ ███    ███   ███    ███ ███    ███   ███    ███ ███   ██▄   ███    ███ ▀█████████▄ 
        ███ ███    ███   ███    █▀  ███    █▀    ███    ███ ███▄▄▄███   ███    ███    ▀███▀▀██ 
        ███ ███    ███  ▄███▄▄▄     ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███   ███    ███     ███   ▀ 
        ███ ███    ███ ▀▀███▀▀▀     ███        ▀▀███▀▀▀▀▀   ▄██   ███ ▀█████████▀      ███     
        ███ ███    ███   ███    █▄  ███    █▄  ▀███████████ ███   ███   ███            ███     
        ███ ███    ███   ███    ███ ███    ███   ███    ███ ███   ███   ███            ███     
    █▄ ▄███  ▀██████▀    ██████████ ████████▀    ███    ███  ▀█████▀   ▄████▀         ▄████▀   
    ▀▀▀▀▀▀                                       ███    ███                                    
    """,
    """
      888888  .d88888b.  8888888888 .d8888b.  8888888b. Y88b   d88P 8888888b. 88888888888 
        "88b d88P" "Y88b 888       d88P  Y88b 888   Y88b Y88b d88P  888   Y88b    888     
         888 888     888 888       888    888 888    888  Y88o88P   888    888    888     
         888 888     888 8888888   888        888   d88P   Y888P    888   d88P    888     
         888 888     888 888       888        8888888P"     888     8888888P"     888     
         888 888     888 888       888    888 888 T88b      888     888           888     
         88P Y88b. .d88P 888       Y88b  d88P 888  T88b     888     888           888     
         888  "Y88888P"  8888888888 "Y8888P"  888   T88b    888     888           888     
       .d88P                                                                              
     .d88P"                                                                               
    888P"                                                                                 
    """,
]


def get_ascii_art():
    print(choice(ascii_art))
