#!/bin/bash

function check()
{
 if [ ! $? -eq 0 ]
 then
  echo "[Korali] Error deploying site."
  exit -1
 fi 
}

currentBranch=`git rev-parse --abbrev-ref HEAD`
if [[ $currentBranch !=  "master" ]]; then
 echo "This is not Korali's master branch so webpage deployment is not performed."
 exit 0
fi

# Copying website to falcon (gateway)
echo $FALCON_FINGERPRINT >> ~/.ssh/known_hosts
tar -zcvf site.tar.gz site
scp -r site.tar.gz circleci@falcon.ethz.ch:websites/korali
check

# Copying from falcon to vladimirovich (host)

git branch | grep \* | grep master
if [ $? -eq 0 ] 
then
  echo "[Korali] Deploying to master webpage."
  ssh circleci@falcon.ethz.ch './update_master.sh'
  check
else
  echo "[Korali] Deploying to development webpage."
  ssh circleci@falcon.ethz.ch './update_development.sh'
  check
fi

echo "[Korali] Deploying complete."
