Summary:

On 1st March, 2023 6:00AM UTC, Mainmarket online experienced an outage that lasted for 10 days. During this time, customers were unable to access the website, resulting in significant disruption to service. The root cause of the outage was determined to be a combination of resource over-usage and malware infestation of three files.

Impact:

The outage had a major impact on Mainmarket's customers, as they were unable to access the website for the entire duration of the outage. This resulted in a loss of revenue and damaged customer relationships. According to our analysis, approximately 10,000 users were affected by the outage.

Root Cause:

Upon further investigation, it was discovered that the root cause of the outage was due to bot activity on the website, which caused an increase in resource usage and triggered the malware infestation. To prevent similar incidents from occurring in the future, we have implemented additional security measures and regular monitoring to detect any suspicious activity. We apologize for any inconvenience caused and are committed to ensuring the reliability and security of our services.

Timeline:

6:00AM UTC 01/03/2023: The issue was first detected by the operations officer through regular business operations.
Initial actions taken included attempting a simple optimization and repair of the database, which did not resolve the issue.
Further investigation was conducted, with focus on the resource usage and malware infestation of three files.
There were no misleading investigation/debugging paths taken.
The incident was escalated to the lead developer and the security team for additional support.
The root cause was determined to be bot activity on the website, which caused an increase in resource usage and triggered the malware infestation of the three files.
The affected files were deleted, and bots hitting the website more than 1000 times in 24 hours were blocked.
The service was restored by the 11th day.

Root Cause:

The root cause of the outage was determined to be bot activity on the website. These bots were hitting the website more than 1000 times in 24 hours, which caused a significant increase in resource usage. This increase in resource usage triggered the malware infestation of three files, which ultimately led to the outage. The bots were able to bypass existing security measures and gain access to the website, which allowed them to cause the disruption.

Resolution:

To fix the issue, the affected files were deleted, and the bots were blocked from accessing the website. The lead developer and security team provided additional support to ensure that the appropriate measures were taken to prevent a recurrence of the issue. In addition, regular monitoring was implemented to detect any suspicious activity and prevent future bot activity. These measures ensured that the website was fully restored by the 11th day, with all customers being able to access the website as normal.

Corrective and Preventative Measures:

To prevent a recurrence of the outage, the following corrective and preventative measures have been identified:

Bot detection and blocking: Additional measures to detect and block bots from accessing the website will be implemented. This includes adding more security layers to the website to prevent bots from bypassing security measures and gaining unauthorized access. Regular monitoring will also be conducted to detect and block any bots attempting to access the website.

TODO:

Implement a Web Application Firewall (WAF) to block suspicious traffic and prevent bots from bypassing security measures.
Implement rate limiting and bot detection measures to limit the number of requests that bots can make to the website.
Regularly review and update the security protocols to ensure that they are up-to-date and effective.
Database optimization: The database will be optimized to reduce the load on the server and improve performance. 
This includes identifying and removing unnecessary database tables and optimizing queries to reduce server load.


TODO:

-Conduct a database audit to identify and remove unnecessary tables and data.
-Optimize database queries to reduce the load on the server.
-Implement regular maintenance and monitoring of the database to ensure optimal performance.


Resource monitoring: The server resources will be monitored regularly to ensure that they are being used efficiently and effectively. This includes monitoring server CPU usage, memory usage, and network usage to identify any abnormalities
 or potential issues.

TODO:

-Implement server monitoring tools to track server resource usage.
-Configure alerts to notify the team when resource usage exceeds certain thresholds.
-Regularly review server logs to identify any issues that may be impacting server performance.


Incident response planning: An incident response plan will be developed to ensure that the team can respond quickly and effectively to any future incidents. This includes establishing clear roles and responsibilities, creating a communication plan, and conducting regular incident response training.

TODO:

-Develop an incident response plan that outlines the steps to be taken in the event of an incident.
-Assign clear roles and responsibilities to team members.
-Conduct regular incident response training to ensure that the team is prepared to respond to any incident.
-By implementing these corrective and preventative measures, we aim to ensure the reliability and security of our 
services, and minimize the risk of future outages. We are committed to providing the highest level of service to our
customers and will continue to review and update our processes and procedures to ensure that we are meeting their needs.
