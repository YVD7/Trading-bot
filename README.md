# Trading-bot
Trading bot

# About 
    - This project is about trading bot which takes market data and of live market data and based on strategys it makes decisions buy and sell or intraday and exits after market close.


# Project setup commands
    * Create the folder on your system as < Project / As per preference >
    * Once the folder is created open the folder on location
        - On Windows:
            1. Double click on file address bar in the file manager and type "cmd"
            2. Once opend the cmd terminal follow through following commands

        - On Linux/MacOS/Unix:
            1. Create folder by name <Project / name as prefenrence>
            2. Once created the folder open the terminal on file location and 
                follow following commands

    1. Clone the repsitory

        ~$ git clone < "http link of repsitory" >

    
    ### Conda environment setup

    1.To Create new conda environment

        ~$ conda create -n <environment_name> python==<python version> -y

        for example:
            ~$ conda create -n dev python==3.12 -y

    2. To Activate Conda environment

        ~$ conda activate <environment_name>

        for example:
            ~$ conda activate dev

    3. To check python version
        
        ~$ python --version 
        
                or 

        ~$ python3 --version

    4. To check list of packages installed into environment

        ~$ pip list


    5. To install package or library into environment

        ~$ pip install <package name>

    6. To install "requirments.txt" file which hold list of packages to be installed

        ~$ pip install -r requirments.txt 

        
    

    ### Git commands for project after project installation to use
    
    1. pull command
        
        ~$ git pull origin < main / branch as created >

    2. initialize git

        ~$ git add .

    3. Comment 

        ~$ git commit -m "<comment>"

    4. Check status

        ~$ git status

    5. push command
        
        ~$ git push origin <branch you created / or main branch>

    
