#!/bin/sh

dst=deployment.zip

[[ -f ${dst} ]] && rm ${dst}

cd ../.env/lib/python3.7/site-packages
zip -r9q ${OLDPWD}/${dst} .

cd $OLDPWD
zip -gq ${dst} *.py

echo "✅ build successful"
ls -l ${dst}
