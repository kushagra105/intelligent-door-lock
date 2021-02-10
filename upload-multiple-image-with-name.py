import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('kushagra.jpg','Kushagra Jaiswal'),
        ('prakhar.jpg','Prakhar Srivastava'),
        ('rishabh.jpg','Rishabh Maurya'),
        ('happy.jpg','Happy Maurya')
       ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('guest-images-collection',image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )
    #print(image[0])
    #print(image[1])
