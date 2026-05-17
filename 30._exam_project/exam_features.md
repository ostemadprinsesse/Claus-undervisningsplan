




# New feature for your application

Besides handing in you already made and deployed application, you should include a new feature.

## Database Migration
You have expressed concerns to your customer, the owner of the Awesome Recipe Cookbook, that a growing number of users would make the application slow if it stays as it is built right now. This could in the future be solved by scaling the number of VMs you use.

This will make your current database architecture a poor choice — for example, having a single SQLite database file on each backend VM is not a good solution. A better approach would be to have a dedicated VM with a database installed on it, that all future backend VMs can read from and write to.

Your job is to create this new feature in your application.

This is a large feature, so it is a good idea to plan it in advance and agree on who in the group does what.

You should document this migration in a way that makes it possible for the teacher and examiner to follow your process. Be sure to focus on DevOps, since that is largely what your exam is about.

Even though a DevOps principle is to avoid long-lived branches, it would in this case — for the sake of the exam — be a good idea to preserve your branches related to this feature. It will make it easier to evaluate what you did. (Note: this does not apply to the rest of your application.)


   
