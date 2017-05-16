import pathlib as pl
import os
import platform
import lib2to3


# ---- configuration test ----
configured = pl.Path("installation/miniconda.sh").is_file()
# ---- System Info ---------
o_system = platform.system()
architecture = platform.architecture()

# ---- path/url definition ----------------------------
miniconda_repo = "https://repo.continuum.io/miniconda/"
install_dir = os.curdir + "/installation"
miniconda_output = os.path.join(install_dir, "miniconda.sh")
requirements = "requirements.txt"

# ---- verbose --------------------------------------------------------
print()
print("      --------------------------------------------------------")
print("      |****************** Justintime SETUP ******************|")
print("      --------------------------------------------------------")
print()
print("Operating system found...")
print("OS: {0}".format(o_system + " " + architecture[0] + " " + architecture[1]))
print()
print("Setting up the configuration according to the operating system: ...")


# This part of the program will configure specific variables, such as
# miniconda binary, terminal behaviour etc.

if not configured:
    config_statements = []
    if o_system == "win32" or o_system == "cygwin":
        if architecture[0] == "32bit":
            miniconda_file = "Miniconda3-latest-Windows-x86.exe"
        else:
            miniconda_file = "Miniconda3-latest-Windows-x86_64.exe"

        miniconda_url = os.path.join(miniconda_repo, miniconda_file)
        miniconda_install = "wget -O" + miniconda_output + miniconda_url
        os.system("./installation/Gow-0.8.0.exe")
        os.system(miniconda_install)
        os.system(miniconda_output)

    else:
        if o_system == "Linux":
            if architecture[0] == "32bit":
                miniconda_file = "Miniconda3-latest-Linux-x86.sh"
            else:
                miniconda_file = "Miniconda3-latest-Linux-x86_64.sh"

        else:
            miniconda_file = "Miniconda3-latest-MacOSX-x86_64.sh"

        miniconda_url = os.path.join(miniconda_repo, miniconda_file)
        miniconda_install = "wget -O " + miniconda_output + " " + miniconda_url

        config_statements.append(miniconda_install)
        config_statements.append("chmod u+x " + miniconda_output)
        config_statements.append(miniconda_output)
        config_statements.append("exit")

        with open("config.sh", "w") as config:
            for statement in config_statements:
                config.write(statement)
                config.write("\n")

        os.system("chmod u+x config.sh")
        os.system("bash config.sh")
        print()
        print("Now, you must close this terminal and run `python setup.py` again.")

else:
    os.system("conda install pip")
    os.system("pip install -r " + requirements)
    os.system("rm config.sh installation/miniconda.sh")
