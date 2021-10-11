About an postmortem.

Summary
It happened on the night of 01/10/2021. The web server that is responsible for serving a Wordpress portal stopped working from 12:00 am to approximately 12:25 am (UTC-5). After a quick check we noticed that the service returned the following message: "Error 500 - Internal server error". What's going on, we ask ourselves as we look at each other. 
I receive a couple of phone calls from the area in charge of delivery and help desk, indicating that customers cannot make purchases through the portal. 100% of the users are affected. The root cause is due to one of the Wordpress configuration files not being found by the web service causing it to crash.

Timeline:
12:00 am - The problem was reported via a phone call notifying that our website was down.
12:02 am - I quickly perform a query (curl -sI 127.0.0.1) which returns an error 500. This confirms that the server is responding however we have a problem with the services it handles.
12:04 am - Using the 'top' command, I look at the processes running. There are two processes running towards the Apache service, one with the user "root" and one with "www-data".
12:06 am - I now use the 'strace' PID (process identifier) command for root. I get a continuous timeout response.
12:08 am - I log into another terminal, query with the curl command with no response. I do the same for 'www-data'. I get a response in the window where the "strace" command is executed.
12:11 am - I search for the possible bug until I find the problem (an error is shown with the value -1 inside strace). The possible error is shown in a line that references a file with extension ".phpp". The line of code: "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' ); (No such file or directory))."
12:18 am - I try to locate "class-wp-locale.phpp" and it does not exist, but "class-wp-locale.php" does so I deduce that it is a typo. I check the "wp-settings.php" file to make the necessary adjustment.
12:23 am - In the organization we have a policy to use "Puppet" for deploying changes in production. I prepare a script to modify this file, the statement is: "sed -i 's/.phpp/.php/g". Using Puppet the replacement is made in the file "/var/www/html/wp-settings.php". (the path for the "sed" command must be specified, in this case "/bin").
12:25 am - After making the change, I perform a curl -sI query (127.0.0.1), get a successful response (200). I communicate to the other areas making it known that the incident has been overcome.

Impact:
100% of our customers who attempted to access the porting during the time the service was unavailable were affected.

Root Cause:
The cause of the problem was due to one of the Wordpress configuration files making mention of another file with an incorrect extension, ".phpp" instead of ".php", this allowed the Apache service on our web server to function.

Corrective actions:
Replacing the erroneous line containing the text ".phpp" with ".php" inside the Wordpress configuration file we managed to resume the web service and consequently the web portal. We used the top command (to identify the processes), strace (to find the error), sed (to replace the erroneous extension), and puppet (to automate scripts, in case an incident has to be corrected on multiple servers).

Preventive actions:
Remind the area making the scripts to use the test servers before their release to production, this to check that the change does not affect the operational services. The area in charge of the deployment must follow up the service involved. Before making the requested change, make a backup of the original files.

Good advice:
A post-mortem explains how a problem was resolved. But if you really want to make a major change in a project or organization, you need to know your own and other people's mistakes and successes. A post-mortem is a very powerful tool; it is a great opportunity to learn about yourself and other people. Knowing this will help make the processes involved more efficient. This is the best way to take it.
