Delivery Guy
==============

Deliveryguy is a tool to deploy config files and other kind of files and execute scripts before and after the copy.
--------------

**CONFIG**

In the repo section you can optionally specify a repo to pull, this will be skipped if you specify a repo by argument when you launch the tool.
In instructions you have:

**TARGET:** Host target, use * for all

**SOURCE:** File path that have to be copied

**DESTINATION:** Destination of file

**RUN_BEFORE:** Script to run before copy

**RUN_AFTER:** Script to run after copy

**MD5_CHECK:** If enabled check the MD5 of the 2 files before execute the copy and proceed only if they are different.

**USAGE**

The right procedure is to create a repo for a customer that contain all the files you want to copy, the scripts you need to execute if any and the instructions.json file that contain the list of task to execute.
You can chose if pass the tool the config file that contain the repo to pull or directly pass the repo as parameter but in this case you have to include  instructions.json inside the repo because the app will look for this file inside.
 
The application is usually installed automatically by puppet on the standard path: /etc/infomentum/tools/deliveryguy, to run the application just call the script and pass as optional parameter the full instructions.json path or the repo to pull

CONFIG FILE:

	/usr/bin/deliveryguy -config <instructions_path>

REPO:

	/usr/bin/deliveryguy -repo <repo_url>