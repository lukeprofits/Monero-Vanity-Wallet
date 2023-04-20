# A SIMPLE WAY TO GENERATE VANITY MONERO WALLETS
# This is not as fast/efficient as other vanity generators because it uses the CLI wallet.
# It is however very simple to use, and is great for generating wallets with a few custom characters like:
# "XMR", "Lol", "Sam", "Tom", "Joe"
# If you are doing more than like 4 characters, you will probably want to use another generator.

# IMPORTS ##############################################################################################################
import os
import time
import subprocess
import concurrent.futures


# FUNCTIONS ############################################################################################################
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def monero_logo():
    print('''
                    k                                     d                   
                    0Kx                                 dOX                   
                    KMWKx                             dONMN                   
                    KMMMWKx                         dONMMMN                   
                    KMMMMMWKk                     d0NMMMMMN                   
                    KMMMMMMMMXk                 dKWMMMMMMMN                   
                    KMMMMMMMMMMXk             dKWMMMMMMMMMN                   
                    KMMMMMMMMMMMMXk         xKWMMMMMMMMMMMN                   
                    KMMMMMXkNMMMMMMXk     dKWMMMMMW00MMMMMN                   
                    KMMMMM0  xNMMMMMMXk dKWMMMMMWOc dMMMMMN                   
                    KMMMMM0    xNMMMMMMNWMMMMMWOc   dMMMMMN                   
                    KMMMMM0      dXMMMMMMMMMNkc     dMMMMMN                   
                    KMMMMM0        oXMMMMMNx;       dMMMMMN                   
KMMMMMMMMMMMMMMMMMMMMMMMMM0          dNMWk:         dMMMMMMMMMMMMMMMMMMMMMMMMK
KMMMMMMMMMMMMMMMMMMMMMMMMM0            o            dMMMMMMMMMMMMMMMMMMMMMMMMK
KMMMMMMMMMMMMMWNNNNNNNNNNNO                         oNNNNNNNNNNNNMMMMMMMMMMMMO''')


def make_wallet():
    global vanity_address_found
    try:
        os.remove(wallet_name)
    except:
        pass
    try:
        os.remove(f'{wallet_name}.keys')
    except:
        pass
    # Generate a new wallet using monero-wallet-cli
    command = f"{monero_wallet_cli_path} --generate-new-wallet {os.path.join(wallet_file_path, wallet_name)} --password '' --mnemonic-language English --command exit"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    worked_check = result.returncode
    if worked_check == 0:
        output_text = result.stdout
        wallet_address = output_text.split('Generated new wallet: ')[1].split('View key: ')[0].strip()
        view_key = output_text.split('View key: ')[1].split('*********************')[0].strip()
        seed = output_text.split(' of your immediate control.')[1].split('********')[0].strip().replace('\n', '')
        end_of_wallet = wallet_address[-(len(vanity_name)):]
        clear_console()
        print(f'Generating Wallets Matching "{vanity_name}":\n{wallet_address} \nThis one ends with: "{end_of_wallet}"\n\nTrying another...\n')
        if end_of_wallet.lower() == vanity_name.lower():
            clear_console()
            print(f'''\n[  FOUND VANITY WALLET:  ]\n')
            wallet_address: {wallet_address}
            view_key: {view_key}
            seed: {seed}\n\n
            This info has been saved to the text file "VANITY_WALLET.txt".\n
            ==============================================================================''')
            print(f'\n\n Please consider donating even a few cents to the creator of this software: \n\n{developer_wallet}\n==============================================================================')

            with open(file='VANITY_WALLET.txt', mode='a', encoding='utf-8') as f:
                f.write(f'wallet_address: {wallet_address}\nview_key: {view_key}\nseed: {seed}\nNo password was added to this wallet, but you have the seed so you can set one.\n\n')

            vanity_address_found = True
        else:
            vanity_address_found = False


# VARIABLES ############################################################################################################
monero_wallet_cli_path = '' + 'monero-wallet-cli.exe'  # path to your monero-wallet-cli executable
wallet_name = 'my_wallet'
wallet_file_path = ''  # Update this path to the location where you want to save the wallet file
number_of_threads = 16
executor = concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads)

developer_wallet = '4At3X5rvVypTofgmueN9s9QtrzdRe5BueFrskAZi17BoYbhzysozzoMFB6zWnTKdGC6AxEAbEE5czFR3hbEEJbsm4hCeX2S'


# START PROGRAM ########################################################################################################
clear_console()

# Print stuff to the screen
monero_logo()
time.sleep(1)
print('''
==============================================================================
                  Vanity Wallet Generator - By Luke Profits                
==============================================================================''')
time.sleep(1.5)
print('This WILL NOT WORK if the Monero CLI Wallet files are not in the same directory as this program.\n')
print('Get the Monero CLI Wallet files here: https://www.getmonero.org/downloads/#cli\n')
time.sleep(2)
print('NOTE: Monero uses Base58 which does not include the visually similar characters: \n\n"0" (Zero), "O" (Capital o), "I" (Capital i), and "l" (lowercase L)\n')
print('This vanity generator generates your vanity text at the END of the wallet rather than the beginning.')
print('(Because all Monero wallets start with a "4", and the 2nd character is usually a 1, 3, 7, or A.)\n')
time.sleep(3)
print('==============================================================================')
print(f'\nPlease consider donating XMR (even a few cents) to the developer of this generator:\n\n{developer_wallet}\n')
print('==============================================================================')
time.sleep(5)

# Get the vanity name to generate from the user
vanity_name = input('\nPlease enter the vanity letters that you want the end of your wallet to have: \n\n')

# Loop until we find it
vanity_address_found = False
while not vanity_address_found:
    executor.submit(make_wallet)  # Multi-threaded to make it faster
    time.sleep(0.025)  # This makes the visuals less glitchy (two threads won't print at the same time as much)

input('')
input('')
