<h1>Quick tool for dumping a MySQL database and automatically uploading it into an S3 bucket</h1>

<b>Make sure you have mysql-client installed<b>

You must also set following ENV variables: 
<li>MYSQLHOST</li>
<li>MYSQLUSER</li>
<li>MYSQLPASSWORD</li>
<li>MYSQLDATABASE</li>
<li>AWS_ACCESS_KEY</li>
<li>AWS_SECRET_ACCESS_KEY</li>
<li>AWS_BUCKET_REGION</li>
<li>AWS_BUCKET_NAME</li>
<br>
Afterwards, just hit em' with a python3 app.py or schedule this as a chronjob and boom, hassle-free database dumps. 

Also, keep in mind after the .sql is uploaded to the S3 bucket, the local copy will automatically delete itself in order to not waste space :)
