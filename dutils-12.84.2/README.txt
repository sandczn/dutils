


dutils - developed by formik, deadly, benitas

How to setup dutils


1. Ensure Python 3.11+ is installed
2. Ensure PIP is installed and up to date
3. Ensure Python and PIP are added to your System's PATH Variable
4. Run the following two commands in command prompt:

	python -m pip uninstall discord.py
	python -m pip install -U discord.py-self

	### If you get an error saying "Index Out of Bounds" when trying to run your token, you may try this command 
	
		pip install git+https://github.com/dolfies/discord.py-self.git

	### Solution taken from (https://www.reddit.com/r/Discord_selfbots/comments/1ashglw/indexerror_list_index_out_of_range/) -> (https://github.com/dolfies/discord.py-self/issues/659#issuecomment-1935174445)

5. Edit the msg.txt file and input a message for the "spam" command to find and spam
6. Open the config.json file and configure the required settings
	For example:

		"token_file_path" : "./mytoken.txt",
	
7. Ensure the following files remain together in the same directory (folder):
	- main.py
	- config.json
	- dutils-{version}-patch.txt
	----> (This file must remain, but you may delete the Markdown version of this file which has the ".md" file extension)

8. To run the program, use the Python interpreter to run the dutils.py file
9. To use dutils, open discord and type a command prefixed with "d." (excluding the quotation marks)
10. type d.help for help

If you want dutils to automatically restart itself after each "d.term" (termination) or error that causes it to crash, you can run the "runner.py" script. This script must be in the same directory as your "dutils.py" and "config.json" files.






