#!/bin/bash
# sudo chmod +x *.sh
# ./launch-stack.sh

AWS_REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/')

MYNAME=${1:-pmd}
PROJECTNAME=${2:-diagrams}
TMPDIR=${3:-.tmp-gitrepo}   
S3BUCKET=${4:-$PROJECTNAME-$MYNAME}
SAMSTACK=${5:-$PROJECTNAME-$MYNAME-$AWS_REGION}
CFNSTACK=${6:-$PROJECTNAME-$MYNAME}
PIPELINEYAML=${7:-pipeline.yml}
OTHER=${8:-pmd-serverless}

sudo rm -rf $TMPDIR
mkdir $TMPDIR
cd $TMPDIR
git clone https://github.com/PaulDuvall/diagrams-as-code.git

aws s3api list-buckets --query 'Buckets[?starts_with(Name, `'$S3BUCKET'`) == `true`].[Name]' --output text | xargs -I {} aws s3 rb s3://{} --force

sleep 20

aws s3 mb s3://$S3BUCKET-$(aws sts get-caller-identity --output text --query 'Account')

aws cloudformation delete-stack --stack-name $CFNSTACK

aws cloudformation wait stack-delete-complete --stack-name $CFNSTACK

cd diagrams-as-code

aws cloudformation create-stack --stack-name $CFNSTACK --capabilities CAPABILITY_NAMED_IAM --disable-rollback --template-body file://$PIPELINEYAML --parameters


aws cloudformation create-stack --stack-name $CFNSTACK --template-body file://$PIPELINEYAML --parameters ParameterKey=BucketRoot,ParameterValue=$S3BUCKET-$(aws sts get-caller-identity --output text --query 'Account') --capabilities CAPABILITY_NAMED_IAM