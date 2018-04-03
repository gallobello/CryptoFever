#!/usr/bin/env python

     ########################################################################################
     #                                                                                      #
     #    This file is part of CryptoFever.                                                 #
     #                                                                                      #
     #    cryptofever is free software: you can redistribute it and/or modify               #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #  
     #    You should have received a copy of the GNU General Public License                 #
     #    along with CryptoFever.  If not, see <http://www.gnu.org/licenses/>.              #
     #                                                                                      #
     ########################################################################################


import sys
import atexit
from time import sleep 
sys.path.insert(0,"lib")
import cryptofever_lib
sys.dont_write_bytecode = True

if __name__ == "__main__":

    cryptofever_lib.UniversalCheck()  

    try:

        cryptofever_lib.Complete_Menu()

    except (KeyboardInterrupt, SystemExit):

        cryptofever_lib.clear()

        print("[CryptoFever] EXIT\n")
        


