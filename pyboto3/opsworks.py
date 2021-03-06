'''

The MIT License (MIT)

Copyright (c) 2016 WavyCloud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

def assign_instance(InstanceId=None, LayerIds=None):
    """
    Assign a registered instance to a layer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.assign_instance(
        InstanceId='string',
        LayerIds=[
            'string',
        ]
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    :type LayerIds: list
    :param LayerIds: [REQUIRED]\nThe layer ID, which must correspond to a custom layer. You cannot assign a registered instance to a built-in layer.\n\n(string) --\n\n

    :returns: 
    InstanceId (string) -- [REQUIRED]
    The instance ID.
    
    LayerIds (list) -- [REQUIRED]
    The layer ID, which must correspond to a custom layer. You cannot assign a registered instance to a built-in layer.
    
    (string) --
    
    
    
    """
    pass

def assign_volume(VolumeId=None, InstanceId=None):
    """
    Assigns one of the stack\'s registered Amazon EBS volumes to a specified instance. The volume must first be registered with the stack by calling  RegisterVolume . After you register the volume, you must call  UpdateVolume to specify a mount point before calling AssignVolume . For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.assign_volume(
        VolumeId='string',
        InstanceId='string'
    )
    
    
    :type VolumeId: string
    :param VolumeId: [REQUIRED]\nThe volume ID.\n

    :type InstanceId: string
    :param InstanceId: The instance ID.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def associate_elastic_ip(ElasticIp=None, InstanceId=None):
    """
    Associates one of the stack\'s registered Elastic IP addresses with a specified instance. The address must first be registered with the stack by calling  RegisterElasticIp . For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_elastic_ip(
        ElasticIp='string',
        InstanceId='string'
    )
    
    
    :type ElasticIp: string
    :param ElasticIp: [REQUIRED]\nThe Elastic IP address.\n

    :type InstanceId: string
    :param InstanceId: The instance ID.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def attach_elastic_load_balancer(ElasticLoadBalancerName=None, LayerId=None):
    """
    Attaches an Elastic Load Balancing load balancer to a specified layer. AWS OpsWorks Stacks does not support Application Load Balancer. You can only use Classic Load Balancer with AWS OpsWorks Stacks. For more information, see Elastic Load Balancing .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_elastic_load_balancer(
        ElasticLoadBalancerName='string',
        LayerId='string'
    )
    
    
    :type ElasticLoadBalancerName: string
    :param ElasticLoadBalancerName: [REQUIRED]\nThe Elastic Load Balancing instance\'s name.\n

    :type LayerId: string
    :param LayerId: [REQUIRED]\nThe ID of the layer to which the Elastic Load Balancing instance is to be attached.\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def clone_stack(SourceStackId=None, Name=None, Region=None, VpcId=None, Attributes=None, ServiceRoleArn=None, DefaultInstanceProfileArn=None, DefaultOs=None, HostnameTheme=None, DefaultAvailabilityZone=None, DefaultSubnetId=None, CustomJson=None, ConfigurationManager=None, ChefConfiguration=None, UseCustomCookbooks=None, UseOpsworksSecurityGroups=None, CustomCookbooksSource=None, DefaultSshKeyName=None, ClonePermissions=None, CloneAppIds=None, DefaultRootDeviceType=None, AgentVersion=None):
    """
    Creates a clone of a specified stack. For more information, see Clone a Stack . By default, all parameters are set to the values used by the parent stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.clone_stack(
        SourceStackId='string',
        Name='string',
        Region='string',
        VpcId='string',
        Attributes={
            'string': 'string'
        },
        ServiceRoleArn='string',
        DefaultInstanceProfileArn='string',
        DefaultOs='string',
        HostnameTheme='string',
        DefaultAvailabilityZone='string',
        DefaultSubnetId='string',
        CustomJson='string',
        ConfigurationManager={
            'Name': 'string',
            'Version': 'string'
        },
        ChefConfiguration={
            'ManageBerkshelf': True|False,
            'BerkshelfVersion': 'string'
        },
        UseCustomCookbooks=True|False,
        UseOpsworksSecurityGroups=True|False,
        CustomCookbooksSource={
            'Type': 'git'|'svn'|'archive'|'s3',
            'Url': 'string',
            'Username': 'string',
            'Password': 'string',
            'SshKey': 'string',
            'Revision': 'string'
        },
        DefaultSshKeyName='string',
        ClonePermissions=True|False,
        CloneAppIds=[
            'string',
        ],
        DefaultRootDeviceType='ebs'|'instance-store',
        AgentVersion='string'
    )
    
    
    :type SourceStackId: string
    :param SourceStackId: [REQUIRED]\nThe source stack ID.\n

    :type Name: string
    :param Name: The cloned stack name.

    :type Region: string
    :param Region: The cloned stack AWS region, such as 'ap-northeast-2'. For more information about AWS regions, see Regions and Endpoints .

    :type VpcId: string
    :param VpcId: The ID of the VPC that the cloned stack is to be launched into. It must be in the specified region. All instances are launched into this VPC, and you cannot change the ID later.\n\nIf your account supports EC2 Classic, the default value is no VPC.\nIf your account does not support EC2 Classic, the default value is the default VPC for the specified region.\n\nIf the VPC ID corresponds to a default VPC and you have specified either the DefaultAvailabilityZone or the DefaultSubnetId parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.\nIf you specify a nondefault VPC ID, note the following:\n\nIt must belong to a VPC in your account that is in the specified region.\nYou must specify a value for DefaultSubnetId .\n\nFor more information about how to use AWS OpsWorks Stacks with a VPC, see Running a Stack in a VPC . For more information about default VPC and EC2 Classic, see Supported Platforms .\n

    :type Attributes: dict
    :param Attributes: A list of stack attributes and values as key/value pairs to be added to the cloned stack.\n\n(string) --\n(string) --\n\n\n\n

    :type ServiceRoleArn: string
    :param ServiceRoleArn: [REQUIRED]\nThe stack AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. If you create a stack by using the AWS OpsWorks Stacks console, it creates the role for you. You can obtain an existing stack\'s IAM ARN programmatically by calling DescribePermissions . For more information about IAM ARNs, see Using Identifiers .\n\nNote\nYou must set this parameter to a valid service role ARN or the action will fail; there is no default value. You can specify the source stack\'s service role ARN, if you prefer, but you must do so explicitly.\n\n

    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .

    :type DefaultOs: string
    :param DefaultOs: The stack\'s operating system, which must be set to one of the following.\n\nA supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2018.03 , Amazon Linux 2017.09 , Amazon Linux 2017.03 , Amazon Linux 2016.09 , Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .\nA supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .\nCentOS Linux 7\nRed Hat Enterprise Linux 7\nMicrosoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .\nA custom AMI: Custom . You specify the custom AMI you want to use when you create instances. For more information about how to use custom AMIs with OpsWorks, see Using Custom AMIs .\n\nThe default option is the parent stack\'s operating system. For more information about supported operating systems, see AWS OpsWorks Stacks Operating Systems .\n\nNote\nYou can specify a different Linux operating system for the cloned stack, but you cannot change from Linux to Windows or Windows to Linux.\n\n

    :type HostnameTheme: string
    :param HostnameTheme: The stack\'s host name theme, with spaces are replaced by underscores. The theme is used to generate host names for the stack\'s instances. By default, HostnameTheme is set to Layer_Dependent , which creates host names by appending integers to the layer\'s short name. The other themes are:\n\nBaked_Goods\nClouds\nEurope_Cities\nFruits\nGreek_Deities_and_Titans\nLegendary_creatures_from_Japan\nPlanets_and_Moons\nRoman_Deities\nScottish_Islands\nUS_Cities\nWild_Cats\n\nTo obtain a generated host name, call GetHostNameSuggestion , which returns a host name based on the current theme.\n

    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: The cloned stack\'s default Availability Zone, which must be in the specified region. For more information, see Regions and Endpoints . If you also specify a value for DefaultSubnetId , the subnet must be in the same zone. For more information, see the VpcId parameter description.

    :type DefaultSubnetId: string
    :param DefaultSubnetId: The stack\'s default VPC subnet ID. This parameter is required if you specify a value for the VpcId parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for DefaultAvailabilityZone , the subnet must be in that zone. For information on default values and when this parameter is required, see the VpcId parameter description.

    :type CustomJson: string
    :param CustomJson: A string that contains user-defined, custom JSON. It is used to override the corresponding default stack configuration JSON values. The string should be in the following format:\n\n'{\\'key1\\': \\'value1\\', \\'key2\\': \\'value2\\',...}'\nFor more information about custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes\n

    :type ConfigurationManager: dict
    :param ConfigurationManager: The configuration manager. When you clone a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.\n\nName (string) --The name. This parameter must be set to 'Chef'.\n\nVersion (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.\n\n\n

    :type ChefConfiguration: dict
    :param ChefConfiguration: A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see Create a New Stack .\n\nManageBerkshelf (boolean) --Whether to enable Berkshelf.\n\nBerkshelfVersion (string) --The Berkshelf version.\n\n\n

    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: Whether to use custom cookbooks.

    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack\'s layers.\nAWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With UseOpsworksSecurityGroups you can instead provide your own custom security groups. UseOpsworksSecurityGroups has the following settings:\n\nTrue - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it but you cannot delete the built-in security group.\nFalse - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate Amazon Elastic Compute Cloud (Amazon EC2) security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.\n\nFor more information, see Create a New Stack .\n

    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: Contains the information required to retrieve an app or cookbook from a repository. For more information, see Adding Apps or Cookbooks and Recipes .\n\nType (string) --The repository type.\n\nUrl (string) --The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .\n\nUsername (string) --This parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Username to the appropriate IAM access key ID.\nFor HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.\n\n\nPassword (string) --When included in a request, the parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Password to the appropriate IAM secret access key.\nFor HTTP bundles and Subversion repositories, set Password to the password.\n\nFor more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nSshKey (string) --In requests, the repository\'s SSH key.\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nRevision (string) --The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.\n\n\n

    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see Using SSH to Communicate with an Instance and Managing SSH Access . You can override this setting by specifying a different key pair, or no key pair, when you create an instance .

    :type ClonePermissions: boolean
    :param ClonePermissions: Whether to clone the source stack\'s permissions.

    :type CloneAppIds: list
    :param CloneAppIds: A list of source stack app IDs to be included in the cloned stack.\n\n(string) --\n\n

    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: The default root device type. This value is used by default for all instances in the cloned stack, but you can override it when you create an instance. For more information, see Storage for the Root Device .

    :type AgentVersion: string
    :param AgentVersion: The default AWS OpsWorks Stacks agent version. You have the following options:\n\nAuto-update - Set this parameter to LATEST . AWS OpsWorks Stacks automatically installs new agent versions on the stack\'s instances as soon as they are available.\nFixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack\'s instances.\n\nThe default setting is LATEST . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.\n\nNote\nYou can also specify an agent version when you create or update an instance, which overrides the stack\'s default setting.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackId': 'string'
}


Response Structure

(dict) --
Contains the response to a CloneStack request.

StackId (string) --
The cloned stack ID.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'StackId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_app(StackId=None, Shortname=None, Name=None, Description=None, DataSources=None, Type=None, AppSource=None, Domains=None, EnableSsl=None, SslConfiguration=None, Attributes=None, Environment=None):
    """
    Creates an app for a specified stack. For more information, see Creating Apps .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_app(
        StackId='string',
        Shortname='string',
        Name='string',
        Description='string',
        DataSources=[
            {
                'Type': 'string',
                'Arn': 'string',
                'DatabaseName': 'string'
            },
        ],
        Type='aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
        AppSource={
            'Type': 'git'|'svn'|'archive'|'s3',
            'Url': 'string',
            'Username': 'string',
            'Password': 'string',
            'SshKey': 'string',
            'Revision': 'string'
        },
        Domains=[
            'string',
        ],
        EnableSsl=True|False,
        SslConfiguration={
            'Certificate': 'string',
            'PrivateKey': 'string',
            'Chain': 'string'
        },
        Attributes={
            'string': 'string'
        },
        Environment=[
            {
                'Key': 'string',
                'Value': 'string',
                'Secure': True|False
            },
        ]
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :type Shortname: string
    :param Shortname: The app\'s short name.

    :type Name: string
    :param Name: [REQUIRED]\nThe app name.\n

    :type Description: string
    :param Description: A description of the app.

    :type DataSources: list
    :param DataSources: The app\'s data source.\n\n(dict) --Describes an app\'s data source.\n\nType (string) --The data source\'s type, AutoSelectOpsworksMysqlInstance , OpsworksMysqlInstance , RdsDbInstance , or None .\n\nArn (string) --The data source\'s ARN.\n\nDatabaseName (string) --The database name.\n\n\n\n\n

    :type Type: string
    :param Type: [REQUIRED]\nThe app type. Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks Stacks deploys an application to those instances that are members of the corresponding layer. If your app isn\'t one of the standard types, or you prefer to implement your own Deploy recipes, specify other .\n

    :type AppSource: dict
    :param AppSource: A Source object that specifies the app repository.\n\nType (string) --The repository type.\n\nUrl (string) --The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .\n\nUsername (string) --This parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Username to the appropriate IAM access key ID.\nFor HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.\n\n\nPassword (string) --When included in a request, the parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Password to the appropriate IAM secret access key.\nFor HTTP bundles and Subversion repositories, set Password to the password.\n\nFor more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nSshKey (string) --In requests, the repository\'s SSH key.\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nRevision (string) --The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.\n\n\n

    :type Domains: list
    :param Domains: The app virtual host settings, with multiple domains separated by commas. For example: \'www.example.com, example.com\'\n\n(string) --\n\n

    :type EnableSsl: boolean
    :param EnableSsl: Whether to enable SSL for the app.

    :type SslConfiguration: dict
    :param SslConfiguration: An SslConfiguration object with the SSL configuration.\n\nCertificate (string) -- [REQUIRED]The contents of the certificate\'s domain.crt file.\n\nPrivateKey (string) -- [REQUIRED]The private key; the contents of the certificate\'s domain.kex file.\n\nChain (string) --Optional. Can be used to specify an intermediate certificate authority key or client authentication.\n\n\n

    :type Attributes: dict
    :param Attributes: One or more user-defined key/value pairs to be added to the stack attributes.\n\n(string) --\n(string) --\n\n\n\n

    :type Environment: list
    :param Environment: An array of EnvironmentVariable objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instance. For more information, see Environment Variables .\nThere is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables\' names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, 'Environment: is too large (maximum is 20KB).'\n\nNote\nIf you have specified one or more environment variables, you cannot modify the stack\'s Chef version.\n\n\n(dict) --Represents an app\'s environment variable.\n\nKey (string) -- [REQUIRED](Required) The environment variable\'s name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.\n\nValue (string) -- [REQUIRED](Optional) The environment variable\'s value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.\n\nSecure (boolean) --(Optional) Whether the variable\'s value will be returned by the DescribeApps action. To conceal an environment variable\'s value, set Secure to true . DescribeApps then returns *****FILTERED***** instead of the actual value. The default value for Secure is false .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AppId': 'string'
}


Response Structure

(dict) --
Contains the response to a CreateApp request.

AppId (string) --
The app ID.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'AppId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_deployment(StackId=None, AppId=None, InstanceIds=None, LayerIds=None, Command=None, Comment=None, CustomJson=None):
    """
    Runs deployment or stack commands. For more information, see Deploying Apps and Run Stack Commands .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment(
        StackId='string',
        AppId='string',
        InstanceIds=[
            'string',
        ],
        LayerIds=[
            'string',
        ],
        Command={
            'Name': 'install_dependencies'|'update_dependencies'|'update_custom_cookbooks'|'execute_recipes'|'configure'|'setup'|'deploy'|'rollback'|'start'|'stop'|'restart'|'undeploy',
            'Args': {
                'string': [
                    'string',
                ]
            }
        },
        Comment='string',
        CustomJson='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :type AppId: string
    :param AppId: The app ID. This parameter is required for app deployments, but not for other deployment commands.

    :type InstanceIds: list
    :param InstanceIds: The instance IDs for the deployment targets.\n\n(string) --\n\n

    :type LayerIds: list
    :param LayerIds: The layer IDs for the deployment targets.\n\n(string) --\n\n

    :type Command: dict
    :param Command: [REQUIRED]\nA DeploymentCommand object that specifies the deployment command and any associated arguments.\n\nName (string) -- [REQUIRED]Specifies the operation. You can specify only one command.\nFor stacks, the following commands are available:\n\nexecute_recipes : Execute one or more recipes. To specify the recipes, set an Args parameter named recipes to the list of recipes to be executed. For example, to execute phpapp::appsetup , set Args to {'recipes':['phpapp::appsetup']} .\ninstall_dependencies : Install the stack\'s dependencies.\nupdate_custom_cookbooks : Update the stack\'s custom cookbooks.\nupdate_dependencies : Update the stack\'s dependencies.\n\n\nNote\nThe update_dependencies and install_dependencies commands are supported only for Linux instances. You can run the commands successfully on Windows instances, but they do nothing.\n\nFor apps, the following commands are available:\n\ndeploy : Deploy an app. Ruby on Rails apps have an optional Args parameter named migrate . Set Args to {'migrate':['true']} to migrate the database. The default setting is {'migrate':['false']}.\nrollback Roll the app back to the previous version. When you update an app, AWS OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions.\nstart : Start the app\'s web or application server.\nstop : Stop the app\'s web or application server.\nrestart : Restart the app\'s web or application server.\nundeploy : Undeploy the app.\n\n\nArgs (dict) --The arguments of those commands that take arguments. It should be set to a JSON object with the following format:\n\n{'arg_name1' : ['value1', 'value2', ...], 'arg_name2' : ['value1', 'value2', ...], ...}\nThe update_dependencies command takes two arguments:\n\nupgrade_os_to - Specifies the desired Amazon Linux version for instances whose OS you want to upgrade, such as Amazon Linux 2016.09 . You must also set the allow_reboot argument to true.\nallow_reboot - Specifies whether to allow AWS OpsWorks Stacks to reboot the instances if necessary, after installing the updates. This argument can be set to either true or false . The default value is false .\n\nFor example, to upgrade an instance to Amazon Linux 2016.09, set Args to the following.\n\n{ 'upgrade_os_to':['Amazon Linux 2016.09'], 'allow_reboot':['true'] }\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\n\n

    :type Comment: string
    :param Comment: A user-defined comment.

    :type CustomJson: string
    :param CustomJson: A string that contains user-defined, custom JSON. You can use this parameter to override some corresponding default stack configuration JSON values. The string should be in the following format:\n\n'{\\'key1\\': \\'value1\\', \\'key2\\': \\'value2\\',...}'\nFor more information about custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes and Overriding Attributes With Custom JSON .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DeploymentId': 'string'
}


Response Structure

(dict) --
Contains the response to a CreateDeployment request.

DeploymentId (string) --
The deployment ID, which can be used with other requests to identify the deployment.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'DeploymentId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_instance(StackId=None, LayerIds=None, InstanceType=None, AutoScalingType=None, Hostname=None, Os=None, AmiId=None, SshKeyName=None, AvailabilityZone=None, VirtualizationType=None, SubnetId=None, Architecture=None, RootDeviceType=None, BlockDeviceMappings=None, InstallUpdatesOnBoot=None, EbsOptimized=None, AgentVersion=None, Tenancy=None):
    """
    Creates an instance in a specified stack. For more information, see Adding an Instance to a Layer .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_instance(
        StackId='string',
        LayerIds=[
            'string',
        ],
        InstanceType='string',
        AutoScalingType='load'|'timer',
        Hostname='string',
        Os='string',
        AmiId='string',
        SshKeyName='string',
        AvailabilityZone='string',
        VirtualizationType='string',
        SubnetId='string',
        Architecture='x86_64'|'i386',
        RootDeviceType='ebs'|'instance-store',
        BlockDeviceMappings=[
            {
                'DeviceName': 'string',
                'NoDevice': 'string',
                'VirtualName': 'string',
                'Ebs': {
                    'SnapshotId': 'string',
                    'Iops': 123,
                    'VolumeSize': 123,
                    'VolumeType': 'gp2'|'io1'|'standard',
                    'DeleteOnTermination': True|False
                }
            },
        ],
        InstallUpdatesOnBoot=True|False,
        EbsOptimized=True|False,
        AgentVersion='string',
        Tenancy='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :type LayerIds: list
    :param LayerIds: [REQUIRED]\nAn array that contains the instance\'s layer IDs.\n\n(string) --\n\n

    :type InstanceType: string
    :param InstanceType: [REQUIRED]\nThe instance type, such as t2.micro . For a list of supported instance types, open the stack in the console, choose Instances , and choose + Instance . The Size list contains the currently supported types. For more information, see Instance Families and Types . The parameter values that you use to specify the various types are in the API Name column of the Available Instance Types table.\n

    :type AutoScalingType: string
    :param AutoScalingType: For load-based or time-based instances, the type. Windows stacks can use only time-based instances.

    :type Hostname: string
    :param Hostname: The instance host name.

    :type Os: string
    :param Os: The instance\'s operating system, which must be set to one of the following.\n\nA supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2018.03 , Amazon Linux 2017.09 , Amazon Linux 2017.03 , Amazon Linux 2016.09 , Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .\nA supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .\nCentOS Linux 7\nRed Hat Enterprise Linux 7\nA supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .\nA custom AMI: Custom .\n\nFor more information about the supported operating systems, see AWS OpsWorks Stacks Operating Systems .\nThe default option is the current Amazon Linux version. If you set this parameter to Custom , you must use the CreateInstance action\'s AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is Custom . For more information about supported operating systems, see Operating Systems For more information about how to use custom AMIs with AWS OpsWorks Stacks, see Using Custom AMIs .\n

    :type AmiId: string
    :param AmiId: A custom AMI ID to be used to create the instance. The AMI should be based on one of the supported operating systems. For more information, see Using Custom AMIs .\n\nNote\nIf you specify a custom AMI, you must set Os to Custom .\n\n

    :type SshKeyName: string
    :param SshKeyName: The instance\'s Amazon EC2 key-pair name.

    :type AvailabilityZone: string
    :param AvailabilityZone: The instance Availability Zone. For more information, see Regions and Endpoints .

    :type VirtualizationType: string
    :param VirtualizationType: The instance\'s virtualization type, paravirtual or hvm .

    :type SubnetId: string
    :param SubnetId: The ID of the instance\'s subnet. If the stack is running in a VPC, you can use this parameter to override the stack\'s default subnet ID value and direct AWS OpsWorks Stacks to launch the instance in a different subnet.

    :type Architecture: string
    :param Architecture: The instance architecture. The default option is x86_64 . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see Instance Families and Types .

    :type RootDeviceType: string
    :param RootDeviceType: The instance root device type. For more information, see Storage for the Root Device .

    :type BlockDeviceMappings: list
    :param BlockDeviceMappings: An array of BlockDeviceMapping objects that specify the instance\'s block devices. For more information, see Block Device Mapping . Note that block device mappings are not supported for custom AMIs.\n\n(dict) --Describes a block device mapping. This data type maps directly to the Amazon EC2 BlockDeviceMapping data type.\n\nDeviceName (string) --The device name that is exposed to the instance, such as /dev/sdh . For the root device, you can use the explicit device name or you can set this parameter to ROOT_DEVICE and AWS OpsWorks Stacks will provide the correct device name.\n\nNoDevice (string) --Suppresses the specified device included in the AMI\'s block device mapping.\n\nVirtualName (string) --The virtual device name. For more information, see BlockDeviceMapping .\n\nEbs (dict) --An EBSBlockDevice that defines how to configure an Amazon EBS volume when the instance is launched.\n\nSnapshotId (string) --The snapshot ID.\n\nIops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For more information, see EbsBlockDevice .\n\nVolumeSize (integer) --The volume size, in GiB. For more information, see EbsBlockDevice .\n\nVolumeType (string) --The volume type. gp2 for General Purpose (SSD) volumes, io1 for Provisioned IOPS (SSD) volumes, st1 for Throughput Optimized hard disk drives (HDD), sc1 for Cold HDD,and standard for Magnetic volumes.\nIf you specify the io1 volume type, you must also specify a value for the Iops attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1. AWS uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50 x (volume size).\n\nDeleteOnTermination (boolean) --Whether the volume is deleted on instance termination.\n\n\n\n\n\n\n

    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.\n\nNote\nWe strongly recommend using the default value of true to ensure that your instances have the latest security updates.\n\n

    :type EbsOptimized: boolean
    :param EbsOptimized: Whether to create an Amazon EBS-optimized instance.

    :type AgentVersion: string
    :param AgentVersion: The default AWS OpsWorks Stacks agent version. You have the following options:\n\nINHERIT - Use the stack\'s default agent version setting.\nversion_number - Use the specified agent version. This value overrides the stack\'s default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the instance.\n\nThe default setting is INHERIT . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.\n

    :type Tenancy: string
    :param Tenancy: The instance\'s tenancy option. The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: dedicated , default , or host . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see Dedicated Hosts Overview and Amazon EC2 Dedicated Hosts . For more information about dedicated instances, see Dedicated Instances and Amazon EC2 Dedicated Instances .

    :rtype: dict

ReturnsResponse Syntax
{
    'InstanceId': 'string'
}


Response Structure

(dict) --
Contains the response to a CreateInstance request.

InstanceId (string) --
The instance ID.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'InstanceId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_layer(StackId=None, Type=None, Name=None, Shortname=None, Attributes=None, CloudWatchLogsConfiguration=None, CustomInstanceProfileArn=None, CustomJson=None, CustomSecurityGroupIds=None, Packages=None, VolumeConfigurations=None, EnableAutoHealing=None, AutoAssignElasticIps=None, AutoAssignPublicIps=None, CustomRecipes=None, InstallUpdatesOnBoot=None, UseEbsOptimizedInstances=None, LifecycleEventConfiguration=None):
    """
    Creates a layer. For more information, see How to Create a Layer .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_layer(
        StackId='string',
        Type='aws-flow-ruby'|'ecs-cluster'|'java-app'|'lb'|'web'|'php-app'|'rails-app'|'nodejs-app'|'memcached'|'db-master'|'monitoring-master'|'custom',
        Name='string',
        Shortname='string',
        Attributes={
            'string': 'string'
        },
        CloudWatchLogsConfiguration={
            'Enabled': True|False,
            'LogStreams': [
                {
                    'LogGroupName': 'string',
                    'DatetimeFormat': 'string',
                    'TimeZone': 'LOCAL'|'UTC',
                    'File': 'string',
                    'FileFingerprintLines': 'string',
                    'MultiLineStartPattern': 'string',
                    'InitialPosition': 'start_of_file'|'end_of_file',
                    'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                    'BufferDuration': 123,
                    'BatchCount': 123,
                    'BatchSize': 123
                },
            ]
        },
        CustomInstanceProfileArn='string',
        CustomJson='string',
        CustomSecurityGroupIds=[
            'string',
        ],
        Packages=[
            'string',
        ],
        VolumeConfigurations=[
            {
                'MountPoint': 'string',
                'RaidLevel': 123,
                'NumberOfDisks': 123,
                'Size': 123,
                'VolumeType': 'string',
                'Iops': 123,
                'Encrypted': True|False
            },
        ],
        EnableAutoHealing=True|False,
        AutoAssignElasticIps=True|False,
        AutoAssignPublicIps=True|False,
        CustomRecipes={
            'Setup': [
                'string',
            ],
            'Configure': [
                'string',
            ],
            'Deploy': [
                'string',
            ],
            'Undeploy': [
                'string',
            ],
            'Shutdown': [
                'string',
            ]
        },
        InstallUpdatesOnBoot=True|False,
        UseEbsOptimizedInstances=True|False,
        LifecycleEventConfiguration={
            'Shutdown': {
                'ExecutionTimeout': 123,
                'DelayUntilElbConnectionsDrained': True|False
            }
        }
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe layer stack ID.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe layer name, which is used by the console.\n

    :type Shortname: string
    :param Shortname: [REQUIRED]\nFor custom layers only, use this parameter to specify the layer\'s short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters, which are limited to the alphanumeric characters, \'-\', \'_\', and \'.\'.\nThe built-in layers\' short names are defined by AWS OpsWorks Stacks. For more information, see the Layer Reference .\n

    :type Attributes: dict
    :param Attributes: One or more user-defined key-value pairs to be added to the stack attributes.\nTo create a cluster layer, set the EcsClusterArn attribute to the cluster\'s ARN.\n\n(string) --\n(string) --\n\n\n\n

    :type CloudWatchLogsConfiguration: dict
    :param CloudWatchLogsConfiguration: Specifies CloudWatch Logs configuration options for the layer. For more information, see CloudWatchLogsLogStream .\n\nEnabled (boolean) --Whether CloudWatch Logs is enabled for a layer.\n\nLogStreams (list) --A list of configuration options for CloudWatch Logs.\n\n(dict) --Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the CloudWatch Logs Agent Reference .\n\nLogGroupName (string) --Specifies the destination log group. A log group is created automatically if it doesn\'t already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), \'/\' (forward slash), and \'.\' (period).\n\nDatetimeFormat (string) --Specifies how the time stamp is extracted from logs. For more information, see the CloudWatch Logs Agent Reference .\n\nTimeZone (string) --Specifies the time zone of log event time stamps.\n\nFile (string) --Specifies log files that you want to push to CloudWatch Logs.\n\nFile can point to a specific file or multiple files (by using wild card characters such as /var/log/system.log* ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as access_log.2014-06-01-01 , access_log.2014-06-01-02 , and so on by using a pattern like access_log.* . Don\'t use a wildcard to match multiple file types, such as access_log_80 and access_log_443 . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.\nZipped files are not supported.\n\nFileFingerprintLines (string) --Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as \'1\', \'2-5\'. The default value is \'1\', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.\n\nMultiLineStartPattern (string) --Specifies the pattern for identifying the start of a log message.\n\nInitialPosition (string) --Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.\n\nEncoding (string) --Specifies the encoding of the log file so that the file can be read correctly. The default is utf_8 . Encodings supported by Python codecs.decode() can be used here.\n\nBufferDuration (integer) --Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.\n\nBatchCount (integer) --Specifies the max number of log events in a batch, up to 10000. The default value is 1000.\n\nBatchSize (integer) --Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.\n\n\n\n\n\n\n

    :type CustomInstanceProfileArn: string
    :param CustomInstanceProfileArn: The ARN of an IAM profile to be used for the layer\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .

    :type CustomJson: string
    :param CustomJson: A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer\'s instances. For more information, see Using Custom JSON . This feature is supported as of version 1.7.42 of the AWS CLI.

    :type CustomSecurityGroupIds: list
    :param CustomSecurityGroupIds: An array containing the layer custom security group IDs.\n\n(string) --\n\n

    :type Packages: list
    :param Packages: An array of Package objects that describes the layer packages.\n\n(string) --\n\n

    :type VolumeConfigurations: list
    :param VolumeConfigurations: A VolumeConfigurations object that describes the layer\'s Amazon EBS volumes.\n\n(dict) --Describes an Amazon EBS volume configuration.\n\nMountPoint (string) -- [REQUIRED]The volume mount point. For example '/dev/sdh'.\n\nRaidLevel (integer) --The volume RAID level .\n\nNumberOfDisks (integer) -- [REQUIRED]The number of disks in the volume.\n\nSize (integer) -- [REQUIRED]The volume size.\n\nVolumeType (string) --The volume type. For more information, see Amazon EBS Volume Types .\n\nstandard - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.\nio1 - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.\ngp2 - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.\nst1 - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.\nsc1 - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.\n\n\nIops (integer) --For PIOPS volumes, the IOPS per disk.\n\nEncrypted (boolean) --Specifies whether an Amazon EBS volume is encrypted. For more information, see Amazon EBS Encryption .\n\n\n\n\n

    :type EnableAutoHealing: boolean
    :param EnableAutoHealing: Whether to disable auto healing for the layer.

    :type AutoAssignElasticIps: boolean
    :param AutoAssignElasticIps: Whether to automatically assign an Elastic IP address to the layer\'s instances. For more information, see How to Edit a Layer .

    :type AutoAssignPublicIps: boolean
    :param AutoAssignPublicIps: For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer\'s instances. For more information, see How to Edit a Layer .

    :type CustomRecipes: dict
    :param CustomRecipes: A LayerCustomRecipes object that specifies the layer custom recipes.\n\nSetup (list) --An array of custom recipe names to be run following a setup event.\n\n(string) --\n\n\nConfigure (list) --An array of custom recipe names to be run following a configure event.\n\n(string) --\n\n\nDeploy (list) --An array of custom recipe names to be run following a deploy event.\n\n(string) --\n\n\nUndeploy (list) --An array of custom recipe names to be run following a undeploy event.\n\n(string) --\n\n\nShutdown (list) --An array of custom recipe names to be run following a shutdown event.\n\n(string) --\n\n\n\n

    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.\n\nNote\nTo ensure that your instances have the latest security updates, we strongly recommend using the default value of true .\n\n

    :type UseEbsOptimizedInstances: boolean
    :param UseEbsOptimizedInstances: Whether to use Amazon EBS-optimized instances.

    :type LifecycleEventConfiguration: dict
    :param LifecycleEventConfiguration: A LifeCycleEventConfiguration object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.\n\nShutdown (dict) --A ShutdownEventConfiguration object that specifies the Shutdown event configuration.\n\nExecutionTimeout (integer) --The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.\n\nDelayUntilElbConnectionsDrained (boolean) --Whether to enable Elastic Load Balancing connection draining. For more information, see Connection Draining\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LayerId': 'string'
}


Response Structure

(dict) --
Contains the response to a CreateLayer request.

LayerId (string) --
The layer ID.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'LayerId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_stack(Name=None, Region=None, VpcId=None, Attributes=None, ServiceRoleArn=None, DefaultInstanceProfileArn=None, DefaultOs=None, HostnameTheme=None, DefaultAvailabilityZone=None, DefaultSubnetId=None, CustomJson=None, ConfigurationManager=None, ChefConfiguration=None, UseCustomCookbooks=None, UseOpsworksSecurityGroups=None, CustomCookbooksSource=None, DefaultSshKeyName=None, DefaultRootDeviceType=None, AgentVersion=None):
    """
    Creates a new stack. For more information, see Create a New Stack .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stack(
        Name='string',
        Region='string',
        VpcId='string',
        Attributes={
            'string': 'string'
        },
        ServiceRoleArn='string',
        DefaultInstanceProfileArn='string',
        DefaultOs='string',
        HostnameTheme='string',
        DefaultAvailabilityZone='string',
        DefaultSubnetId='string',
        CustomJson='string',
        ConfigurationManager={
            'Name': 'string',
            'Version': 'string'
        },
        ChefConfiguration={
            'ManageBerkshelf': True|False,
            'BerkshelfVersion': 'string'
        },
        UseCustomCookbooks=True|False,
        UseOpsworksSecurityGroups=True|False,
        CustomCookbooksSource={
            'Type': 'git'|'svn'|'archive'|'s3',
            'Url': 'string',
            'Username': 'string',
            'Password': 'string',
            'SshKey': 'string',
            'Revision': 'string'
        },
        DefaultSshKeyName='string',
        DefaultRootDeviceType='ebs'|'instance-store',
        AgentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe stack name.\n

    :type Region: string
    :param Region: [REQUIRED]\nThe stack\'s AWS region, such as ap-south-1 . For more information about Amazon regions, see Regions and Endpoints .\n\nNote\nIn the AWS CLI, this API maps to the --stack-region parameter. If the --stack-region parameter and the AWS CLI common parameter --region are set to the same value, the stack uses a regional endpoint. If the --stack-region parameter is not set, but the AWS CLI --region parameter is, this also results in a stack with a regional endpoint. However, if the --region parameter is set to us-east-1 , and the --stack-region parameter is set to one of the following, then the stack uses a legacy or classic region: us-west-1, us-west-2, sa-east-1, eu-central-1, eu-west-1, ap-northeast-1, ap-southeast-1, ap-southeast-2 . In this case, the actual API endpoint of the stack is in us-east-1 . Only the preceding regions are supported as classic regions in the us-east-1 API endpoint. Because it is a best practice to choose the regional endpoint that is closest to where you manage AWS, we recommend that you use regional endpoints for new stacks. The AWS CLI common --region parameter always specifies a regional API endpoint; it cannot be used to specify a classic AWS OpsWorks Stacks region.\n\n

    :type VpcId: string
    :param VpcId: The ID of the VPC that the stack is to be launched into. The VPC must be in the stack\'s region. All instances are launched into this VPC. You cannot change the ID later.\n\nIf your account supports EC2-Classic, the default value is no VPC .\nIf your account does not support EC2-Classic, the default value is the default VPC for the specified region.\n\nIf the VPC ID corresponds to a default VPC and you have specified either the DefaultAvailabilityZone or the DefaultSubnetId parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.\nIf you specify a nondefault VPC ID, note the following:\n\nIt must belong to a VPC in your account that is in the specified region.\nYou must specify a value for DefaultSubnetId .\n\nFor more information about how to use AWS OpsWorks Stacks with a VPC, see Running a Stack in a VPC . For more information about default VPC and EC2-Classic, see Supported Platforms .\n

    :type Attributes: dict
    :param Attributes: One or more user-defined key-value pairs to be added to the stack attributes.\n\n(string) --\n(string) --\n\n\n\n

    :type ServiceRoleArn: string
    :param ServiceRoleArn: [REQUIRED]\nThe stack\'s AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see Using Identifiers .\n

    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .\n

    :type DefaultOs: string
    :param DefaultOs: The stack\'s default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following.\n\nA supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2018.03 , Amazon Linux 2017.09 , Amazon Linux 2017.03 , Amazon Linux 2016.09 , Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .\nA supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .\nCentOS Linux 7\nRed Hat Enterprise Linux 7\nA supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .\nA custom AMI: Custom . You specify the custom AMI you want to use when you create instances. For more information, see Using Custom AMIs .\n\nThe default option is the current Amazon Linux version. For more information about supported operating systems, see AWS OpsWorks Stacks Operating Systems .\n

    :type HostnameTheme: string
    :param HostnameTheme: The stack\'s host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack\'s instances. By default, HostnameTheme is set to Layer_Dependent , which creates host names by appending integers to the layer\'s short name. The other themes are:\n\nBaked_Goods\nClouds\nEurope_Cities\nFruits\nGreek_Deities_and_Titans\nLegendary_creatures_from_Japan\nPlanets_and_Moons\nRoman_Deities\nScottish_Islands\nUS_Cities\nWild_Cats\n\nTo obtain a generated host name, call GetHostNameSuggestion , which returns a host name based on the current theme.\n

    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: The stack\'s default Availability Zone, which must be in the specified region. For more information, see Regions and Endpoints . If you also specify a value for DefaultSubnetId , the subnet must be in the same zone. For more information, see the VpcId parameter description.

    :type DefaultSubnetId: string
    :param DefaultSubnetId: The stack\'s default VPC subnet ID. This parameter is required if you specify a value for the VpcId parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for DefaultAvailabilityZone , the subnet must be in that zone. For information on default values and when this parameter is required, see the VpcId parameter description.

    :type CustomJson: string
    :param CustomJson: A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:\n\n'{\\'key1\\': \\'value1\\', \\'key2\\': \\'value2\\',...}'\nFor more information about custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .\n

    :type ConfigurationManager: dict
    :param ConfigurationManager: The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.\n\nName (string) --The name. This parameter must be set to 'Chef'.\n\nVersion (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.\n\n\n

    :type ChefConfiguration: dict
    :param ChefConfiguration: A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see Create a New Stack .\n\nManageBerkshelf (boolean) --Whether to enable Berkshelf.\n\nBerkshelfVersion (string) --The Berkshelf version.\n\n\n

    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: Whether the stack uses custom cookbooks.

    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack\'s layers.\nAWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With UseOpsworksSecurityGroups you can instead provide your own custom security groups. UseOpsworksSecurityGroups has the following settings:\n\nTrue - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.\nFalse - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.\n\nFor more information, see Create a New Stack .\n

    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: Contains the information required to retrieve an app or cookbook from a repository. For more information, see Adding Apps or Cookbooks and Recipes .\n\nType (string) --The repository type.\n\nUrl (string) --The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .\n\nUsername (string) --This parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Username to the appropriate IAM access key ID.\nFor HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.\n\n\nPassword (string) --When included in a request, the parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Password to the appropriate IAM secret access key.\nFor HTTP bundles and Subversion repositories, set Password to the password.\n\nFor more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nSshKey (string) --In requests, the repository\'s SSH key.\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nRevision (string) --The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.\n\n\n

    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see Using SSH to Communicate with an Instance and Managing SSH Access . You can override this setting by specifying a different key pair, or no key pair, when you create an instance .

    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is instance-store . For more information, see Storage for the Root Device .

    :type AgentVersion: string
    :param AgentVersion: The default AWS OpsWorks Stacks agent version. You have the following options:\n\nAuto-update - Set this parameter to LATEST . AWS OpsWorks Stacks automatically installs new agent versions on the stack\'s instances as soon as they are available.\nFixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack\'s instances.\n\nThe default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.\n\nNote\nYou can also specify an agent version when you create or update an instance, which overrides the stack\'s default setting.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackId': 'string'
}


Response Structure

(dict) --
Contains the response to a CreateStack request.

StackId (string) --
The stack ID, which is an opaque string that you use to identify the stack when performing actions such as DescribeStacks .







Exceptions

OpsWorks.Client.exceptions.ValidationException


    :return: {
        'StackId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    
    """
    pass

def create_user_profile(IamUserArn=None, SshUsername=None, SshPublicKey=None, AllowSelfManagement=None):
    """
    Creates a new user profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user_profile(
        IamUserArn='string',
        SshUsername='string',
        SshPublicKey='string',
        AllowSelfManagement=True|False
    )
    
    
    :type IamUserArn: string
    :param IamUserArn: [REQUIRED]\nThe user\'s IAM ARN; this can also be a federated user\'s ARN.\n

    :type SshUsername: string
    :param SshUsername: The user\'s SSH user name. The allowable characters are [a-z], [A-Z], [0-9], \'-\', and \'_\'. If the specified name includes other punctuation marks, AWS OpsWorks Stacks removes them. For example, my.name will be changed to myname . If you do not specify an SSH user name, AWS OpsWorks Stacks generates one from the IAM user name.

    :type SshPublicKey: string
    :param SshPublicKey: The user\'s public SSH key.

    :type AllowSelfManagement: boolean
    :param AllowSelfManagement: Whether users can specify their own SSH public key through the My Settings page. For more information, see Setting an IAM User\'s Public SSH Key .

    :rtype: dict

ReturnsResponse Syntax
{
    'IamUserArn': 'string'
}


Response Structure

(dict) --
Contains the response to a CreateUserProfile request.

IamUserArn (string) --
The user\'s IAM ARN.







Exceptions

OpsWorks.Client.exceptions.ValidationException


    :return: {
        'IamUserArn': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    
    """
    pass

def delete_app(AppId=None):
    """
    Deletes a specified app.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_app(
        AppId='string'
    )
    
    
    :type AppId: string
    :param AppId: [REQUIRED]\nThe app ID.\n

    """
    pass

def delete_instance(InstanceId=None, DeleteElasticIp=None, DeleteVolumes=None):
    """
    Deletes a specified instance, which terminates the associated Amazon EC2 instance. You must stop an instance before you can delete it.
    For more information, see Deleting Instances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_instance(
        InstanceId='string',
        DeleteElasticIp=True|False,
        DeleteVolumes=True|False
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    :type DeleteElasticIp: boolean
    :param DeleteElasticIp: Whether to delete the instance Elastic IP address.

    :type DeleteVolumes: boolean
    :param DeleteVolumes: Whether to delete the instance\'s Amazon EBS volumes.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_layer(LayerId=None):
    """
    Deletes a specified layer. You must first stop and then delete all associated instances or unassign registered instances. For more information, see How to Delete a Layer .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_layer(
        LayerId='string'
    )
    
    
    :type LayerId: string
    :param LayerId: [REQUIRED]\nThe layer ID.\n

    """
    pass

def delete_stack(StackId=None):
    """
    Deletes a specified stack. You must first delete all instances, layers, and apps or deregister registered instances. For more information, see Shut Down a Stack .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stack(
        StackId='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    """
    pass

def delete_user_profile(IamUserArn=None):
    """
    Deletes a user profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_profile(
        IamUserArn='string'
    )
    
    
    :type IamUserArn: string
    :param IamUserArn: [REQUIRED]\nThe user\'s IAM ARN. This can also be a federated user\'s ARN.\n

    """
    pass

def deregister_ecs_cluster(EcsClusterArn=None):
    """
    Deregisters a specified Amazon ECS cluster from a stack. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_ecs_cluster(
        EcsClusterArn='string'
    )
    
    
    :type EcsClusterArn: string
    :param EcsClusterArn: [REQUIRED]\nThe cluster\'s Amazon Resource Number (ARN).\n

    """
    pass

def deregister_elastic_ip(ElasticIp=None):
    """
    Deregisters a specified Elastic IP address. The address can then be registered by another stack. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_elastic_ip(
        ElasticIp='string'
    )
    
    
    :type ElasticIp: string
    :param ElasticIp: [REQUIRED]\nThe Elastic IP address.\n

    """
    pass

def deregister_instance(InstanceId=None):
    """
    Deregister a registered Amazon EC2 or on-premises instance. This action removes the instance from the stack and returns it to your control. This action cannot be used with instances that were created with AWS OpsWorks Stacks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_instance(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    """
    pass

def deregister_rds_db_instance(RdsDbInstanceArn=None):
    """
    Deregisters an Amazon RDS instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_rds_db_instance(
        RdsDbInstanceArn='string'
    )
    
    
    :type RdsDbInstanceArn: string
    :param RdsDbInstanceArn: [REQUIRED]\nThe Amazon RDS instance\'s ARN.\n

    """
    pass

def deregister_volume(VolumeId=None):
    """
    Deregisters an Amazon EBS volume. The volume can then be registered by another stack. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_volume(
        VolumeId='string'
    )
    
    
    :type VolumeId: string
    :param VolumeId: [REQUIRED]\nThe AWS OpsWorks Stacks volume ID, which is the GUID that AWS OpsWorks Stacks assigned to the instance when you registered the volume with the stack, not the Amazon EC2 volume ID.\n

    """
    pass

def describe_agent_versions(StackId=None, ConfigurationManager=None):
    """
    Describes the available AWS OpsWorks Stacks agent versions. You must specify a stack ID or a configuration manager. DescribeAgentVersions returns a list of available agent versions for the specified stack or configuration manager.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_agent_versions(
        StackId='string',
        ConfigurationManager={
            'Name': 'string',
            'Version': 'string'
        }
    )
    
    
    :type StackId: string
    :param StackId: The stack ID.

    :type ConfigurationManager: dict
    :param ConfigurationManager: The configuration manager.\n\nName (string) --The name. This parameter must be set to 'Chef'.\n\nVersion (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AgentVersions': [
        {
            'Version': 'string',
            'ConfigurationManager': {
                'Name': 'string',
                'Version': 'string'
            }
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeAgentVersions request.

AgentVersions (list) --
The agent versions for the specified stack or configuration manager. Note that this value is the complete version number, not the abbreviated number used by the console.

(dict) --
Describes an agent version.

Version (string) --
The agent version.

ConfigurationManager (dict) --
The configuration manager.

Name (string) --
The name. This parameter must be set to "Chef".

Version (string) --
The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.













Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'AgentVersions': [
            {
                'Version': 'string',
                'ConfigurationManager': {
                    'Name': 'string',
                    'Version': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_apps(StackId=None, AppIds=None):
    """
    Requests a description of a specified set of apps.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_apps(
        StackId='string',
        AppIds=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: The app stack ID. If you use this parameter, DescribeApps returns a description of the apps in the specified stack.

    :type AppIds: list
    :param AppIds: An array of app IDs for the apps to be described. If you use this parameter, DescribeApps returns a description of the specified apps. Otherwise, it returns a description of every app.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Apps': [
        {
            'AppId': 'string',
            'StackId': 'string',
            'Shortname': 'string',
            'Name': 'string',
            'Description': 'string',
            'DataSources': [
                {
                    'Type': 'string',
                    'Arn': 'string',
                    'DatabaseName': 'string'
                },
            ],
            'Type': 'aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
            'AppSource': {
                'Type': 'git'|'svn'|'archive'|'s3',
                'Url': 'string',
                'Username': 'string',
                'Password': 'string',
                'SshKey': 'string',
                'Revision': 'string'
            },
            'Domains': [
                'string',
            ],
            'EnableSsl': True|False,
            'SslConfiguration': {
                'Certificate': 'string',
                'PrivateKey': 'string',
                'Chain': 'string'
            },
            'Attributes': {
                'string': 'string'
            },
            'CreatedAt': 'string',
            'Environment': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Secure': True|False
                },
            ]
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeApps request.

Apps (list) --
An array of App objects that describe the specified apps.

(dict) --
A description of the app.

AppId (string) --
The app ID.

StackId (string) --
The app stack ID.

Shortname (string) --
The app\'s short name.

Name (string) --
The app name.

Description (string) --
A description of the app.

DataSources (list) --
The app\'s data sources.

(dict) --
Describes an app\'s data source.

Type (string) --
The data source\'s type, AutoSelectOpsworksMysqlInstance , OpsworksMysqlInstance , RdsDbInstance , or None .

Arn (string) --
The data source\'s ARN.

DatabaseName (string) --
The database name.





Type (string) --
The app type.

AppSource (dict) --
A Source object that describes the app repository.

Type (string) --
The repository type.

Url (string) --
The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .

Username (string) --
This parameter depends on the repository type.

For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.


Password (string) --
When included in a request, the parameter depends on the repository type.

For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
For HTTP bundles and Subversion repositories, set Password to the password.

For more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
In responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.

SshKey (string) --
In requests, the repository\'s SSH key.
In responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.

Revision (string) --
The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.



Domains (list) --
The app vhost settings with multiple domains separated by commas. For example: \'www.example.com, example.com\'

(string) --


EnableSsl (boolean) --
Whether to enable SSL for the app.

SslConfiguration (dict) --
An SslConfiguration object with the SSL configuration.

Certificate (string) --
The contents of the certificate\'s domain.crt file.

PrivateKey (string) --
The private key; the contents of the certificate\'s domain.kex file.

Chain (string) --
Optional. Can be used to specify an intermediate certificate authority key or client authentication.



Attributes (dict) --
The stack attributes.

(string) --
(string) --




CreatedAt (string) --
When the app was created.

Environment (list) --
An array of EnvironmentVariable objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instances. For more information, see Environment Variables .

Note
There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variable names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases, but if you do exceed it, you will cause an exception (API) with an "Environment: is too large (maximum is 20 KB)" message.


(dict) --
Represents an app\'s environment variable.

Key (string) --
(Required) The environment variable\'s name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.

Value (string) --
(Optional) The environment variable\'s value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.

Secure (boolean) --
(Optional) Whether the variable\'s value will be returned by the  DescribeApps action. To conceal an environment variable\'s value, set Secure to true . DescribeApps then returns *****FILTERED***** instead of the actual value. The default value for Secure is false .















Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Apps': [
            {
                'AppId': 'string',
                'StackId': 'string',
                'Shortname': 'string',
                'Name': 'string',
                'Description': 'string',
                'DataSources': [
                    {
                        'Type': 'string',
                        'Arn': 'string',
                        'DatabaseName': 'string'
                    },
                ],
                'Type': 'aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
                'AppSource': {
                    'Type': 'git'|'svn'|'archive'|'s3',
                    'Url': 'string',
                    'Username': 'string',
                    'Password': 'string',
                    'SshKey': 'string',
                    'Revision': 'string'
                },
                'Domains': [
                    'string',
                ],
                'EnableSsl': True|False,
                'SslConfiguration': {
                    'Certificate': 'string',
                    'PrivateKey': 'string',
                    'Chain': 'string'
                },
                'Attributes': {
                    'string': 'string'
                },
                'CreatedAt': 'string',
                'Environment': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Secure': True|False
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
    For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
    
    """
    pass

def describe_commands(DeploymentId=None, InstanceId=None, CommandIds=None):
    """
    Describes the results of specified commands.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_commands(
        DeploymentId='string',
        InstanceId='string',
        CommandIds=[
            'string',
        ]
    )
    
    
    :type DeploymentId: string
    :param DeploymentId: The deployment ID. If you include this parameter, DescribeCommands returns a description of the commands associated with the specified deployment.

    :type InstanceId: string
    :param InstanceId: The instance ID. If you include this parameter, DescribeCommands returns a description of the commands associated with the specified instance.

    :type CommandIds: list
    :param CommandIds: An array of command IDs. If you include this parameter, DescribeCommands returns a description of the specified commands. Otherwise, it returns a description of every command.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Commands': [
        {
            'CommandId': 'string',
            'InstanceId': 'string',
            'DeploymentId': 'string',
            'CreatedAt': 'string',
            'AcknowledgedAt': 'string',
            'CompletedAt': 'string',
            'Status': 'string',
            'ExitCode': 123,
            'LogUrl': 'string',
            'Type': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeCommands request.

Commands (list) --
An array of Command objects that describe each of the specified commands.

(dict) --
Describes a command.

CommandId (string) --
The command ID.

InstanceId (string) --
The ID of the instance where the command was executed.

DeploymentId (string) --
The command deployment ID.

CreatedAt (string) --
Date and time when the command was run.

AcknowledgedAt (string) --
Date and time when the command was acknowledged.

CompletedAt (string) --
Date when the command completed.

Status (string) --
The command status:

failed
successful
skipped
pending


ExitCode (integer) --
The command exit code.

LogUrl (string) --
The URL of the command log.

Type (string) --
The command type:

configure
deploy
execute_recipes
install_dependencies
restart
rollback
setup
start
stop
undeploy
update_custom_cookbooks
update_dependencies












Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Commands': [
            {
                'CommandId': 'string',
                'InstanceId': 'string',
                'DeploymentId': 'string',
                'CreatedAt': 'string',
                'AcknowledgedAt': 'string',
                'CompletedAt': 'string',
                'Status': 'string',
                'ExitCode': 123,
                'LogUrl': 'string',
                'Type': 'string'
            },
        ]
    }
    
    
    :returns: 
    failed
    successful
    skipped
    pending
    
    """
    pass

def describe_deployments(StackId=None, AppId=None, DeploymentIds=None):
    """
    Requests a description of a specified set of deployments.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_deployments(
        StackId='string',
        AppId='string',
        DeploymentIds=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: The stack ID. If you include this parameter, the command returns a description of the commands associated with the specified stack.

    :type AppId: string
    :param AppId: The app ID. If you include this parameter, the command returns a description of the commands associated with the specified app.

    :type DeploymentIds: list
    :param DeploymentIds: An array of deployment IDs to be described. If you include this parameter, the command returns a description of the specified deployments. Otherwise, it returns a description of every deployment.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Deployments': [
        {
            'DeploymentId': 'string',
            'StackId': 'string',
            'AppId': 'string',
            'CreatedAt': 'string',
            'CompletedAt': 'string',
            'Duration': 123,
            'IamUserArn': 'string',
            'Comment': 'string',
            'Command': {
                'Name': 'install_dependencies'|'update_dependencies'|'update_custom_cookbooks'|'execute_recipes'|'configure'|'setup'|'deploy'|'rollback'|'start'|'stop'|'restart'|'undeploy',
                'Args': {
                    'string': [
                        'string',
                    ]
                }
            },
            'Status': 'string',
            'CustomJson': 'string',
            'InstanceIds': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeDeployments request.

Deployments (list) --
An array of Deployment objects that describe the deployments.

(dict) --
Describes a deployment of a stack or app.

DeploymentId (string) --
The deployment ID.

StackId (string) --
The stack ID.

AppId (string) --
The app ID.

CreatedAt (string) --
Date when the deployment was created.

CompletedAt (string) --
Date when the deployment completed.

Duration (integer) --
The deployment duration.

IamUserArn (string) --
The user\'s IAM ARN.

Comment (string) --
A user-defined comment.

Command (dict) --
Used to specify a stack or deployment command.

Name (string) --
Specifies the operation. You can specify only one command.
For stacks, the following commands are available:

execute_recipes : Execute one or more recipes. To specify the recipes, set an Args parameter named recipes to the list of recipes to be executed. For example, to execute phpapp::appsetup , set Args to {"recipes":["phpapp::appsetup"]} .
install_dependencies : Install the stack\'s dependencies.
update_custom_cookbooks : Update the stack\'s custom cookbooks.
update_dependencies : Update the stack\'s dependencies.


Note
The update_dependencies and install_dependencies commands are supported only for Linux instances. You can run the commands successfully on Windows instances, but they do nothing.

For apps, the following commands are available:

deploy : Deploy an app. Ruby on Rails apps have an optional Args parameter named migrate . Set Args to {"migrate":["true"]} to migrate the database. The default setting is {"migrate":["false"]}.
rollback Roll the app back to the previous version. When you update an app, AWS OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions.
start : Start the app\'s web or application server.
stop : Stop the app\'s web or application server.
restart : Restart the app\'s web or application server.
undeploy : Undeploy the app.


Args (dict) --
The arguments of those commands that take arguments. It should be set to a JSON object with the following format:

{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...], ...}

The update_dependencies command takes two arguments:

upgrade_os_to - Specifies the desired Amazon Linux version for instances whose OS you want to upgrade, such as Amazon Linux 2016.09 . You must also set the allow_reboot argument to true.
allow_reboot - Specifies whether to allow AWS OpsWorks Stacks to reboot the instances if necessary, after installing the updates. This argument can be set to either true or false . The default value is false .

For example, to upgrade an instance to Amazon Linux 2016.09, set Args to the following.

{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }


(string) --
(list) --
(string) --








Status (string) --
The deployment status:

running
successful
failed


CustomJson (string) --
A string that contains user-defined custom JSON. It can be used to override the corresponding default stack configuration attribute values for stack or to pass data to recipes. The string should be in the following format:

"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"

For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .

InstanceIds (list) --
The IDs of the target instances.

(string) --












Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Deployments': [
            {
                'DeploymentId': 'string',
                'StackId': 'string',
                'AppId': 'string',
                'CreatedAt': 'string',
                'CompletedAt': 'string',
                'Duration': 123,
                'IamUserArn': 'string',
                'Comment': 'string',
                'Command': {
                    'Name': 'install_dependencies'|'update_dependencies'|'update_custom_cookbooks'|'execute_recipes'|'configure'|'setup'|'deploy'|'rollback'|'start'|'stop'|'restart'|'undeploy',
                    'Args': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'Status': 'string',
                'CustomJson': 'string',
                'InstanceIds': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    execute_recipes : Execute one or more recipes. To specify the recipes, set an Args parameter named recipes to the list of recipes to be executed. For example, to execute phpapp::appsetup , set Args to {"recipes":["phpapp::appsetup"]} .
    install_dependencies : Install the stack\'s dependencies.
    update_custom_cookbooks : Update the stack\'s custom cookbooks.
    update_dependencies : Update the stack\'s dependencies.
    
    """
    pass

def describe_ecs_clusters(EcsClusterArns=None, StackId=None, NextToken=None, MaxResults=None):
    """
    Describes Amazon ECS clusters that are registered with a stack. If you specify only a stack ID, you can use the MaxResults and NextToken parameters to paginate the response. However, AWS OpsWorks Stacks currently supports only one cluster per layer, so the result set has a maximum of one element.
    This call accepts only one resource-identifying parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ecs_clusters(
        EcsClusterArns=[
            'string',
        ],
        StackId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type EcsClusterArns: list
    :param EcsClusterArns: A list of ARNs, one for each cluster to be described.\n\n(string) --\n\n

    :type StackId: string
    :param StackId: A stack ID. DescribeEcsClusters returns a description of the cluster that is registered with the stack.

    :type NextToken: string
    :param NextToken: If the previous paginated request did not return all of the remaining results, the response object\'s``NextToken`` parameter value is set to a token. To retrieve the next set of results, call DescribeEcsClusters again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'EcsClusters': [
        {
            'EcsClusterArn': 'string',
            'EcsClusterName': 'string',
            'StackId': 'string',
            'RegisteredAt': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Contains the response to a DescribeEcsClusters request.

EcsClusters (list) --
A list of EcsCluster objects containing the cluster descriptions.

(dict) --
Describes a registered Amazon ECS cluster.

EcsClusterArn (string) --
The cluster\'s ARN.

EcsClusterName (string) --
The cluster name.

StackId (string) --
The stack ID.

RegisteredAt (string) --
The time and date that the cluster was registered with the stack.





NextToken (string) --
If a paginated request does not return all of the remaining results, this parameter is set to a token that you can assign to the request object\'s NextToken parameter to retrieve the next set of results. If the previous paginated request returned all of the remaining results, this parameter is set to null .







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'EcsClusters': [
            {
                'EcsClusterArn': 'string',
                'EcsClusterName': 'string',
                'StackId': 'string',
                'RegisteredAt': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_elastic_ips(InstanceId=None, StackId=None, Ips=None):
    """
    Describes Elastic IP addresses .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_elastic_ips(
        InstanceId='string',
        StackId='string',
        Ips=[
            'string',
        ]
    )
    
    
    :type InstanceId: string
    :param InstanceId: The instance ID. If you include this parameter, DescribeElasticIps returns a description of the Elastic IP addresses associated with the specified instance.

    :type StackId: string
    :param StackId: A stack ID. If you include this parameter, DescribeElasticIps returns a description of the Elastic IP addresses that are registered with the specified stack.

    :type Ips: list
    :param Ips: An array of Elastic IP addresses to be described. If you include this parameter, DescribeElasticIps returns a description of the specified Elastic IP addresses. Otherwise, it returns a description of every Elastic IP address.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ElasticIps': [
        {
            'Ip': 'string',
            'Name': 'string',
            'Domain': 'string',
            'Region': 'string',
            'InstanceId': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeElasticIps request.

ElasticIps (list) --
An ElasticIps object that describes the specified Elastic IP addresses.

(dict) --
Describes an Elastic IP address.

Ip (string) --
The IP address.

Name (string) --
The name.

Domain (string) --
The domain.

Region (string) --
The AWS region. For more information, see Regions and Endpoints .

InstanceId (string) --
The ID of the instance that the address is attached to.











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'ElasticIps': [
            {
                'Ip': 'string',
                'Name': 'string',
                'Domain': 'string',
                'Region': 'string',
                'InstanceId': 'string'
            },
        ]
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_elastic_load_balancers(StackId=None, LayerIds=None):
    """
    Describes a stack\'s Elastic Load Balancing instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_elastic_load_balancers(
        StackId='string',
        LayerIds=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: A stack ID. The action describes the stack\'s Elastic Load Balancing instances.

    :type LayerIds: list
    :param LayerIds: A list of layer IDs. The action describes the Elastic Load Balancing instances for the specified layers.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ElasticLoadBalancers': [
        {
            'ElasticLoadBalancerName': 'string',
            'Region': 'string',
            'DnsName': 'string',
            'StackId': 'string',
            'LayerId': 'string',
            'VpcId': 'string',
            'AvailabilityZones': [
                'string',
            ],
            'SubnetIds': [
                'string',
            ],
            'Ec2InstanceIds': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeElasticLoadBalancers request.

ElasticLoadBalancers (list) --
A list of ElasticLoadBalancer objects that describe the specified Elastic Load Balancing instances.

(dict) --
Describes an Elastic Load Balancing instance.

ElasticLoadBalancerName (string) --
The Elastic Load Balancing instance\'s name.

Region (string) --
The instance\'s AWS region.

DnsName (string) --
The instance\'s public DNS name.

StackId (string) --
The ID of the stack that the instance is associated with.

LayerId (string) --
The ID of the layer that the instance is attached to.

VpcId (string) --
The VPC ID.

AvailabilityZones (list) --
A list of Availability Zones.

(string) --


SubnetIds (list) --
A list of subnet IDs, if the stack is running in a VPC.

(string) --


Ec2InstanceIds (list) --
A list of the EC2 instances that the Elastic Load Balancing instance is managing traffic for.

(string) --












Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'ElasticLoadBalancers': [
            {
                'ElasticLoadBalancerName': 'string',
                'Region': 'string',
                'DnsName': 'string',
                'StackId': 'string',
                'LayerId': 'string',
                'VpcId': 'string',
                'AvailabilityZones': [
                    'string',
                ],
                'SubnetIds': [
                    'string',
                ],
                'Ec2InstanceIds': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_instances(StackId=None, LayerId=None, InstanceIds=None):
    """
    Requests a description of a set of instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_instances(
        StackId='string',
        LayerId='string',
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: A stack ID. If you use this parameter, DescribeInstances returns descriptions of the instances associated with the specified stack.

    :type LayerId: string
    :param LayerId: A layer ID. If you use this parameter, DescribeInstances returns descriptions of the instances associated with the specified layer.

    :type InstanceIds: list
    :param InstanceIds: An array of instance IDs to be described. If you use this parameter, DescribeInstances returns a description of the specified instances. Otherwise, it returns a description of every instance.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Instances': [
        {
            'AgentVersion': 'string',
            'AmiId': 'string',
            'Architecture': 'x86_64'|'i386',
            'Arn': 'string',
            'AutoScalingType': 'load'|'timer',
            'AvailabilityZone': 'string',
            'BlockDeviceMappings': [
                {
                    'DeviceName': 'string',
                    'NoDevice': 'string',
                    'VirtualName': 'string',
                    'Ebs': {
                        'SnapshotId': 'string',
                        'Iops': 123,
                        'VolumeSize': 123,
                        'VolumeType': 'gp2'|'io1'|'standard',
                        'DeleteOnTermination': True|False
                    }
                },
            ],
            'CreatedAt': 'string',
            'EbsOptimized': True|False,
            'Ec2InstanceId': 'string',
            'EcsClusterArn': 'string',
            'EcsContainerInstanceArn': 'string',
            'ElasticIp': 'string',
            'Hostname': 'string',
            'InfrastructureClass': 'string',
            'InstallUpdatesOnBoot': True|False,
            'InstanceId': 'string',
            'InstanceProfileArn': 'string',
            'InstanceType': 'string',
            'LastServiceErrorId': 'string',
            'LayerIds': [
                'string',
            ],
            'Os': 'string',
            'Platform': 'string',
            'PrivateDns': 'string',
            'PrivateIp': 'string',
            'PublicDns': 'string',
            'PublicIp': 'string',
            'RegisteredBy': 'string',
            'ReportedAgentVersion': 'string',
            'ReportedOs': {
                'Family': 'string',
                'Name': 'string',
                'Version': 'string'
            },
            'RootDeviceType': 'ebs'|'instance-store',
            'RootDeviceVolumeId': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SshHostDsaKeyFingerprint': 'string',
            'SshHostRsaKeyFingerprint': 'string',
            'SshKeyName': 'string',
            'StackId': 'string',
            'Status': 'string',
            'SubnetId': 'string',
            'Tenancy': 'string',
            'VirtualizationType': 'paravirtual'|'hvm'
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeInstances request.

Instances (list) --
An array of Instance objects that describe the instances.

(dict) --
Describes an instance.

AgentVersion (string) --
The agent version. This parameter is set to INHERIT if the instance inherits the default stack setting or to a a version number for a fixed agent version.

AmiId (string) --
A custom AMI ID to be used to create the instance. For more information, see Instances

Architecture (string) --
The instance architecture: "i386" or "x86_64".

Arn (string) --
The instance\'s Amazon Resource Number (ARN).

AutoScalingType (string) --
For load-based or time-based instances, the type.

AvailabilityZone (string) --
The instance Availability Zone. For more information, see Regions and Endpoints .

BlockDeviceMappings (list) --
An array of BlockDeviceMapping objects that specify the instance\'s block device mappings.

(dict) --
Describes a block device mapping. This data type maps directly to the Amazon EC2 BlockDeviceMapping data type.

DeviceName (string) --
The device name that is exposed to the instance, such as /dev/sdh . For the root device, you can use the explicit device name or you can set this parameter to ROOT_DEVICE and AWS OpsWorks Stacks will provide the correct device name.

NoDevice (string) --
Suppresses the specified device included in the AMI\'s block device mapping.

VirtualName (string) --
The virtual device name. For more information, see BlockDeviceMapping .

Ebs (dict) --
An EBSBlockDevice that defines how to configure an Amazon EBS volume when the instance is launched.

SnapshotId (string) --
The snapshot ID.

Iops (integer) --
The number of I/O operations per second (IOPS) that the volume supports. For more information, see EbsBlockDevice .

VolumeSize (integer) --
The volume size, in GiB. For more information, see EbsBlockDevice .

VolumeType (string) --
The volume type. gp2 for General Purpose (SSD) volumes, io1 for Provisioned IOPS (SSD) volumes, st1 for Throughput Optimized hard disk drives (HDD), sc1 for Cold HDD,and standard for Magnetic volumes.
If you specify the io1 volume type, you must also specify a value for the Iops attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1. AWS uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50 x (volume size).

DeleteOnTermination (boolean) --
Whether the volume is deleted on instance termination.







CreatedAt (string) --
The time that the instance was created.

EbsOptimized (boolean) --
Whether this is an Amazon EBS-optimized instance.

Ec2InstanceId (string) --
The ID of the associated Amazon EC2 instance.

EcsClusterArn (string) --
For container instances, the Amazon ECS cluster\'s ARN.

EcsContainerInstanceArn (string) --
For container instances, the instance\'s ARN.

ElasticIp (string) --
The instance Elastic IP address .

Hostname (string) --
The instance host name.

InfrastructureClass (string) --
For registered instances, the infrastructure class: ec2 or on-premises .

InstallUpdatesOnBoot (boolean) --
Whether to install operating system and package updates when the instance boots. The default value is true . If this value is set to false , you must then update your instances manually by using  CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.

Note
We strongly recommend using the default value of true , to ensure that your instances have the latest security updates.


InstanceId (string) --
The instance ID.

InstanceProfileArn (string) --
The ARN of the instance\'s IAM profile. For more information about IAM ARNs, see Using Identifiers .

InstanceType (string) --
The instance type, such as t2.micro .

LastServiceErrorId (string) --
The ID of the last service error. For more information, call  DescribeServiceErrors .

LayerIds (list) --
An array containing the instance layer IDs.

(string) --


Os (string) --
The instance\'s operating system.

Platform (string) --
The instance\'s platform.

PrivateDns (string) --
The instance\'s private DNS name.

PrivateIp (string) --
The instance\'s private IP address.

PublicDns (string) --
The instance public DNS name.

PublicIp (string) --
The instance public IP address.

RegisteredBy (string) --
For registered instances, who performed the registration.

ReportedAgentVersion (string) --
The instance\'s reported AWS OpsWorks Stacks agent version.

ReportedOs (dict) --
For registered instances, the reported operating system.

Family (string) --
The operating system family.

Name (string) --
The operating system name.

Version (string) --
The operating system version.



RootDeviceType (string) --
The instance\'s root device type. For more information, see Storage for the Root Device .

RootDeviceVolumeId (string) --
The root device volume ID.

SecurityGroupIds (list) --
An array containing the instance security group IDs.

(string) --


SshHostDsaKeyFingerprint (string) --
The SSH key\'s Deep Security Agent (DSA) fingerprint.

SshHostRsaKeyFingerprint (string) --
The SSH key\'s RSA fingerprint.

SshKeyName (string) --
The instance\'s Amazon EC2 key-pair name.

StackId (string) --
The stack ID.

Status (string) --
The instance status:

booting
connection_lost
online
pending
rebooting
requested
running_setup
setup_failed
shutting_down
start_failed
stop_failed
stopped
stopping
terminated
terminating


SubnetId (string) --
The instance\'s subnet ID; applicable only if the stack is running in a VPC.

Tenancy (string) --
The instance\'s tenancy option, such as dedicated or host .

VirtualizationType (string) --
The instance\'s virtualization type: paravirtual or hvm .











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Instances': [
            {
                'AgentVersion': 'string',
                'AmiId': 'string',
                'Architecture': 'x86_64'|'i386',
                'Arn': 'string',
                'AutoScalingType': 'load'|'timer',
                'AvailabilityZone': 'string',
                'BlockDeviceMappings': [
                    {
                        'DeviceName': 'string',
                        'NoDevice': 'string',
                        'VirtualName': 'string',
                        'Ebs': {
                            'SnapshotId': 'string',
                            'Iops': 123,
                            'VolumeSize': 123,
                            'VolumeType': 'gp2'|'io1'|'standard',
                            'DeleteOnTermination': True|False
                        }
                    },
                ],
                'CreatedAt': 'string',
                'EbsOptimized': True|False,
                'Ec2InstanceId': 'string',
                'EcsClusterArn': 'string',
                'EcsContainerInstanceArn': 'string',
                'ElasticIp': 'string',
                'Hostname': 'string',
                'InfrastructureClass': 'string',
                'InstallUpdatesOnBoot': True|False,
                'InstanceId': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'LastServiceErrorId': 'string',
                'LayerIds': [
                    'string',
                ],
                'Os': 'string',
                'Platform': 'string',
                'PrivateDns': 'string',
                'PrivateIp': 'string',
                'PublicDns': 'string',
                'PublicIp': 'string',
                'RegisteredBy': 'string',
                'ReportedAgentVersion': 'string',
                'ReportedOs': {
                    'Family': 'string',
                    'Name': 'string',
                    'Version': 'string'
                },
                'RootDeviceType': 'ebs'|'instance-store',
                'RootDeviceVolumeId': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SshHostDsaKeyFingerprint': 'string',
                'SshHostRsaKeyFingerprint': 'string',
                'SshKeyName': 'string',
                'StackId': 'string',
                'Status': 'string',
                'SubnetId': 'string',
                'Tenancy': 'string',
                'VirtualizationType': 'paravirtual'|'hvm'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_layers(StackId=None, LayerIds=None):
    """
    Requests a description of one or more layers in a specified stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_layers(
        StackId='string',
        LayerIds=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: The stack ID.

    :type LayerIds: list
    :param LayerIds: An array of layer IDs that specify the layers to be described. If you omit this parameter, DescribeLayers returns a description of every layer in the specified stack.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Layers': [
        {
            'Arn': 'string',
            'StackId': 'string',
            'LayerId': 'string',
            'Type': 'aws-flow-ruby'|'ecs-cluster'|'java-app'|'lb'|'web'|'php-app'|'rails-app'|'nodejs-app'|'memcached'|'db-master'|'monitoring-master'|'custom',
            'Name': 'string',
            'Shortname': 'string',
            'Attributes': {
                'string': 'string'
            },
            'CloudWatchLogsConfiguration': {
                'Enabled': True|False,
                'LogStreams': [
                    {
                        'LogGroupName': 'string',
                        'DatetimeFormat': 'string',
                        'TimeZone': 'LOCAL'|'UTC',
                        'File': 'string',
                        'FileFingerprintLines': 'string',
                        'MultiLineStartPattern': 'string',
                        'InitialPosition': 'start_of_file'|'end_of_file',
                        'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                        'BufferDuration': 123,
                        'BatchCount': 123,
                        'BatchSize': 123
                    },
                ]
            },
            'CustomInstanceProfileArn': 'string',
            'CustomJson': 'string',
            'CustomSecurityGroupIds': [
                'string',
            ],
            'DefaultSecurityGroupNames': [
                'string',
            ],
            'Packages': [
                'string',
            ],
            'VolumeConfigurations': [
                {
                    'MountPoint': 'string',
                    'RaidLevel': 123,
                    'NumberOfDisks': 123,
                    'Size': 123,
                    'VolumeType': 'string',
                    'Iops': 123,
                    'Encrypted': True|False
                },
            ],
            'EnableAutoHealing': True|False,
            'AutoAssignElasticIps': True|False,
            'AutoAssignPublicIps': True|False,
            'DefaultRecipes': {
                'Setup': [
                    'string',
                ],
                'Configure': [
                    'string',
                ],
                'Deploy': [
                    'string',
                ],
                'Undeploy': [
                    'string',
                ],
                'Shutdown': [
                    'string',
                ]
            },
            'CustomRecipes': {
                'Setup': [
                    'string',
                ],
                'Configure': [
                    'string',
                ],
                'Deploy': [
                    'string',
                ],
                'Undeploy': [
                    'string',
                ],
                'Shutdown': [
                    'string',
                ]
            },
            'CreatedAt': 'string',
            'InstallUpdatesOnBoot': True|False,
            'UseEbsOptimizedInstances': True|False,
            'LifecycleEventConfiguration': {
                'Shutdown': {
                    'ExecutionTimeout': 123,
                    'DelayUntilElbConnectionsDrained': True|False
                }
            }
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeLayers request.

Layers (list) --
An array of Layer objects that describe the layers.

(dict) --
Describes a layer.

Arn (string) --
The Amazon Resource Number (ARN) of a layer.

StackId (string) --
The layer stack ID.

LayerId (string) --
The layer ID.

Type (string) --
The layer type.

Name (string) --
The layer name.

Shortname (string) --
The layer short name.

Attributes (dict) --
The layer attributes.
For the HaproxyStatsPassword , MysqlRootPassword , and GangliaPassword attributes, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value
For an ECS Cluster layer, AWS OpsWorks Stacks the EcsClusterArn attribute is set to the cluster\'s ARN.

(string) --
(string) --




CloudWatchLogsConfiguration (dict) --
The Amazon CloudWatch Logs configuration settings for the layer.

Enabled (boolean) --
Whether CloudWatch Logs is enabled for a layer.

LogStreams (list) --
A list of configuration options for CloudWatch Logs.

(dict) --
Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the CloudWatch Logs Agent Reference .

LogGroupName (string) --
Specifies the destination log group. A log group is created automatically if it doesn\'t already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), \'/\' (forward slash), and \'.\' (period).

DatetimeFormat (string) --
Specifies how the time stamp is extracted from logs. For more information, see the CloudWatch Logs Agent Reference .

TimeZone (string) --
Specifies the time zone of log event time stamps.

File (string) --
Specifies log files that you want to push to CloudWatch Logs.

File can point to a specific file or multiple files (by using wild card characters such as /var/log/system.log* ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as access_log.2014-06-01-01 , access_log.2014-06-01-02 , and so on by using a pattern like access_log.* . Don\'t use a wildcard to match multiple file types, such as access_log_80 and access_log_443 . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

Zipped files are not supported.

FileFingerprintLines (string) --
Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as \'1\', \'2-5\'. The default value is \'1\', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

MultiLineStartPattern (string) --
Specifies the pattern for identifying the start of a log message.

InitialPosition (string) --
Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

Encoding (string) --
Specifies the encoding of the log file so that the file can be read correctly. The default is utf_8 . Encodings supported by Python codecs.decode() can be used here.

BufferDuration (integer) --
Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

BatchCount (integer) --
Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

BatchSize (integer) --
Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.







CustomInstanceProfileArn (string) --
The ARN of the default IAM profile to be used for the layer\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .

CustomJson (string) --
A JSON formatted string containing the layer\'s custom stack configuration and deployment attributes.

CustomSecurityGroupIds (list) --
An array containing the layer\'s custom security group IDs.

(string) --


DefaultSecurityGroupNames (list) --
An array containing the layer\'s security group names.

(string) --


Packages (list) --
An array of Package objects that describe the layer\'s packages.

(string) --


VolumeConfigurations (list) --
A VolumeConfigurations object that describes the layer\'s Amazon EBS volumes.

(dict) --
Describes an Amazon EBS volume configuration.

MountPoint (string) --
The volume mount point. For example "/dev/sdh".

RaidLevel (integer) --
The volume RAID level .

NumberOfDisks (integer) --
The number of disks in the volume.

Size (integer) --
The volume size.

VolumeType (string) --
The volume type. For more information, see Amazon EBS Volume Types .

standard - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.
io1 - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.
gp2 - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.
st1 - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
sc1 - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.


Iops (integer) --
For PIOPS volumes, the IOPS per disk.

Encrypted (boolean) --
Specifies whether an Amazon EBS volume is encrypted. For more information, see Amazon EBS Encryption .





EnableAutoHealing (boolean) --
Whether auto healing is disabled for the layer.

AutoAssignElasticIps (boolean) --
Whether to automatically assign an Elastic IP address to the layer\'s instances. For more information, see How to Edit a Layer .

AutoAssignPublicIps (boolean) --
For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer\'s instances. For more information, see How to Edit a Layer .

DefaultRecipes (dict) --
AWS OpsWorks Stacks supports five lifecycle events: setup , configuration , deploy , undeploy , and shutdown . For each layer, AWS OpsWorks Stacks runs a set of standard recipes for each event. You can also provide custom recipes for any or all layers and events. AWS OpsWorks Stacks runs custom event recipes after the standard recipes. LayerCustomRecipes specifies the custom recipes for a particular layer to be run in response to each of the five events.
To specify a recipe, use the cookbook\'s directory name in the repository followed by two colons and the recipe name, which is the recipe\'s file name without the .rb extension. For example: phpapp2::dbsetup specifies the dbsetup.rb recipe in the repository\'s phpapp2 folder.

Setup (list) --
An array of custom recipe names to be run following a setup event.

(string) --


Configure (list) --
An array of custom recipe names to be run following a configure event.

(string) --


Deploy (list) --
An array of custom recipe names to be run following a deploy event.

(string) --


Undeploy (list) --
An array of custom recipe names to be run following a undeploy event.

(string) --


Shutdown (list) --
An array of custom recipe names to be run following a shutdown event.

(string) --




CustomRecipes (dict) --
A LayerCustomRecipes object that specifies the layer\'s custom recipes.

Setup (list) --
An array of custom recipe names to be run following a setup event.

(string) --


Configure (list) --
An array of custom recipe names to be run following a configure event.

(string) --


Deploy (list) --
An array of custom recipe names to be run following a deploy event.

(string) --


Undeploy (list) --
An array of custom recipe names to be run following a undeploy event.

(string) --


Shutdown (list) --
An array of custom recipe names to be run following a shutdown event.

(string) --




CreatedAt (string) --
Date when the layer was created.

InstallUpdatesOnBoot (boolean) --
Whether to install operating system and package updates when the instance boots. The default value is true . If this value is set to false , you must then update your instances manually by using  CreateDeployment to run the update_dependencies stack command or manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.

Note
We strongly recommend using the default value of true , to ensure that your instances have the latest security updates.


UseEbsOptimizedInstances (boolean) --
Whether the layer uses Amazon EBS-optimized instances.

LifecycleEventConfiguration (dict) --
A LifeCycleEventConfiguration object that specifies the Shutdown event configuration.

Shutdown (dict) --
A ShutdownEventConfiguration object that specifies the Shutdown event configuration.

ExecutionTimeout (integer) --
The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.

DelayUntilElbConnectionsDrained (boolean) --
Whether to enable Elastic Load Balancing connection draining. For more information, see Connection Draining















Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Layers': [
            {
                'Arn': 'string',
                'StackId': 'string',
                'LayerId': 'string',
                'Type': 'aws-flow-ruby'|'ecs-cluster'|'java-app'|'lb'|'web'|'php-app'|'rails-app'|'nodejs-app'|'memcached'|'db-master'|'monitoring-master'|'custom',
                'Name': 'string',
                'Shortname': 'string',
                'Attributes': {
                    'string': 'string'
                },
                'CloudWatchLogsConfiguration': {
                    'Enabled': True|False,
                    'LogStreams': [
                        {
                            'LogGroupName': 'string',
                            'DatetimeFormat': 'string',
                            'TimeZone': 'LOCAL'|'UTC',
                            'File': 'string',
                            'FileFingerprintLines': 'string',
                            'MultiLineStartPattern': 'string',
                            'InitialPosition': 'start_of_file'|'end_of_file',
                            'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                            'BufferDuration': 123,
                            'BatchCount': 123,
                            'BatchSize': 123
                        },
                    ]
                },
                'CustomInstanceProfileArn': 'string',
                'CustomJson': 'string',
                'CustomSecurityGroupIds': [
                    'string',
                ],
                'DefaultSecurityGroupNames': [
                    'string',
                ],
                'Packages': [
                    'string',
                ],
                'VolumeConfigurations': [
                    {
                        'MountPoint': 'string',
                        'RaidLevel': 123,
                        'NumberOfDisks': 123,
                        'Size': 123,
                        'VolumeType': 'string',
                        'Iops': 123,
                        'Encrypted': True|False
                    },
                ],
                'EnableAutoHealing': True|False,
                'AutoAssignElasticIps': True|False,
                'AutoAssignPublicIps': True|False,
                'DefaultRecipes': {
                    'Setup': [
                        'string',
                    ],
                    'Configure': [
                        'string',
                    ],
                    'Deploy': [
                        'string',
                    ],
                    'Undeploy': [
                        'string',
                    ],
                    'Shutdown': [
                        'string',
                    ]
                },
                'CustomRecipes': {
                    'Setup': [
                        'string',
                    ],
                    'Configure': [
                        'string',
                    ],
                    'Deploy': [
                        'string',
                    ],
                    'Undeploy': [
                        'string',
                    ],
                    'Shutdown': [
                        'string',
                    ]
                },
                'CreatedAt': 'string',
                'InstallUpdatesOnBoot': True|False,
                'UseEbsOptimizedInstances': True|False,
                'LifecycleEventConfiguration': {
                    'Shutdown': {
                        'ExecutionTimeout': 123,
                        'DelayUntilElbConnectionsDrained': True|False
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_load_based_auto_scaling(LayerIds=None):
    """
    Describes load-based auto scaling configurations for specified layers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_load_based_auto_scaling(
        LayerIds=[
            'string',
        ]
    )
    
    
    :type LayerIds: list
    :param LayerIds: [REQUIRED]\nAn array of layer IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoadBasedAutoScalingConfigurations': [
        {
            'LayerId': 'string',
            'Enable': True|False,
            'UpScaling': {
                'InstanceCount': 123,
                'ThresholdsWaitTime': 123,
                'IgnoreMetricsTime': 123,
                'CpuThreshold': 123.0,
                'MemoryThreshold': 123.0,
                'LoadThreshold': 123.0,
                'Alarms': [
                    'string',
                ]
            },
            'DownScaling': {
                'InstanceCount': 123,
                'ThresholdsWaitTime': 123,
                'IgnoreMetricsTime': 123,
                'CpuThreshold': 123.0,
                'MemoryThreshold': 123.0,
                'LoadThreshold': 123.0,
                'Alarms': [
                    'string',
                ]
            }
        },
    ]
}


Response Structure

(dict) --Contains the response to a DescribeLoadBasedAutoScaling request.

LoadBasedAutoScalingConfigurations (list) --An array of LoadBasedAutoScalingConfiguration objects that describe each layer\'s configuration.

(dict) --Describes a layer\'s load-based auto scaling configuration.

LayerId (string) --The layer ID.

Enable (boolean) --Whether load-based auto scaling is enabled for the layer.

UpScaling (dict) --An AutoScalingThresholds object that describes the upscaling configuration, which defines how and when AWS OpsWorks Stacks increases the number of instances.

InstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.

ThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

IgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won\'t start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

CpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

MemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

LoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .

Alarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

Note
To use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks Stacks to Act on Your Behalf .


(string) --




DownScaling (dict) --An AutoScalingThresholds object that describes the downscaling configuration, which defines how and when AWS OpsWorks Stacks reduces the number of instances.

InstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.

ThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

IgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won\'t start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

CpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

MemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

LoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .

Alarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

Note
To use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks Stacks to Act on Your Behalf .


(string) --













Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'LoadBasedAutoScalingConfigurations': [
            {
                'LayerId': 'string',
                'Enable': True|False,
                'UpScaling': {
                    'InstanceCount': 123,
                    'ThresholdsWaitTime': 123,
                    'IgnoreMetricsTime': 123,
                    'CpuThreshold': 123.0,
                    'MemoryThreshold': 123.0,
                    'LoadThreshold': 123.0,
                    'Alarms': [
                        'string',
                    ]
                },
                'DownScaling': {
                    'InstanceCount': 123,
                    'ThresholdsWaitTime': 123,
                    'IgnoreMetricsTime': 123,
                    'CpuThreshold': 123.0,
                    'MemoryThreshold': 123.0,
                    'LoadThreshold': 123.0,
                    'Alarms': [
                        'string',
                    ]
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_my_user_profile():
    """
    Describes a user\'s SSH information.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_my_user_profile()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'UserProfile': {
        'IamUserArn': 'string',
        'Name': 'string',
        'SshUsername': 'string',
        'SshPublicKey': 'string'
    }
}


Response Structure

(dict) --Contains the response to a DescribeMyUserProfile request.

UserProfile (dict) --A UserProfile object that describes the user\'s SSH information.

IamUserArn (string) --The user\'s IAM ARN.

Name (string) --The user\'s name.

SshUsername (string) --The user\'s SSH user name.

SshPublicKey (string) --The user\'s SSH public key.









    :return: {
        'UserProfile': {
            'IamUserArn': 'string',
            'Name': 'string',
            'SshUsername': 'string',
            'SshPublicKey': 'string'
        }
    }
    
    
    """
    pass

def describe_operating_systems():
    """
    Describes the operating systems that are supported by AWS OpsWorks Stacks.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_operating_systems()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'OperatingSystems': [
        {
            'Name': 'string',
            'Id': 'string',
            'Type': 'string',
            'ConfigurationManagers': [
                {
                    'Name': 'string',
                    'Version': 'string'
                },
            ],
            'ReportedName': 'string',
            'ReportedVersion': 'string',
            'Supported': True|False
        },
    ]
}


Response Structure

(dict) --The response to a DescribeOperatingSystems request.

OperatingSystems (list) --Contains information in response to a DescribeOperatingSystems request.

(dict) --Describes supported operating systems in AWS OpsWorks Stacks.

Name (string) --The name of the operating system, such as Amazon Linux 2018.03 .

Id (string) --The ID of a supported operating system, such as Amazon Linux 2018.03 .

Type (string) --The type of a supported operating system, either Linux or Windows .

ConfigurationManagers (list) --Supported configuration manager name and versions for an AWS OpsWorks Stacks operating system.

(dict) --A block that contains information about the configuration manager (Chef) and the versions of the configuration manager that are supported for an operating system.

Name (string) --The name of the configuration manager, which is Chef.

Version (string) --The versions of the configuration manager that are supported by an operating system.





ReportedName (string) --A short name for the operating system manufacturer.

ReportedVersion (string) --The version of the operating system, including the release and edition, if applicable.

Supported (boolean) --Indicates that an operating system is not supported for new instances.











    :return: {
        'OperatingSystems': [
            {
                'Name': 'string',
                'Id': 'string',
                'Type': 'string',
                'ConfigurationManagers': [
                    {
                        'Name': 'string',
                        'Version': 'string'
                    },
                ],
                'ReportedName': 'string',
                'ReportedVersion': 'string',
                'Supported': True|False
            },
        ]
    }
    
    
    """
    pass

def describe_permissions(IamUserArn=None, StackId=None):
    """
    Describes the permissions for a specified stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_permissions(
        IamUserArn='string',
        StackId='string'
    )
    
    
    :type IamUserArn: string
    :param IamUserArn: The user\'s IAM ARN. This can also be a federated user\'s ARN. For more information about IAM ARNs, see Using Identifiers .

    :type StackId: string
    :param StackId: The stack ID.

    :rtype: dict

ReturnsResponse Syntax
{
    'Permissions': [
        {
            'StackId': 'string',
            'IamUserArn': 'string',
            'AllowSsh': True|False,
            'AllowSudo': True|False,
            'Level': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribePermissions request.

Permissions (list) --
An array of Permission objects that describe the stack permissions.

If the request object contains only a stack ID, the array contains a Permission object with permissions for each of the stack IAM ARNs.
If the request object contains only an IAM ARN, the array contains a Permission object with permissions for each of the user\'s stack IDs.
If the request contains a stack ID and an IAM ARN, the array contains a single Permission object with permissions for the specified stack and IAM ARN.


(dict) --
Describes stack or user permissions.

StackId (string) --
A stack ID.

IamUserArn (string) --
The Amazon Resource Name (ARN) for an AWS Identity and Access Management (IAM) role. For more information about IAM ARNs, see Using Identifiers .

AllowSsh (boolean) --
Whether the user can use SSH.

AllowSudo (boolean) --
Whether the user can use sudo .

Level (string) --
The user\'s permission level, which must be the following:

deny
show
deploy
manage
iam_only

For more information on the permissions associated with these levels, see Managing User Permissions











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Permissions': [
            {
                'StackId': 'string',
                'IamUserArn': 'string',
                'AllowSsh': True|False,
                'AllowSudo': True|False,
                'Level': 'string'
            },
        ]
    }
    
    
    :returns: 
    If the request object contains only a stack ID, the array contains a Permission object with permissions for each of the stack IAM ARNs.
    If the request object contains only an IAM ARN, the array contains a Permission object with permissions for each of the user\'s stack IDs.
    If the request contains a stack ID and an IAM ARN, the array contains a single Permission object with permissions for the specified stack and IAM ARN.
    
    """
    pass

def describe_raid_arrays(InstanceId=None, StackId=None, RaidArrayIds=None):
    """
    Describe an instance\'s RAID arrays.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_raid_arrays(
        InstanceId='string',
        StackId='string',
        RaidArrayIds=[
            'string',
        ]
    )
    
    
    :type InstanceId: string
    :param InstanceId: The instance ID. If you use this parameter, DescribeRaidArrays returns descriptions of the RAID arrays associated with the specified instance.

    :type StackId: string
    :param StackId: The stack ID.

    :type RaidArrayIds: list
    :param RaidArrayIds: An array of RAID array IDs. If you use this parameter, DescribeRaidArrays returns descriptions of the specified arrays. Otherwise, it returns a description of every array.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RaidArrays': [
        {
            'RaidArrayId': 'string',
            'InstanceId': 'string',
            'Name': 'string',
            'RaidLevel': 123,
            'NumberOfDisks': 123,
            'Size': 123,
            'Device': 'string',
            'MountPoint': 'string',
            'AvailabilityZone': 'string',
            'CreatedAt': 'string',
            'StackId': 'string',
            'VolumeType': 'string',
            'Iops': 123
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeRaidArrays request.

RaidArrays (list) --
A RaidArrays object that describes the specified RAID arrays.

(dict) --
Describes an instance\'s RAID array.

RaidArrayId (string) --
The array ID.

InstanceId (string) --
The instance ID.

Name (string) --
The array name.

RaidLevel (integer) --
The RAID level .

NumberOfDisks (integer) --
The number of disks in the array.

Size (integer) --
The array\'s size.

Device (string) --
The array\'s Linux device. For example /dev/mdadm0.

MountPoint (string) --
The array\'s mount point.

AvailabilityZone (string) --
The array\'s Availability Zone. For more information, see Regions and Endpoints .

CreatedAt (string) --
When the RAID array was created.

StackId (string) --
The stack ID.

VolumeType (string) --
The volume type, standard or PIOPS.

Iops (integer) --
For PIOPS volumes, the IOPS per disk.











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'RaidArrays': [
            {
                'RaidArrayId': 'string',
                'InstanceId': 'string',
                'Name': 'string',
                'RaidLevel': 123,
                'NumberOfDisks': 123,
                'Size': 123,
                'Device': 'string',
                'MountPoint': 'string',
                'AvailabilityZone': 'string',
                'CreatedAt': 'string',
                'StackId': 'string',
                'VolumeType': 'string',
                'Iops': 123
            },
        ]
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_rds_db_instances(StackId=None, RdsDbInstanceArns=None):
    """
    Describes Amazon RDS instances.
    This call accepts only one resource-identifying parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_rds_db_instances(
        StackId='string',
        RdsDbInstanceArns=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe ID of the stack with which the instances are registered. The operation returns descriptions of all registered Amazon RDS instances.\n

    :type RdsDbInstanceArns: list
    :param RdsDbInstanceArns: An array containing the ARNs of the instances to be described.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RdsDbInstances': [
        {
            'RdsDbInstanceArn': 'string',
            'DbInstanceIdentifier': 'string',
            'DbUser': 'string',
            'DbPassword': 'string',
            'Region': 'string',
            'Address': 'string',
            'Engine': 'string',
            'StackId': 'string',
            'MissingOnRds': True|False
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeRdsDbInstances request.

RdsDbInstances (list) --
An a array of RdsDbInstance objects that describe the instances.

(dict) --
Describes an Amazon RDS instance.

RdsDbInstanceArn (string) --
The instance\'s ARN.

DbInstanceIdentifier (string) --
The DB instance identifier.

DbUser (string) --
The master user name.

DbPassword (string) --
AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.

Region (string) --
The instance\'s AWS region.

Address (string) --
The instance\'s address.

Engine (string) --
The instance\'s database engine.

StackId (string) --
The ID of the stack with which the instance is registered.

MissingOnRds (boolean) --
Set to true if AWS OpsWorks Stacks is unable to discover the Amazon RDS instance. AWS OpsWorks Stacks attempts to discover the instance only once. If this value is set to true , you must deregister the instance, and then register it again.











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'RdsDbInstances': [
            {
                'RdsDbInstanceArn': 'string',
                'DbInstanceIdentifier': 'string',
                'DbUser': 'string',
                'DbPassword': 'string',
                'Region': 'string',
                'Address': 'string',
                'Engine': 'string',
                'StackId': 'string',
                'MissingOnRds': True|False
            },
        ]
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_service_errors(StackId=None, InstanceId=None, ServiceErrorIds=None):
    """
    Describes AWS OpsWorks Stacks service errors.
    This call accepts only one resource-identifying parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_service_errors(
        StackId='string',
        InstanceId='string',
        ServiceErrorIds=[
            'string',
        ]
    )
    
    
    :type StackId: string
    :param StackId: The stack ID. If you use this parameter, DescribeServiceErrors returns descriptions of the errors associated with the specified stack.

    :type InstanceId: string
    :param InstanceId: The instance ID. If you use this parameter, DescribeServiceErrors returns descriptions of the errors associated with the specified instance.

    :type ServiceErrorIds: list
    :param ServiceErrorIds: An array of service error IDs. If you use this parameter, DescribeServiceErrors returns descriptions of the specified errors. Otherwise, it returns a description of every error.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceErrors': [
        {
            'ServiceErrorId': 'string',
            'StackId': 'string',
            'InstanceId': 'string',
            'Type': 'string',
            'Message': 'string',
            'CreatedAt': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeServiceErrors request.

ServiceErrors (list) --
An array of ServiceError objects that describe the specified service errors.

(dict) --
Describes an AWS OpsWorks Stacks service error.

ServiceErrorId (string) --
The error ID.

StackId (string) --
The stack ID.

InstanceId (string) --
The instance ID.

Type (string) --
The error type.

Message (string) --
A message that describes the error.

CreatedAt (string) --
When the error occurred.











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'ServiceErrors': [
            {
                'ServiceErrorId': 'string',
                'StackId': 'string',
                'InstanceId': 'string',
                'Type': 'string',
                'Message': 'string',
                'CreatedAt': 'string'
            },
        ]
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_stack_provisioning_parameters(StackId=None):
    """
    Requests a description of a stack\'s provisioning parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stack_provisioning_parameters(
        StackId='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AgentInstallerUrl': 'string',
    'Parameters': {
        'string': 'string'
    }
}


Response Structure

(dict) --Contains the response to a DescribeStackProvisioningParameters request.

AgentInstallerUrl (string) --The AWS OpsWorks Stacks agent installer\'s URL.

Parameters (dict) --An embedded object that contains the provisioning parameters.

(string) --
(string) --









Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'AgentInstallerUrl': 'string',
        'Parameters': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_stack_summary(StackId=None):
    """
    Describes the number of layers and apps in a specified stack, and the number of instances in each state, such as running_setup or online .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stack_summary(
        StackId='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StackSummary': {
        'StackId': 'string',
        'Name': 'string',
        'Arn': 'string',
        'LayersCount': 123,
        'AppsCount': 123,
        'InstancesCount': {
            'Assigning': 123,
            'Booting': 123,
            'ConnectionLost': 123,
            'Deregistering': 123,
            'Online': 123,
            'Pending': 123,
            'Rebooting': 123,
            'Registered': 123,
            'Registering': 123,
            'Requested': 123,
            'RunningSetup': 123,
            'SetupFailed': 123,
            'ShuttingDown': 123,
            'StartFailed': 123,
            'StopFailed': 123,
            'Stopped': 123,
            'Stopping': 123,
            'Terminated': 123,
            'Terminating': 123,
            'Unassigning': 123
        }
    }
}


Response Structure

(dict) --Contains the response to a DescribeStackSummary request.

StackSummary (dict) --A StackSummary object that contains the results.

StackId (string) --The stack ID.

Name (string) --The stack name.

Arn (string) --The stack\'s ARN.

LayersCount (integer) --The number of layers.

AppsCount (integer) --The number of apps.

InstancesCount (dict) --An InstancesCount object with the number of instances in each status.

Assigning (integer) --The number of instances in the Assigning state.

Booting (integer) --The number of instances with booting status.

ConnectionLost (integer) --The number of instances with connection_lost status.

Deregistering (integer) --The number of instances in the Deregistering state.

Online (integer) --The number of instances with online status.

Pending (integer) --The number of instances with pending status.

Rebooting (integer) --The number of instances with rebooting status.

Registered (integer) --The number of instances in the Registered state.

Registering (integer) --The number of instances in the Registering state.

Requested (integer) --The number of instances with requested status.

RunningSetup (integer) --The number of instances with running_setup status.

SetupFailed (integer) --The number of instances with setup_failed status.

ShuttingDown (integer) --The number of instances with shutting_down status.

StartFailed (integer) --The number of instances with start_failed status.

StopFailed (integer) --The number of instances with stop_failed status.

Stopped (integer) --The number of instances with stopped status.

Stopping (integer) --The number of instances with stopping status.

Terminated (integer) --The number of instances with terminated status.

Terminating (integer) --The number of instances with terminating status.

Unassigning (integer) --The number of instances in the Unassigning state.










Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'StackSummary': {
            'StackId': 'string',
            'Name': 'string',
            'Arn': 'string',
            'LayersCount': 123,
            'AppsCount': 123,
            'InstancesCount': {
                'Assigning': 123,
                'Booting': 123,
                'ConnectionLost': 123,
                'Deregistering': 123,
                'Online': 123,
                'Pending': 123,
                'Rebooting': 123,
                'Registered': 123,
                'Registering': 123,
                'Requested': 123,
                'RunningSetup': 123,
                'SetupFailed': 123,
                'ShuttingDown': 123,
                'StartFailed': 123,
                'StopFailed': 123,
                'Stopped': 123,
                'Stopping': 123,
                'Terminated': 123,
                'Terminating': 123,
                'Unassigning': 123
            }
        }
    }
    
    
    """
    pass

def describe_stacks(StackIds=None):
    """
    Requests a description of one or more stacks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stacks(
        StackIds=[
            'string',
        ]
    )
    
    
    :type StackIds: list
    :param StackIds: An array of stack IDs that specify the stacks to be described. If you omit this parameter, DescribeStacks returns a description of every stack.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Stacks': [
        {
            'StackId': 'string',
            'Name': 'string',
            'Arn': 'string',
            'Region': 'string',
            'VpcId': 'string',
            'Attributes': {
                'string': 'string'
            },
            'ServiceRoleArn': 'string',
            'DefaultInstanceProfileArn': 'string',
            'DefaultOs': 'string',
            'HostnameTheme': 'string',
            'DefaultAvailabilityZone': 'string',
            'DefaultSubnetId': 'string',
            'CustomJson': 'string',
            'ConfigurationManager': {
                'Name': 'string',
                'Version': 'string'
            },
            'ChefConfiguration': {
                'ManageBerkshelf': True|False,
                'BerkshelfVersion': 'string'
            },
            'UseCustomCookbooks': True|False,
            'UseOpsworksSecurityGroups': True|False,
            'CustomCookbooksSource': {
                'Type': 'git'|'svn'|'archive'|'s3',
                'Url': 'string',
                'Username': 'string',
                'Password': 'string',
                'SshKey': 'string',
                'Revision': 'string'
            },
            'DefaultSshKeyName': 'string',
            'CreatedAt': 'string',
            'DefaultRootDeviceType': 'ebs'|'instance-store',
            'AgentVersion': 'string'
        },
    ]
}


Response Structure

(dict) --Contains the response to a DescribeStacks request.

Stacks (list) --An array of Stack objects that describe the stacks.

(dict) --Describes a stack.

StackId (string) --The stack ID.

Name (string) --The stack name.

Arn (string) --The stack\'s ARN.

Region (string) --The stack AWS region, such as "ap-northeast-2". For more information about AWS regions, see Regions and Endpoints .

VpcId (string) --The VPC ID; applicable only if the stack is running in a VPC.

Attributes (dict) --The stack\'s attributes.

(string) --
(string) --




ServiceRoleArn (string) --The stack AWS Identity and Access Management (IAM) role.

DefaultInstanceProfileArn (string) --The ARN of an IAM profile that is the default profile for all of the stack\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .

DefaultOs (string) --The stack\'s default operating system.

HostnameTheme (string) --The stack host name theme, with spaces replaced by underscores.

DefaultAvailabilityZone (string) --The stack\'s default Availability Zone. For more information, see Regions and Endpoints .

DefaultSubnetId (string) --The default subnet ID; applicable only if the stack is running in a VPC.

CustomJson (string) --A JSON object that contains user-defined attributes to be added to the stack configuration and deployment attributes. You can use custom JSON to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:

"{\\"key1\\": \\"value1\\", \\"key2\\": \\"value2\\",...}"
For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .

ConfigurationManager (dict) --The configuration manager.

Name (string) --The name. This parameter must be set to "Chef".

Version (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.



ChefConfiguration (dict) --A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version. For more information, see Create a New Stack .

ManageBerkshelf (boolean) --Whether to enable Berkshelf.

BerkshelfVersion (string) --The Berkshelf version.



UseCustomCookbooks (boolean) --Whether the stack uses custom cookbooks.

UseOpsworksSecurityGroups (boolean) --Whether the stack automatically associates the AWS OpsWorks Stacks built-in security groups with the stack\'s layers.

CustomCookbooksSource (dict) --Contains the information required to retrieve an app or cookbook from a repository. For more information, see Adding Apps or Cookbooks and Recipes .

Type (string) --The repository type.

Url (string) --The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .

Username (string) --This parameter depends on the repository type.

For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.


Password (string) --When included in a request, the parameter depends on the repository type.

For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
For HTTP bundles and Subversion repositories, set Password to the password.

For more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
In responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.

SshKey (string) --In requests, the repository\'s SSH key.
In responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.

Revision (string) --The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.



DefaultSshKeyName (string) --A default Amazon EC2 key pair for the stack\'s instances. You can override this value when you create or update an instance.

CreatedAt (string) --The date when the stack was created.

DefaultRootDeviceType (string) --The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see Storage for the Root Device .

AgentVersion (string) --The agent version. This parameter is set to LATEST for auto-update. or a version number for a fixed agent version.










Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Stacks': [
            {
                'StackId': 'string',
                'Name': 'string',
                'Arn': 'string',
                'Region': 'string',
                'VpcId': 'string',
                'Attributes': {
                    'string': 'string'
                },
                'ServiceRoleArn': 'string',
                'DefaultInstanceProfileArn': 'string',
                'DefaultOs': 'string',
                'HostnameTheme': 'string',
                'DefaultAvailabilityZone': 'string',
                'DefaultSubnetId': 'string',
                'CustomJson': 'string',
                'ConfigurationManager': {
                    'Name': 'string',
                    'Version': 'string'
                },
                'ChefConfiguration': {
                    'ManageBerkshelf': True|False,
                    'BerkshelfVersion': 'string'
                },
                'UseCustomCookbooks': True|False,
                'UseOpsworksSecurityGroups': True|False,
                'CustomCookbooksSource': {
                    'Type': 'git'|'svn'|'archive'|'s3',
                    'Url': 'string',
                    'Username': 'string',
                    'Password': 'string',
                    'SshKey': 'string',
                    'Revision': 'string'
                },
                'DefaultSshKeyName': 'string',
                'CreatedAt': 'string',
                'DefaultRootDeviceType': 'ebs'|'instance-store',
                'AgentVersion': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_time_based_auto_scaling(InstanceIds=None):
    """
    Describes time-based auto scaling configurations for specified instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_time_based_auto_scaling(
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]\nAn array of instance IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'TimeBasedAutoScalingConfigurations': [
        {
            'InstanceId': 'string',
            'AutoScalingSchedule': {
                'Monday': {
                    'string': 'string'
                },
                'Tuesday': {
                    'string': 'string'
                },
                'Wednesday': {
                    'string': 'string'
                },
                'Thursday': {
                    'string': 'string'
                },
                'Friday': {
                    'string': 'string'
                },
                'Saturday': {
                    'string': 'string'
                },
                'Sunday': {
                    'string': 'string'
                }
            }
        },
    ]
}


Response Structure

(dict) --Contains the response to a DescribeTimeBasedAutoScaling request.

TimeBasedAutoScalingConfigurations (list) --An array of TimeBasedAutoScalingConfiguration objects that describe the configuration for the specified instances.

(dict) --Describes an instance\'s time-based auto scaling configuration.

InstanceId (string) --The instance ID.

AutoScalingSchedule (dict) --A WeeklyAutoScalingSchedule object with the instance schedule.

Monday (dict) --The schedule for Monday.

(string) --
(string) --




Tuesday (dict) --The schedule for Tuesday.

(string) --
(string) --




Wednesday (dict) --The schedule for Wednesday.

(string) --
(string) --




Thursday (dict) --The schedule for Thursday.

(string) --
(string) --




Friday (dict) --The schedule for Friday.

(string) --
(string) --




Saturday (dict) --The schedule for Saturday.

(string) --
(string) --




Sunday (dict) --The schedule for Sunday.

(string) --
(string) --















Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'TimeBasedAutoScalingConfigurations': [
            {
                'InstanceId': 'string',
                'AutoScalingSchedule': {
                    'Monday': {
                        'string': 'string'
                    },
                    'Tuesday': {
                        'string': 'string'
                    },
                    'Wednesday': {
                        'string': 'string'
                    },
                    'Thursday': {
                        'string': 'string'
                    },
                    'Friday': {
                        'string': 'string'
                    },
                    'Saturday': {
                        'string': 'string'
                    },
                    'Sunday': {
                        'string': 'string'
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_user_profiles(IamUserArns=None):
    """
    Describe specified users.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_profiles(
        IamUserArns=[
            'string',
        ]
    )
    
    
    :type IamUserArns: list
    :param IamUserArns: An array of IAM or federated user ARNs that identify the users to be described.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UserProfiles': [
        {
            'IamUserArn': 'string',
            'Name': 'string',
            'SshUsername': 'string',
            'SshPublicKey': 'string',
            'AllowSelfManagement': True|False
        },
    ]
}


Response Structure

(dict) --Contains the response to a DescribeUserProfiles request.

UserProfiles (list) --A Users object that describes the specified users.

(dict) --Describes a user\'s SSH information.

IamUserArn (string) --The user\'s IAM ARN.

Name (string) --The user\'s name.

SshUsername (string) --The user\'s SSH user name.

SshPublicKey (string) --The user\'s SSH public key.

AllowSelfManagement (boolean) --Whether users can specify their own SSH public key through the My Settings page. For more information, see Managing User Permissions .










Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'UserProfiles': [
            {
                'IamUserArn': 'string',
                'Name': 'string',
                'SshUsername': 'string',
                'SshPublicKey': 'string',
                'AllowSelfManagement': True|False
            },
        ]
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_volumes(InstanceId=None, StackId=None, RaidArrayId=None, VolumeIds=None):
    """
    Describes an instance\'s Amazon EBS volumes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_volumes(
        InstanceId='string',
        StackId='string',
        RaidArrayId='string',
        VolumeIds=[
            'string',
        ]
    )
    
    
    :type InstanceId: string
    :param InstanceId: The instance ID. If you use this parameter, DescribeVolumes returns descriptions of the volumes associated with the specified instance.

    :type StackId: string
    :param StackId: A stack ID. The action describes the stack\'s registered Amazon EBS volumes.

    :type RaidArrayId: string
    :param RaidArrayId: The RAID array ID. If you use this parameter, DescribeVolumes returns descriptions of the volumes associated with the specified RAID array.

    :type VolumeIds: list
    :param VolumeIds: Am array of volume IDs. If you use this parameter, DescribeVolumes returns descriptions of the specified volumes. Otherwise, it returns a description of every volume.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Volumes': [
        {
            'VolumeId': 'string',
            'Ec2VolumeId': 'string',
            'Name': 'string',
            'RaidArrayId': 'string',
            'InstanceId': 'string',
            'Status': 'string',
            'Size': 123,
            'Device': 'string',
            'MountPoint': 'string',
            'Region': 'string',
            'AvailabilityZone': 'string',
            'VolumeType': 'string',
            'Iops': 123,
            'Encrypted': True|False
        },
    ]
}


Response Structure

(dict) --
Contains the response to a DescribeVolumes request.

Volumes (list) --
An array of volume IDs.

(dict) --
Describes an instance\'s Amazon EBS volume.

VolumeId (string) --
The volume ID.

Ec2VolumeId (string) --
The Amazon EC2 volume ID.

Name (string) --
The volume name.

RaidArrayId (string) --
The RAID array ID.

InstanceId (string) --
The instance ID.

Status (string) --
The value returned by DescribeVolumes .

Size (integer) --
The volume size.

Device (string) --
The device name.

MountPoint (string) --
The volume mount point. For example, "/mnt/disk1".

Region (string) --
The AWS region. For more information about AWS regions, see Regions and Endpoints .

AvailabilityZone (string) --
The volume Availability Zone. For more information, see Regions and Endpoints .

VolumeType (string) --
The volume type. For more information, see Amazon EBS Volume Types .

standard - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.
io1 - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.
gp2 - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.
st1 - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
sc1 - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.


Iops (integer) --
For PIOPS volumes, the IOPS per disk.

Encrypted (boolean) --
Specifies whether an Amazon EBS volume is encrypted. For more information, see Amazon EBS Encryption .











Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Volumes': [
            {
                'VolumeId': 'string',
                'Ec2VolumeId': 'string',
                'Name': 'string',
                'RaidArrayId': 'string',
                'InstanceId': 'string',
                'Status': 'string',
                'Size': 123,
                'Device': 'string',
                'MountPoint': 'string',
                'Region': 'string',
                'AvailabilityZone': 'string',
                'VolumeType': 'string',
                'Iops': 123,
                'Encrypted': True|False
            },
        ]
    }
    
    
    :returns: 
    standard - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.
    io1 - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.
    gp2 - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.
    st1 - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
    sc1 - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.
    
    """
    pass

def detach_elastic_load_balancer(ElasticLoadBalancerName=None, LayerId=None):
    """
    Detaches a specified Elastic Load Balancing instance from its layer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_elastic_load_balancer(
        ElasticLoadBalancerName='string',
        LayerId='string'
    )
    
    
    :type ElasticLoadBalancerName: string
    :param ElasticLoadBalancerName: [REQUIRED]\nThe Elastic Load Balancing instance\'s name.\n

    :type LayerId: string
    :param LayerId: [REQUIRED]\nThe ID of the layer that the Elastic Load Balancing instance is attached to.\n

    :returns: 
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def disassociate_elastic_ip(ElasticIp=None):
    """
    Disassociates an Elastic IP address from its instance. The address remains registered with the stack. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_elastic_ip(
        ElasticIp='string'
    )
    
    
    :type ElasticIp: string
    :param ElasticIp: [REQUIRED]\nThe Elastic IP address.\n

    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_hostname_suggestion(LayerId=None):
    """
    Gets a generated host name for the specified layer, based on the current host name theme.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_hostname_suggestion(
        LayerId='string'
    )
    
    
    :type LayerId: string
    :param LayerId: [REQUIRED]\nThe layer ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LayerId': 'string',
    'Hostname': 'string'
}


Response Structure

(dict) --Contains the response to a GetHostnameSuggestion request.

LayerId (string) --The layer ID.

Hostname (string) --The generated host name.






Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'LayerId': 'string',
        'Hostname': 'string'
    }
    
    
    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def grant_access(InstanceId=None, ValidForInMinutes=None):
    """
    Grants RDP access to a Windows instance for a specified time period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.grant_access(
        InstanceId='string',
        ValidForInMinutes=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance\'s AWS OpsWorks Stacks ID.\n

    :type ValidForInMinutes: integer
    :param ValidForInMinutes: The length of time (in minutes) that the grant is valid. When the grant expires at the end of this period, the user will no longer be able to use the credentials to log in. If the user is logged in at the time, he or she automatically will be logged out.

    :rtype: dict

ReturnsResponse Syntax
{
    'TemporaryCredential': {
        'Username': 'string',
        'Password': 'string',
        'ValidForInMinutes': 123,
        'InstanceId': 'string'
    }
}


Response Structure

(dict) --
Contains the response to a GrantAccess request.

TemporaryCredential (dict) --
A TemporaryCredential object that contains the data needed to log in to the instance by RDP clients, such as the Microsoft Remote Desktop Connection.

Username (string) --
The user name.

Password (string) --
The password.

ValidForInMinutes (integer) --
The length of time (in minutes) that the grant is valid. When the grant expires, at the end of this period, the user will no longer be able to use the credentials to log in. If they are logged in at the time, they will be automatically logged out.

InstanceId (string) --
The instance\'s AWS OpsWorks Stacks ID.









Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'TemporaryCredential': {
            'Username': 'string',
            'Password': 'string',
            'ValidForInMinutes': 123,
            'InstanceId': 'string'
        }
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_tags(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of tags that are applied to the specified stack or layer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe stack or layer\'s Amazon Resource Number (ARN).\n

    :type MaxResults: integer
    :param MaxResults: Do not use. A validation exception occurs if you add a MaxResults parameter to a ListTagsRequest call.

    :type NextToken: string
    :param NextToken: Do not use. A validation exception occurs if you add a NextToken parameter to a ListTagsRequest call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': {
        'string': 'string'
    },
    'NextToken': 'string'
}


Response Structure

(dict) --
Contains the response to a ListTags request.

Tags (dict) --
A set of key-value pairs that contain tag keys and tag values that are attached to a stack or layer.

(string) --
(string) --




NextToken (string) --
If a paginated request does not return all of the remaining results, this parameter is set to a token that you can assign to the request object\'s NextToken parameter to get the next set of results. If the previous paginated request returned all of the remaining results, this parameter is set to null .







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'Tags': {
            'string': 'string'
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def reboot_instance(InstanceId=None):
    """
    Reboots a specified instance. For more information, see Starting, Stopping, and Rebooting Instances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_instance(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    """
    pass

def register_ecs_cluster(EcsClusterArn=None, StackId=None):
    """
    Registers a specified Amazon ECS cluster with a stack. You can register only one cluster with a stack. A cluster can be registered with only one stack. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_ecs_cluster(
        EcsClusterArn='string',
        StackId='string'
    )
    
    
    :type EcsClusterArn: string
    :param EcsClusterArn: [REQUIRED]\nThe cluster\'s ARN.\n

    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EcsClusterArn': 'string'
}


Response Structure

(dict) --
Contains the response to a RegisterEcsCluster request.

EcsClusterArn (string) --
The cluster\'s ARN.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'EcsClusterArn': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def register_elastic_ip(ElasticIp=None, StackId=None):
    """
    Registers an Elastic IP address with a specified stack. An address can be registered with only one stack at a time. If the address is already registered, you must first deregister it by calling  DeregisterElasticIp . For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_elastic_ip(
        ElasticIp='string',
        StackId='string'
    )
    
    
    :type ElasticIp: string
    :param ElasticIp: [REQUIRED]\nThe Elastic IP address.\n

    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ElasticIp': 'string'
}


Response Structure

(dict) --
Contains the response to a RegisterElasticIp request.

ElasticIp (string) --
The Elastic IP address.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'ElasticIp': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def register_instance(StackId=None, Hostname=None, PublicIp=None, PrivateIp=None, RsaPublicKey=None, RsaPublicKeyFingerprint=None, InstanceIdentity=None):
    """
    Registers instances that were created outside of AWS OpsWorks Stacks with a specified stack.
    Registered instances have the same requirements as instances that are created by using the  CreateInstance API. For example, registered instances must be running a supported Linux-based operating system, and they must have a supported instance type. For more information about requirements for instances that you want to register, see Preparing the Instance .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_instance(
        StackId='string',
        Hostname='string',
        PublicIp='string',
        PrivateIp='string',
        RsaPublicKey='string',
        RsaPublicKeyFingerprint='string',
        InstanceIdentity={
            'Document': 'string',
            'Signature': 'string'
        }
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe ID of the stack that the instance is to be registered with.\n

    :type Hostname: string
    :param Hostname: The instance\'s hostname.

    :type PublicIp: string
    :param PublicIp: The instance\'s public IP address.

    :type PrivateIp: string
    :param PrivateIp: The instance\'s private IP address.

    :type RsaPublicKey: string
    :param RsaPublicKey: The instances public RSA key. This key is used to encrypt communication between the instance and the service.

    :type RsaPublicKeyFingerprint: string
    :param RsaPublicKeyFingerprint: The instances public RSA key fingerprint.

    :type InstanceIdentity: dict
    :param InstanceIdentity: An InstanceIdentity object that contains the instance\'s identity.\n\nDocument (string) --A JSON document that contains the metadata.\n\nSignature (string) --A signature that can be used to verify the document\'s accuracy and authenticity.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InstanceId': 'string'
}


Response Structure

(dict) --
Contains the response to a RegisterInstanceResult request.

InstanceId (string) --
The registered instance\'s AWS OpsWorks Stacks ID.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'InstanceId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def register_rds_db_instance(StackId=None, RdsDbInstanceArn=None, DbUser=None, DbPassword=None):
    """
    Registers an Amazon RDS instance with a stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_rds_db_instance(
        StackId='string',
        RdsDbInstanceArn='string',
        DbUser='string',
        DbPassword='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :type RdsDbInstanceArn: string
    :param RdsDbInstanceArn: [REQUIRED]\nThe Amazon RDS instance\'s ARN.\n

    :type DbUser: string
    :param DbUser: [REQUIRED]\nThe database\'s master user name.\n

    :type DbPassword: string
    :param DbPassword: [REQUIRED]\nThe database password.\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def register_volume(Ec2VolumeId=None, StackId=None):
    """
    Registers an Amazon EBS volume with a specified stack. A volume can be registered with only one stack at a time. If the volume is already registered, you must first deregister it by calling  DeregisterVolume . For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_volume(
        Ec2VolumeId='string',
        StackId='string'
    )
    
    
    :type Ec2VolumeId: string
    :param Ec2VolumeId: The Amazon EBS volume ID.

    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeId': 'string'
}


Response Structure

(dict) --
Contains the response to a RegisterVolume request.

VolumeId (string) --
The volume ID.







Exceptions

OpsWorks.Client.exceptions.ValidationException
OpsWorks.Client.exceptions.ResourceNotFoundException


    :return: {
        'VolumeId': 'string'
    }
    
    
    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def set_load_based_auto_scaling(LayerId=None, Enable=None, UpScaling=None, DownScaling=None):
    """
    Specify the load-based auto scaling configuration for a specified layer. For more information, see Managing Load with Time-based and Load-based Instances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_load_based_auto_scaling(
        LayerId='string',
        Enable=True|False,
        UpScaling={
            'InstanceCount': 123,
            'ThresholdsWaitTime': 123,
            'IgnoreMetricsTime': 123,
            'CpuThreshold': 123.0,
            'MemoryThreshold': 123.0,
            'LoadThreshold': 123.0,
            'Alarms': [
                'string',
            ]
        },
        DownScaling={
            'InstanceCount': 123,
            'ThresholdsWaitTime': 123,
            'IgnoreMetricsTime': 123,
            'CpuThreshold': 123.0,
            'MemoryThreshold': 123.0,
            'LoadThreshold': 123.0,
            'Alarms': [
                'string',
            ]
        }
    )
    
    
    :type LayerId: string
    :param LayerId: [REQUIRED]\nThe layer ID.\n

    :type Enable: boolean
    :param Enable: Enables load-based auto scaling for the layer.

    :type UpScaling: dict
    :param UpScaling: An AutoScalingThresholds object with the upscaling threshold configuration. If the load exceeds these thresholds for a specified amount of time, AWS OpsWorks Stacks starts a specified number of instances.\n\nInstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.\n\nThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.\n\nIgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won\'t start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.\n\nCpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.\n\nMemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.\n\nLoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .\n\nAlarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.\n\nNote\nTo use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks Stacks to Act on Your Behalf .\n\n\n(string) --\n\n\n\n

    :type DownScaling: dict
    :param DownScaling: An AutoScalingThresholds object with the downscaling threshold configuration. If the load falls below these thresholds for a specified amount of time, AWS OpsWorks Stacks stops a specified number of instances.\n\nInstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.\n\nThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.\n\nIgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won\'t start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.\n\nCpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.\n\nMemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.\n\nLoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .\n\nAlarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.\n\nNote\nTo use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks Stacks to Act on Your Behalf .\n\n\n(string) --\n\n\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def set_permission(StackId=None, IamUserArn=None, AllowSsh=None, AllowSudo=None, Level=None):
    """
    Specifies a user\'s permissions. For more information, see Security and Permissions .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_permission(
        StackId='string',
        IamUserArn='string',
        AllowSsh=True|False,
        AllowSudo=True|False,
        Level='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :type IamUserArn: string
    :param IamUserArn: [REQUIRED]\nThe user\'s IAM ARN. This can also be a federated user\'s ARN.\n

    :type AllowSsh: boolean
    :param AllowSsh: The user is allowed to use SSH to communicate with the instance.

    :type AllowSudo: boolean
    :param AllowSudo: The user is allowed to use sudo to elevate privileges.

    :type Level: string
    :param Level: The user\'s permission level, which must be set to one of the following strings. You cannot set your own permissions level.\n\ndeny\nshow\ndeploy\nmanage\niam_only\n\nFor more information about the permissions associated with these levels, see Managing User Permissions .\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def set_time_based_auto_scaling(InstanceId=None, AutoScalingSchedule=None):
    """
    Specify the time-based auto scaling configuration for a specified instance. For more information, see Managing Load with Time-based and Load-based Instances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_time_based_auto_scaling(
        InstanceId='string',
        AutoScalingSchedule={
            'Monday': {
                'string': 'string'
            },
            'Tuesday': {
                'string': 'string'
            },
            'Wednesday': {
                'string': 'string'
            },
            'Thursday': {
                'string': 'string'
            },
            'Friday': {
                'string': 'string'
            },
            'Saturday': {
                'string': 'string'
            },
            'Sunday': {
                'string': 'string'
            }
        }
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    :type AutoScalingSchedule: dict
    :param AutoScalingSchedule: An AutoScalingSchedule with the instance schedule.\n\nMonday (dict) --The schedule for Monday.\n\n(string) --\n(string) --\n\n\n\n\nTuesday (dict) --The schedule for Tuesday.\n\n(string) --\n(string) --\n\n\n\n\nWednesday (dict) --The schedule for Wednesday.\n\n(string) --\n(string) --\n\n\n\n\nThursday (dict) --The schedule for Thursday.\n\n(string) --\n(string) --\n\n\n\n\nFriday (dict) --The schedule for Friday.\n\n(string) --\n(string) --\n\n\n\n\nSaturday (dict) --The schedule for Saturday.\n\n(string) --\n(string) --\n\n\n\n\nSunday (dict) --The schedule for Sunday.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def start_instance(InstanceId=None):
    """
    Starts a specified instance. For more information, see Starting, Stopping, and Rebooting Instances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_instance(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    """
    pass

def start_stack(StackId=None):
    """
    Starts a stack\'s instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_stack(
        StackId='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    """
    pass

def stop_instance(InstanceId=None, Force=None):
    """
    Stops a specified instance. When you stop a standard instance, the data disappears and must be reinstalled when you restart the instance. You can stop an Amazon EBS-backed instance without losing data. For more information, see Starting, Stopping, and Rebooting Instances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_instance(
        InstanceId='string',
        Force=True|False
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    :type Force: boolean
    :param Force: Specifies whether to force an instance to stop. If the instance\'s root device type is ebs , or EBS-backed, adding the Force parameter to the StopInstances API call disassociates the AWS OpsWorks Stacks instance from EC2, and forces deletion of only the OpsWorks Stacks instance. You must also delete the formerly-associated instance in EC2 after troubleshooting and replacing the AWS OpsWorks Stacks instance with a new one.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def stop_stack(StackId=None):
    """
    Stops a specified stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_stack(
        StackId='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Apply cost-allocation tags to a specified stack or layer in AWS OpsWorks Stacks. For more information about how tagging works, see Tags in the AWS OpsWorks User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe stack or layer\'s Amazon Resource Number (ARN).\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nA map that contains tag keys and tag values that are attached to a stack or layer.\n\nThe key cannot be empty.\nThe key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\nThe value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\nLeading and trailing white spaces are trimmed from both the key and value.\nA maximum of 40 tags is allowed for any resource.\n\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def unassign_instance(InstanceId=None):
    """
    Unassigns a registered instance from all layers that are using the instance. The instance remains in the stack as an unassigned instance, and can be assigned to another layer as needed. You cannot use this action with instances that were created with AWS OpsWorks Stacks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unassign_instance(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    """
    pass

def unassign_volume(VolumeId=None):
    """
    Unassigns an assigned Amazon EBS volume. The volume remains registered with the stack. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unassign_volume(
        VolumeId='string'
    )
    
    
    :type VolumeId: string
    :param VolumeId: [REQUIRED]\nThe volume ID.\n

    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes tags from a specified stack or layer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe stack or layer\'s Amazon Resource Number (ARN).\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of the keys of tags to be removed from a stack or layer.\n\n(string) --\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_app(AppId=None, Name=None, Description=None, DataSources=None, Type=None, AppSource=None, Domains=None, EnableSsl=None, SslConfiguration=None, Attributes=None, Environment=None):
    """
    Updates a specified app.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_app(
        AppId='string',
        Name='string',
        Description='string',
        DataSources=[
            {
                'Type': 'string',
                'Arn': 'string',
                'DatabaseName': 'string'
            },
        ],
        Type='aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
        AppSource={
            'Type': 'git'|'svn'|'archive'|'s3',
            'Url': 'string',
            'Username': 'string',
            'Password': 'string',
            'SshKey': 'string',
            'Revision': 'string'
        },
        Domains=[
            'string',
        ],
        EnableSsl=True|False,
        SslConfiguration={
            'Certificate': 'string',
            'PrivateKey': 'string',
            'Chain': 'string'
        },
        Attributes={
            'string': 'string'
        },
        Environment=[
            {
                'Key': 'string',
                'Value': 'string',
                'Secure': True|False
            },
        ]
    )
    
    
    :type AppId: string
    :param AppId: [REQUIRED]\nThe app ID.\n

    :type Name: string
    :param Name: The app name.

    :type Description: string
    :param Description: A description of the app.

    :type DataSources: list
    :param DataSources: The app\'s data sources.\n\n(dict) --Describes an app\'s data source.\n\nType (string) --The data source\'s type, AutoSelectOpsworksMysqlInstance , OpsworksMysqlInstance , RdsDbInstance , or None .\n\nArn (string) --The data source\'s ARN.\n\nDatabaseName (string) --The database name.\n\n\n\n\n

    :type Type: string
    :param Type: The app type.

    :type AppSource: dict
    :param AppSource: A Source object that specifies the app repository.\n\nType (string) --The repository type.\n\nUrl (string) --The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .\n\nUsername (string) --This parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Username to the appropriate IAM access key ID.\nFor HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.\n\n\nPassword (string) --When included in a request, the parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Password to the appropriate IAM secret access key.\nFor HTTP bundles and Subversion repositories, set Password to the password.\n\nFor more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nSshKey (string) --In requests, the repository\'s SSH key.\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nRevision (string) --The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.\n\n\n

    :type Domains: list
    :param Domains: The app\'s virtual host settings, with multiple domains separated by commas. For example: \'www.example.com, example.com\'\n\n(string) --\n\n

    :type EnableSsl: boolean
    :param EnableSsl: Whether SSL is enabled for the app.

    :type SslConfiguration: dict
    :param SslConfiguration: An SslConfiguration object with the SSL configuration.\n\nCertificate (string) -- [REQUIRED]The contents of the certificate\'s domain.crt file.\n\nPrivateKey (string) -- [REQUIRED]The private key; the contents of the certificate\'s domain.kex file.\n\nChain (string) --Optional. Can be used to specify an intermediate certificate authority key or client authentication.\n\n\n

    :type Attributes: dict
    :param Attributes: One or more user-defined key/value pairs to be added to the stack attributes.\n\n(string) --\n(string) --\n\n\n\n

    :type Environment: list
    :param Environment: An array of EnvironmentVariable objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instances.For more information, see Environment Variables .\nThere is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables\' names, values, and protected flag values - cannot exceed 20 KB. This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, 'Environment: is too large (maximum is 20 KB).'\n\nNote\nIf you have specified one or more environment variables, you cannot modify the stack\'s Chef version.\n\n\n(dict) --Represents an app\'s environment variable.\n\nKey (string) -- [REQUIRED](Required) The environment variable\'s name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.\n\nValue (string) -- [REQUIRED](Optional) The environment variable\'s value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.\n\nSecure (boolean) --(Optional) Whether the variable\'s value will be returned by the DescribeApps action. To conceal an environment variable\'s value, set Secure to true . DescribeApps then returns *****FILTERED***** instead of the actual value. The default value for Secure is false .\n\n\n\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_elastic_ip(ElasticIp=None, Name=None):
    """
    Updates a registered Elastic IP address\'s name. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_elastic_ip(
        ElasticIp='string',
        Name='string'
    )
    
    
    :type ElasticIp: string
    :param ElasticIp: [REQUIRED]\nThe IP address for which you want to update the name.\n

    :type Name: string
    :param Name: The new name.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_instance(InstanceId=None, LayerIds=None, InstanceType=None, AutoScalingType=None, Hostname=None, Os=None, AmiId=None, SshKeyName=None, Architecture=None, InstallUpdatesOnBoot=None, EbsOptimized=None, AgentVersion=None):
    """
    Updates a specified instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_instance(
        InstanceId='string',
        LayerIds=[
            'string',
        ],
        InstanceType='string',
        AutoScalingType='load'|'timer',
        Hostname='string',
        Os='string',
        AmiId='string',
        SshKeyName='string',
        Architecture='x86_64'|'i386',
        InstallUpdatesOnBoot=True|False,
        EbsOptimized=True|False,
        AgentVersion='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID.\n

    :type LayerIds: list
    :param LayerIds: The instance\'s layer IDs.\n\n(string) --\n\n

    :type InstanceType: string
    :param InstanceType: The instance type, such as t2.micro . For a list of supported instance types, open the stack in the console, choose Instances , and choose + Instance . The Size list contains the currently supported types. For more information, see Instance Families and Types . The parameter values that you use to specify the various types are in the API Name column of the Available Instance Types table.

    :type AutoScalingType: string
    :param AutoScalingType: For load-based or time-based instances, the type. Windows stacks can use only time-based instances.

    :type Hostname: string
    :param Hostname: The instance host name.

    :type Os: string
    :param Os: The instance\'s operating system, which must be set to one of the following. You cannot update an instance that is using a custom AMI.\n\nA supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2018.03 , Amazon Linux 2017.09 , Amazon Linux 2017.03 , Amazon Linux 2016.09 , Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .\nA supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .\nCentOS Linux 7\nRed Hat Enterprise Linux 7\nA supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .\n\nFor more information about supported operating systems, see AWS OpsWorks Stacks Operating Systems .\nThe default option is the current Amazon Linux version. If you set this parameter to Custom , you must use the AmiId parameter to specify the custom AMI that you want to use. For more information about supported operating systems, see Operating Systems . For more information about how to use custom AMIs with OpsWorks, see Using Custom AMIs .\n\nNote\nYou can specify a different Linux operating system for the updated stack, but you cannot change from Linux to Windows or Windows to Linux.\n\n

    :type AmiId: string
    :param AmiId: The ID of the AMI that was used to create the instance. The value of this parameter must be the same AMI ID that the instance is already using. You cannot apply a new AMI to an instance by running UpdateInstance. UpdateInstance does not work on instances that are using custom AMIs.

    :type SshKeyName: string
    :param SshKeyName: The instance\'s Amazon EC2 key name.

    :type Architecture: string
    :param Architecture: The instance architecture. Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see Instance Families and Types .

    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.\n\nNote\nWe strongly recommend using the default value of true , to ensure that your instances have the latest security updates.\n\n

    :type EbsOptimized: boolean
    :param EbsOptimized: This property cannot be updated.

    :type AgentVersion: string
    :param AgentVersion: The default AWS OpsWorks Stacks agent version. You have the following options:\n\nINHERIT - Use the stack\'s default agent version setting.\nversion_number - Use the specified agent version. This value overrides the stack\'s default setting. To update the agent version, you must edit the instance configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the instance.\n\nThe default setting is INHERIT . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions .\nAgentVersion cannot be set to Chef 12.2.\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_layer(LayerId=None, Name=None, Shortname=None, Attributes=None, CloudWatchLogsConfiguration=None, CustomInstanceProfileArn=None, CustomJson=None, CustomSecurityGroupIds=None, Packages=None, VolumeConfigurations=None, EnableAutoHealing=None, AutoAssignElasticIps=None, AutoAssignPublicIps=None, CustomRecipes=None, InstallUpdatesOnBoot=None, UseEbsOptimizedInstances=None, LifecycleEventConfiguration=None):
    """
    Updates a specified layer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_layer(
        LayerId='string',
        Name='string',
        Shortname='string',
        Attributes={
            'string': 'string'
        },
        CloudWatchLogsConfiguration={
            'Enabled': True|False,
            'LogStreams': [
                {
                    'LogGroupName': 'string',
                    'DatetimeFormat': 'string',
                    'TimeZone': 'LOCAL'|'UTC',
                    'File': 'string',
                    'FileFingerprintLines': 'string',
                    'MultiLineStartPattern': 'string',
                    'InitialPosition': 'start_of_file'|'end_of_file',
                    'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                    'BufferDuration': 123,
                    'BatchCount': 123,
                    'BatchSize': 123
                },
            ]
        },
        CustomInstanceProfileArn='string',
        CustomJson='string',
        CustomSecurityGroupIds=[
            'string',
        ],
        Packages=[
            'string',
        ],
        VolumeConfigurations=[
            {
                'MountPoint': 'string',
                'RaidLevel': 123,
                'NumberOfDisks': 123,
                'Size': 123,
                'VolumeType': 'string',
                'Iops': 123,
                'Encrypted': True|False
            },
        ],
        EnableAutoHealing=True|False,
        AutoAssignElasticIps=True|False,
        AutoAssignPublicIps=True|False,
        CustomRecipes={
            'Setup': [
                'string',
            ],
            'Configure': [
                'string',
            ],
            'Deploy': [
                'string',
            ],
            'Undeploy': [
                'string',
            ],
            'Shutdown': [
                'string',
            ]
        },
        InstallUpdatesOnBoot=True|False,
        UseEbsOptimizedInstances=True|False,
        LifecycleEventConfiguration={
            'Shutdown': {
                'ExecutionTimeout': 123,
                'DelayUntilElbConnectionsDrained': True|False
            }
        }
    )
    
    
    :type LayerId: string
    :param LayerId: [REQUIRED]\nThe layer ID.\n

    :type Name: string
    :param Name: The layer name, which is used by the console.

    :type Shortname: string
    :param Shortname: For custom layers only, use this parameter to specify the layer\'s short name, which is used internally by AWS OpsWorks Stacks and by Chef. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters and must be in the following format: /A[a-z0-9-_.]+Z/.\nThe built-in layers\' short names are defined by AWS OpsWorks Stacks. For more information, see the Layer Reference\n

    :type Attributes: dict
    :param Attributes: One or more user-defined key/value pairs to be added to the stack attributes.\n\n(string) --\n(string) --\n\n\n\n

    :type CloudWatchLogsConfiguration: dict
    :param CloudWatchLogsConfiguration: Specifies CloudWatch Logs configuration options for the layer. For more information, see CloudWatchLogsLogStream .\n\nEnabled (boolean) --Whether CloudWatch Logs is enabled for a layer.\n\nLogStreams (list) --A list of configuration options for CloudWatch Logs.\n\n(dict) --Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the CloudWatch Logs Agent Reference .\n\nLogGroupName (string) --Specifies the destination log group. A log group is created automatically if it doesn\'t already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), \'/\' (forward slash), and \'.\' (period).\n\nDatetimeFormat (string) --Specifies how the time stamp is extracted from logs. For more information, see the CloudWatch Logs Agent Reference .\n\nTimeZone (string) --Specifies the time zone of log event time stamps.\n\nFile (string) --Specifies log files that you want to push to CloudWatch Logs.\n\nFile can point to a specific file or multiple files (by using wild card characters such as /var/log/system.log* ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as access_log.2014-06-01-01 , access_log.2014-06-01-02 , and so on by using a pattern like access_log.* . Don\'t use a wildcard to match multiple file types, such as access_log_80 and access_log_443 . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.\nZipped files are not supported.\n\nFileFingerprintLines (string) --Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as \'1\', \'2-5\'. The default value is \'1\', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.\n\nMultiLineStartPattern (string) --Specifies the pattern for identifying the start of a log message.\n\nInitialPosition (string) --Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.\n\nEncoding (string) --Specifies the encoding of the log file so that the file can be read correctly. The default is utf_8 . Encodings supported by Python codecs.decode() can be used here.\n\nBufferDuration (integer) --Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.\n\nBatchCount (integer) --Specifies the max number of log events in a batch, up to 10000. The default value is 1000.\n\nBatchSize (integer) --Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.\n\n\n\n\n\n\n

    :type CustomInstanceProfileArn: string
    :param CustomInstanceProfileArn: The ARN of an IAM profile to be used for all of the layer\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .

    :type CustomJson: string
    :param CustomJson: A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer\'s instances. For more information, see Using Custom JSON .

    :type CustomSecurityGroupIds: list
    :param CustomSecurityGroupIds: An array containing the layer\'s custom security group IDs.\n\n(string) --\n\n

    :type Packages: list
    :param Packages: An array of Package objects that describe the layer\'s packages.\n\n(string) --\n\n

    :type VolumeConfigurations: list
    :param VolumeConfigurations: A VolumeConfigurations object that describes the layer\'s Amazon EBS volumes.\n\n(dict) --Describes an Amazon EBS volume configuration.\n\nMountPoint (string) -- [REQUIRED]The volume mount point. For example '/dev/sdh'.\n\nRaidLevel (integer) --The volume RAID level .\n\nNumberOfDisks (integer) -- [REQUIRED]The number of disks in the volume.\n\nSize (integer) -- [REQUIRED]The volume size.\n\nVolumeType (string) --The volume type. For more information, see Amazon EBS Volume Types .\n\nstandard - Magnetic. Magnetic volumes must have a minimum size of 1 GiB and a maximum size of 1024 GiB.\nio1 - Provisioned IOPS (SSD). PIOPS volumes must have a minimum size of 4 GiB and a maximum size of 16384 GiB.\ngp2 - General Purpose (SSD). General purpose volumes must have a minimum size of 1 GiB and a maximum size of 16384 GiB.\nst1 - Throughput Optimized hard disk drive (HDD). Throughput optimized HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.\nsc1 - Cold HDD. Cold HDD volumes must have a minimum size of 500 GiB and a maximum size of 16384 GiB.\n\n\nIops (integer) --For PIOPS volumes, the IOPS per disk.\n\nEncrypted (boolean) --Specifies whether an Amazon EBS volume is encrypted. For more information, see Amazon EBS Encryption .\n\n\n\n\n

    :type EnableAutoHealing: boolean
    :param EnableAutoHealing: Whether to disable auto healing for the layer.

    :type AutoAssignElasticIps: boolean
    :param AutoAssignElasticIps: Whether to automatically assign an Elastic IP address to the layer\'s instances. For more information, see How to Edit a Layer .

    :type AutoAssignPublicIps: boolean
    :param AutoAssignPublicIps: For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer\'s instances. For more information, see How to Edit a Layer .

    :type CustomRecipes: dict
    :param CustomRecipes: A LayerCustomRecipes object that specifies the layer\'s custom recipes.\n\nSetup (list) --An array of custom recipe names to be run following a setup event.\n\n(string) --\n\n\nConfigure (list) --An array of custom recipe names to be run following a configure event.\n\n(string) --\n\n\nDeploy (list) --An array of custom recipe names to be run following a deploy event.\n\n(string) --\n\n\nUndeploy (list) --An array of custom recipe names to be run following a undeploy event.\n\n(string) --\n\n\nShutdown (list) --An array of custom recipe names to be run following a shutdown event.\n\n(string) --\n\n\n\n

    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.\n\nNote\nWe strongly recommend using the default value of true , to ensure that your instances have the latest security updates.\n\n

    :type UseEbsOptimizedInstances: boolean
    :param UseEbsOptimizedInstances: Whether to use Amazon EBS-optimized instances.

    :type LifecycleEventConfiguration: dict
    :param LifecycleEventConfiguration: \nShutdown (dict) --A ShutdownEventConfiguration object that specifies the Shutdown event configuration.\n\nExecutionTimeout (integer) --The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.\n\nDelayUntilElbConnectionsDrained (boolean) --Whether to enable Elastic Load Balancing connection draining. For more information, see Connection Draining\n\n\n\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_my_user_profile(SshPublicKey=None):
    """
    Updates a user\'s SSH public key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_my_user_profile(
        SshPublicKey='string'
    )
    
    
    :type SshPublicKey: string
    :param SshPublicKey: The user\'s SSH public key.

    """
    pass

def update_rds_db_instance(RdsDbInstanceArn=None, DbUser=None, DbPassword=None):
    """
    Updates an Amazon RDS instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rds_db_instance(
        RdsDbInstanceArn='string',
        DbUser='string',
        DbPassword='string'
    )
    
    
    :type RdsDbInstanceArn: string
    :param RdsDbInstanceArn: [REQUIRED]\nThe Amazon RDS instance\'s ARN.\n

    :type DbUser: string
    :param DbUser: The master user name.

    :type DbPassword: string
    :param DbPassword: The database password.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_stack(StackId=None, Name=None, Attributes=None, ServiceRoleArn=None, DefaultInstanceProfileArn=None, DefaultOs=None, HostnameTheme=None, DefaultAvailabilityZone=None, DefaultSubnetId=None, CustomJson=None, ConfigurationManager=None, ChefConfiguration=None, UseCustomCookbooks=None, CustomCookbooksSource=None, DefaultSshKeyName=None, DefaultRootDeviceType=None, UseOpsworksSecurityGroups=None, AgentVersion=None):
    """
    Updates a specified stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stack(
        StackId='string',
        Name='string',
        Attributes={
            'string': 'string'
        },
        ServiceRoleArn='string',
        DefaultInstanceProfileArn='string',
        DefaultOs='string',
        HostnameTheme='string',
        DefaultAvailabilityZone='string',
        DefaultSubnetId='string',
        CustomJson='string',
        ConfigurationManager={
            'Name': 'string',
            'Version': 'string'
        },
        ChefConfiguration={
            'ManageBerkshelf': True|False,
            'BerkshelfVersion': 'string'
        },
        UseCustomCookbooks=True|False,
        CustomCookbooksSource={
            'Type': 'git'|'svn'|'archive'|'s3',
            'Url': 'string',
            'Username': 'string',
            'Password': 'string',
            'SshKey': 'string',
            'Revision': 'string'
        },
        DefaultSshKeyName='string',
        DefaultRootDeviceType='ebs'|'instance-store',
        UseOpsworksSecurityGroups=True|False,
        AgentVersion='string'
    )
    
    
    :type StackId: string
    :param StackId: [REQUIRED]\nThe stack ID.\n

    :type Name: string
    :param Name: The stack\'s new name.

    :type Attributes: dict
    :param Attributes: One or more user-defined key-value pairs to be added to the stack attributes.\n\n(string) --\n(string) --\n\n\n\n

    :type ServiceRoleArn: string
    :param ServiceRoleArn: Do not use this parameter. You cannot update a stack\'s service role.

    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: The ARN of an IAM profile that is the default profile for all of the stack\'s EC2 instances. For more information about IAM ARNs, see Using Identifiers .

    :type DefaultOs: string
    :param DefaultOs: The stack\'s operating system, which must be set to one of the following:\n\nA supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2018.03 , Amazon Linux 2017.09 , Amazon Linux 2017.03 , Amazon Linux 2016.09 , Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .\nA supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .\nCentOS Linux 7\nRed Hat Enterprise Linux 7\nA supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .\nA custom AMI: Custom . You specify the custom AMI you want to use when you create instances. For more information about how to use custom AMIs with OpsWorks, see Using Custom AMIs .\n\nThe default option is the stack\'s current operating system. For more information about supported operating systems, see AWS OpsWorks Stacks Operating Systems .\n

    :type HostnameTheme: string
    :param HostnameTheme: The stack\'s new host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack\'s instances. By default, HostnameTheme is set to Layer_Dependent , which creates host names by appending integers to the layer\'s short name. The other themes are:\n\nBaked_Goods\nClouds\nEurope_Cities\nFruits\nGreek_Deities_and_Titans\nLegendary_creatures_from_Japan\nPlanets_and_Moons\nRoman_Deities\nScottish_Islands\nUS_Cities\nWild_Cats\n\nTo obtain a generated host name, call GetHostNameSuggestion , which returns a host name based on the current theme.\n

    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: The stack\'s default Availability Zone, which must be in the stack\'s region. For more information, see Regions and Endpoints . If you also specify a value for DefaultSubnetId , the subnet must be in the same zone. For more information, see CreateStack .

    :type DefaultSubnetId: string
    :param DefaultSubnetId: The stack\'s default VPC subnet ID. This parameter is required if you specify a value for the VpcId parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for DefaultAvailabilityZone , the subnet must be in that zone. For information on default values and when this parameter is required, see the VpcId parameter description.

    :type CustomJson: string
    :param CustomJson: A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration JSON values or to pass data to recipes. The string should be in the following format:\n\n'{\\'key1\\': \\'value1\\', \\'key2\\': \\'value2\\',...}'\nFor more information about custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .\n

    :type ConfigurationManager: dict
    :param ConfigurationManager: The configuration manager. When you update a stack, we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.\n\nName (string) --The name. This parameter must be set to 'Chef'.\n\nVersion (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.\n\n\n

    :type ChefConfiguration: dict
    :param ChefConfiguration: A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see Create a New Stack .\n\nManageBerkshelf (boolean) --Whether to enable Berkshelf.\n\nBerkshelfVersion (string) --The Berkshelf version.\n\n\n

    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: Whether the stack uses custom cookbooks.

    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: Contains the information required to retrieve an app or cookbook from a repository. For more information, see Adding Apps or Cookbooks and Recipes .\n\nType (string) --The repository type.\n\nUrl (string) --The source URL. The following is an example of an Amazon S3 source URL: https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz .\n\nUsername (string) --This parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Username to the appropriate IAM access key ID.\nFor HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.\n\n\nPassword (string) --When included in a request, the parameter depends on the repository type.\n\nFor Amazon S3 bundles, set Password to the appropriate IAM secret access key.\nFor HTTP bundles and Subversion repositories, set Password to the password.\n\nFor more information on how to safely handle IAM credentials, see https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nSshKey (string) --In requests, the repository\'s SSH key.\nIn responses, AWS OpsWorks Stacks returns *****FILTERED***** instead of the actual value.\n\nRevision (string) --The application\'s version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.\n\n\n

    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: A default Amazon EC2 key-pair name. The default value is none . If you specify a key-pair name, AWS OpsWorks Stacks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see Using SSH to Communicate with an Instance and Managing SSH Access . You can override this setting by specifying a different key pair, or no key pair, when you create an instance .

    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see Storage for the Root Device .

    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack\'s layers.\nAWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. UseOpsworksSecurityGroups allows you to provide your own custom security groups instead of using the built-in groups. UseOpsworksSecurityGroups has the following settings:\n\nTrue - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.\nFalse - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on. Custom security groups are required only for those layers that need custom settings.\n\nFor more information, see Create a New Stack .\n

    :type AgentVersion: string
    :param AgentVersion: The default AWS OpsWorks Stacks agent version. You have the following options:\n\nAuto-update - Set this parameter to LATEST . AWS OpsWorks Stacks automatically installs new agent versions on the stack\'s instances as soon as they are available.\nFixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack\'s instances.\n\nThe default setting is LATEST . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.\n\nNote\nYou can also specify an agent version when you create or update an instance, which overrides the stack\'s default setting.\n\n

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_user_profile(IamUserArn=None, SshUsername=None, SshPublicKey=None, AllowSelfManagement=None):
    """
    Updates a specified user profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_profile(
        IamUserArn='string',
        SshUsername='string',
        SshPublicKey='string',
        AllowSelfManagement=True|False
    )
    
    
    :type IamUserArn: string
    :param IamUserArn: [REQUIRED]\nThe user IAM ARN. This can also be a federated user\'s ARN.\n

    :type SshUsername: string
    :param SshUsername: The user\'s SSH user name. The allowable characters are [a-z], [A-Z], [0-9], \'-\', and \'_\'. If the specified name includes other punctuation marks, AWS OpsWorks Stacks removes them. For example, my.name will be changed to myname . If you do not specify an SSH user name, AWS OpsWorks Stacks generates one from the IAM user name.

    :type SshPublicKey: string
    :param SshPublicKey: The user\'s new SSH public key.

    :type AllowSelfManagement: boolean
    :param AllowSelfManagement: Whether users can specify their own SSH public key through the My Settings page. For more information, see Managing User Permissions .

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_volume(VolumeId=None, Name=None, MountPoint=None):
    """
    Updates an Amazon EBS volume\'s name or mount point. For more information, see Resource Management .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_volume(
        VolumeId='string',
        Name='string',
        MountPoint='string'
    )
    
    
    :type VolumeId: string
    :param VolumeId: [REQUIRED]\nThe volume ID.\n

    :type Name: string
    :param Name: The new name.

    :type MountPoint: string
    :param MountPoint: The new mount point.

    :returns: 
    OpsWorks.Client.exceptions.ValidationException
    OpsWorks.Client.exceptions.ResourceNotFoundException
    
    """
    pass

